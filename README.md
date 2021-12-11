Hello world, simple readme.

## Starting the environment

I set up the app using python3 (3.8.6).
There is a virtual environment set up for the app to lock a certain python version, as well as setting up dependencies.

Activate the virtual environment by running:

```
source timerapp/bin/activate

# If on windows you can run:
timerapp\Scripts\activate
```

Install any added libraries by running:
```
pip install -r requirements.txt
```

note: if any new requirements are added, they need to be "frozen" into the requirements file using:
```
pip freeze > requirements.txt
```

To start the app locally run:
```
python app.py
```

This will start the app on 51023, you can visit it at <a href="localhost:51023">localhost:51023</a>.

## General Design

### OAuth 2 Workflow

This is going to be a workflow we need to build into the app with proper web pages.
This is what gets us an access_token to subscribe to QT's stream of updates on the socket api (https://dev.streamlabs.com/docs/socket-api).

My proposal is to add a list of sub-endpoints like:
```
localhost:51023/auth/login     # this is the base for our page, will direct users to the SL endpoint
                               # through some mechanism tbd (js or 302, not sure)

localhost:51023/auth/callback  # Endpoint SL will redirect users to, this is how we get the access + refresh tokens
```

We will need to store the data.
To start we can maybe just use local variables - but they will not be durable if we restart the app in the cloud.
Eventually, I think we can cache them in a database.

Sign in flow for our app:
- User visits `/auth/login` and enters a random ID (We can generate a UUID for them)
    - this id will be what is used to identify them and the key to access/refresh tokens in the database
- User is sent to StreamLabs to approve our app to have access to them

- User uses their secret token to access an admin endpoint `/admin` - they enter their token in the page so that it is not stored in URL history
    - this page lets them control the timer/config settings
    - this is not needed for MVP, we can work with QT to set default config for lego stream and update on the fly as needed (e.g. 15 minute timer on reset and +/- 30 seconds per donation)
- User can enter the url `localhost:51023/obsplugin/{token}` in their OBS web browser plugin
    - this is the read only page with the countdown

Eventually we probably need some proper login, maybe we can use twitch auth for them to sign in.
Not too worried about it for the time being since it should be short lived.

## Helpful guides/documents:
### Setting OAuth 2 with StreamLabs
https://dev.streamlabs.com/docs/connecting-to-an-account

### StreamLabs Socket API
https://dev.streamlabs.com/docs/socket-api

### Setting up http files with Flask
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

This will be helpful for building pages in the above flow.
