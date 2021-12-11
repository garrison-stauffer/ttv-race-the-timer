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

