# Some configurations and keys.

# Secret key for sessions
SECRET_KEY = '<insert your secret key here>'

# Twitter credentials
TWITTER_KEY = '<insert your Twitter Consumer Key>'
TWITTER_SECRET = '<insert your Twitter Consumer Secret here>'

# Twitter URLs
TWITTER_BASE_URL = 'https://api.twitter.com/1.1/'
TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
TWITTER_AUTHORIZE_URL = 'https://api.twitter.com/oauth/authenticate'
TWITTER_MEDIA_UPLOAD_URL = 'https://upload.twitter.com/1.1/media/upload.json'

# URLs for external styles and JS.
JQUERY_URL = 'https://code.jquery.com/jquery-3.1.1.slim.min.js'
JQUERY_SUM = 'sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3h' + \
    'pfag6Ed950n'

BOOTSTRAP_CSS_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha' + \
    '.6/css/bootstrap.min.css'
BOOTSTRAP_CSS_SUM = 'sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQ' + \
    'QKnKkoFVhFQhNUwEyJ'

BOOTSTRAP_JS_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.' + \
    '6/js/bootstrap.min.js'
BOOTSTRAP_JS_SUM = 'sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVk' + \
    'E+jo0ieGizqPLForn'

TETHER_JS_URL = 'https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/' + \
    'tether.min.js'
TETHER_JS_SUM = 'sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx' + \
    '6Qin1DkWx51bBrb'

HTML2CANVAS_URL = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/' + \
    '0.4.1/html2canvas.min.js'
HTML2CANVAS_SUM = 'sha256-c3RzsUWg+y2XljunEQS0LqWdQ04X1D3j22fd/8JCAKw='

FONT_URL = 'https://fonts.googleapis.com/css?family=Bitter|Indie+Flower|' + \
    'Satisfy|Source+Sans+Pro'
FONT_NAMES = {
    # Always use single quotes for font names. Eg. 'Source Sans Pro'. Using
    # double quotes here will break the template.
    'Source Sans Pro': "'Source Sans Pro', sans-serif",
    'Satisfy': "'Satisfy', cursive",
    'Indie Flower': "'Indie Flower', cursive",
    'Bitter': "'Bitter', serif",
}
FONT_SIZES = {
    # It's recommended that sizes be specified in pixels. This ensures
    # consistent image sizes across all screen sizes/resolutions.
    'Extra Large': '36px',
    'Large': '24px',
    'Normal': '14px',
}
