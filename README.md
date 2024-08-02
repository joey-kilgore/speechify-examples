# SPEECHIFY-EXAMPLES

## Setup
Go to the speechify website and request and API https://speechify.com/blog/category/api/

In `constants.py` copy and paste the API key into the quotations

Run the following commands to setup a virtual environment and install requirements

```
$ virtualenv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
```

## Hello World
The `hello-world.py` script is the simplest example of converting text to speech  
To run, use the following code snippet

```
$ source myenv/bin/activate
$ python3 ./hello-world.py
```