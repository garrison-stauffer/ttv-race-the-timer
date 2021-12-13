from websocket import create_connection
from pseudo_database import db
from constants import CLIENT_NAME, CLIENT_SECRET
import threading
import requests


def open_socket_connection(stream_token):
    # get an access token
    # get a socket token
    # open the socket on a new thread!
    ws = create_connection()


def get_access_token(steamer_code):
    request_body = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_NAME,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': 'http://dev.garrison-stauffer.com:51023/auth/callback',  # this should be an environment var too
        'code': steamer_code
    }

    headers = {
        'Accept': 'application/json'
    }

    response = requests.post(url='https://streamlabs.com/api/v1.0/token', data=request_body, headers=headers)
    print(response)
    print(response.text)

    json = response.json()
    print(json)

    return json['access_token']


def get_socket_token(access_token):
    response = requests.get(
        url=f'https://streamlabs.com/api/v1.0/socket/token?access_token={access_token}',
        headers={'Accept': 'application/json'}
    )

    print(response)
    print(response.request.url)
    print(response.text)

    json = response.json()
    print(json)

    return response['stream_token']
