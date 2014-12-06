#Disciple-Py

Requirements:

* Python 2.7
* MongoDB

Running:

1. Create a virtualenv for developing. If you don't know how to do so, you can find out [here](https://virtualenv.pypa.io/en/latest/). You can also use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) as well.
2. Download the dependencies via `pip install -r requirements.txt`
3. Make sure MongoDB is running
4. Update config.py with the appropriate settings
5. Run via `python main.py`

Whenever adding requirements to requirements.txt, be sure to do it via `pip freeze -l > requirements.txt` to make sure you only add libraries installed in the virtualenv.