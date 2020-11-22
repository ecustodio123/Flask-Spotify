from requests import get

AUTH_ENDPOINT = 'https://accounts.spotify.com/authorize'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
GET_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}'
RELATED_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/related-artists'
TOP_TRACKS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/top-tracks'
TOKEN_FIELD = 'BQCzeUOSN-gFs2grjeLIHq0jvqatlJyKSWurx0jWKMbmaooASVNX55YjgCe7TeuOUHKUTO5IlOeGU90zWKYA5VttnZ3CkYF6tct14ElUTFKr79h2Us2eDEW8jdFtsXfET-linNREWi__URiSnPNcOShvvaqiAvJPomdu-OZ647xEyhtf2D5ez0mcIWXLMlIUiM9_DwuIdV8POzfMKzswPikoAYOE3XT0s68_O7Qf4YoDMAznK0-UPHnX6eMRPHoi5vJ1ZpG4I8IZ9P1T7Ayb'


def auth_token():
    return TOKEN_FIELD


def search_by_artist_name(name):
    params = { 'type': 'artist' }
    params['q'] = name
    token = auth_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = get(SEARCH_ENDPOINT, params=params, headers=headers)
    return response.json()

def get_artist(artist_id):
    url = GET_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = get(url, headers=headers)
    return response.json()

def get_related_artists(artist_id):
    url = RELATED_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = get(url, headers=headers)
    return response.json()

def get_artist_top_tracks(artist_id, market='US'):
    url = TOP_TRACKS_ENDPOINT.format(id=artist_id)
    params = {'market': market}
    token = auth_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = get(url, params=params, headers=headers)
    return response.json()
