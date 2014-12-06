#Disciple-Py

Requirements:

* Python 2.7
* MongoDB

Setup:

1. Create a virtualenv. If you don't know how to do so, you can find out [here](https://virtualenv.pypa.io/en/latest/). You can also use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) as well.
2. Download the dependencies via `pip install -r requirements.txt`


Running:

1. Make sure MongoDB is running
2. Update config.py with the appropriate settings
3. Run via `python main.py`

Testing:

1. Run tests via the command, `nosetests`

Whenever adding requirements to requirements.txt, be sure to do it via `pip freeze -l > requirements.txt` to make sure you only add libraries installed in the virtualenv.