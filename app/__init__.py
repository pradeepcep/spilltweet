from flask import *
from flask_oauth import OAuth


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
        flash('You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        oauth_response['oauth_token'],
        oauth_response['oauth_token_secret']
    )

    # We will use the presence of twitter_user in session to indicate if the
    # user is logged in or not.
    session['twitter_user'] = oauth_response['screen_name']
    flash('Welcome, @%s!' % oauth_response['screen_name'])

    # Once authorized, get some basic info about the user.
    tw_response = twitter.get(
        'users/show.json?screen_name=%s' % session['twitter_user'])
    if tw_response.status == 200:
        session['user_info'] = tw_response.data
    else:
        flash('There was an error in reading you Twitter info.')

    return redirect(next_url)


@app.route('/logout')
def logout():
    session.pop('twitter_token', None)
    session.pop('twitter_user', None)
    session.pop('user_info', None)
    flash('You were successfully logged out.')
    return redirect(request.args.get('next') or url_for('index'))
