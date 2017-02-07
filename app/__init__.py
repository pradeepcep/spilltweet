from flask import *
from flask_oauth import OAuth


from os import environ

app = Flask(__name__)
app.config.from_object('app.config')


# Create the twitter object to interact with twitter OAuth.
oauth = OAuth()
twitter = oauth.remote_app(
    'twitter',
    base_url=app.config['TWITTER_BASE_URL'],
    request_token_url=app.config['TWITTER_REQUEST_TOKEN_URL'],
    access_token_url=app.config['TWITTER_ACCESS_TOKEN_URL'],
    authorize_url=app.config['TWITTER_AUTHORIZE_URL'],
    consumer_key=app.config['TWITTER_KEY'],
    consumer_secret=app.config['TWITTER_SECRET'])


@app.route('/')
def index():
    if 'twitter_user' in session:
        return render_template('authorized_index.html')
    return render_template('index.html')


@app.route('/login')
def login():
    if 'twitter_user' not in session:
        return twitter.authorize(
            callback=url_for(
                'oauth_authorized',
                next=request.args.get('next') or request.referrer or None))
    else:
        return redirect(url_for('index'))


@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')


@app.route('/oauth_authorized')
@twitter.authorized_handler
def oauth_authorized(oauth_response):
    next_url = request.args.get('next') or url_for('index')
    if oauth_response is None:
        flash('You denied the request to sign in.', 'danger')
        return redirect(next_url)

    session['twitter_token'] = (
        oauth_response['oauth_token'],
        oauth_response['oauth_token_secret']
    )

    # We will use the presence of twitter_user in session to indicate if the
    # user is logged in or not.
    session['twitter_user'] = oauth_response['screen_name']
    flash('Welcome, @%s!' % oauth_response['screen_name'], 'success')

    # Once authorized, get some basic info about the user.
    tw_response = twitter.get(
        'users/show.json?screen_name=%s' % session['twitter_user'])
    if tw_response.status == 200:
        session['user_info'] = tw_response.data
    else:
        flash('There was an error in reading you Twitter info.', 'danger')

    return redirect(next_url)


@app.route('/logout')
def logout():
    session.pop('twitter_token', None)
    session.pop('twitter_user', None)
    session.pop('user_info', None)
    flash('You were successfully logged out.', 'info')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/postimage', methods=['GET', 'POST'])
def postimage():
    # Don't allow if not logged in.
    if 'twitter_user' not in session:
        flash('You must login before you can post tweets.', 'danger')
        return redirect(url_for('index'))

    if not request.form.get('imagedata'):
        return redirect(url_for('index'))
    else:
        imagedata = request.form.get('imagedata')

    if imagedata and imagedata.startswith('data:image/png;base64,'):
        imagedata = imagedata.replace('data:image/png;base64,', '')

        # Allow for debugging without getting banned from Twitter :)
        if environ.get('SPILLTWEET_DEBUG') \
                and environ.get('SPILLTWEET_DEBUG') == '1':
            # Generate a unique filename and save the image instead of posting.
            from base64 import b64decode
            from hashlib import sha512
            filename = session['twitter_user'] + '_' + \
                ''.join(sha512(imagedata).hexdigest()[:20]) + '.png'
            with open(app.root_path + '/tmp/' + filename, 'wb') as imagefile:
                imagefile.write(b64decode(imagedata))
                flash(
                    'Successfully wrote image to %s' % (imagefile.name),
                    'success')
        else:
            tw_response = twitter.post(
                app.config['TWITTER_MEDIA_UPLOAD_URL'],
                data={'media_data': imagedata},
                )
            # Media upload successful.
            if tw_response.status == 200:
                tw_status_response = twitter.post(
                    'statuses/update.json',
                    data={
                        'status': '',
                        'media_ids': [tw_response.data['media_id_string']]})
                # Posting a status using that media was successful as well.
                if tw_status_response.status == 200:
                    flash('Successfully posted tweet!', 'success')
                else:
                    flash('Unable to post tweet. Please try again.', 'danger')
            else:
                flash('Unable to post image. Please try again.', 'danger')

        return redirect(url_for('index'))
    else:
        flash('Sorry, there was an error posting the image.', 'danger')
        return redirect(url_for('index'))
