import flask
import requests

app = flask.Flask(__name__)

# Replace these values with your actual client ID and secret ID
client_id = "3a68722813a646dd956affd097f5aafd"
client_secret = "71ee84a80a314930bf5c91a0a6e262ab"

# API token URL
APItok_Url = 'https://accounts.spotify.com/api/token'

# Request API token
auth_response = requests.post(APItok_Url, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})

# Extract token from response
auth_data = auth_response.json()
access_token = auth_data['access_token']

# Set up headers for API requests
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# Base URL for Spotify API
API_Url = 'https://api.spotify.com/v1/'

@app.route('/')
def index():
    # Get artist ID from URL parameter or set default value
    artist_id = flask.request.args.get('artist_id', '53XhwfbYqKCa1cC15pYq2q')

    # Request album data for the artist
    mainLink = requests.get(API_Url + 'artists/' + artist_id + '/albums', 
                 headers=headers, 
                 params={'market': 'ES', 'limit': 10, 'offset': 5})

    data = mainLink.json()

    return flask.render_template("index.html", data=data)

app.run(use_reloader = True, debug = True)
