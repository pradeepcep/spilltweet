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
    return render_template('index.html')


@app.route('/login')
def login():
    if 'twitter_token' not in session or session['twitter_token'] is None:
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
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash('You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']

    flash('Welcome, @%s!' % resp['screen_name'])
    return redirect(next_url)


@app.route('/logout')
def logout():
    session.pop('twitter_token', None)
    session.pop('twitter_user', None)
    flash('You were successfully logged out.')
    return redirect(request.args.get('next') or url_for('index'))
