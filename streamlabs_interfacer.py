import socketio
from pseudo_database import db
from constants import CLIENT_NAME, CLIENT_SECRET
import threading
import requests


class MyEventHandlerNamespace(socketio.ClientNamespace):
    def trigger_event(self, event, *args):
        print(f"{event}")
        if args:
            print(f'data is {args[0]}')


def open_socket_connection(stream_token):
    def foo():
        sio = socketio.Client()
        sio.register_namespace(MyEventHandlerNamespace())
        sio.connect(f'https://sockets.streamlabs.com?token={stream_token}')
        sio.wait()

    # get an access token
    # get a socket token
    # open the socket on a new thread!

    thread = threading.Thread(target=foo, name="StreamlabsWebSocket")
    thread.start()

    while not thread.is_alive():
        print('waiting for thread to go live')
    print(thread.is_alive())


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

    return json['socket_token']
