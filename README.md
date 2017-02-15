# Spilltweet

[Spilltweet](http://spilltweet.com/) &mdash; when your tweets are just too long!


Spilltweet is a neat little tool that lets you post large tweets ( > 140 characters) as pictures. All you have to do is enter (or paste) your text, and Spilltweet will convert them to pictures and tweet them for you.

> **Please note**: This is a guide for people who want to set up Spilltweet on their own. If you are a Spilltweet user and looking for help using the app, [read the help section](http://spilltweet.com/help). You can also access the help section by clicking `Help` at the top-right section of the page on Spilltweet.

-

### How it works

Spilltweet renders the resulting markup of your text in a hidden `iframe`. This markup is then converted to a `canvas` object, from which we get the image. The image is then sent to the server, which posts it on Twitter.

-

### Getting Spilltweet

Clone this repository using `git`:
```
 $ git clone https://github.com/cepradeep/spilltweet.git
 $ cd spilltweet
```

Or [download the source](https://github.com/cepradeep/spilltweet/archive/master.zip) as a zip file.

-

### Dependencies

Spilltweet runs on the `Flask` web framework. The recommended way to setup Spilltweet for development is inside a `virtualenv`. After ensuring you have `python`, `pip` and `virtualenv` installed, run:

```
 $ virtualenv flask
 $ source flask/bin/activate
 $ pip install -r requirements.txt
```

-

### Configuration

Create a `config.py` file by copying the sample configuration file included with Spilltweet.
```
 $ cp app/config.default.py app/config.py
```

Open `config.py` in your favorite text editor. There are three variables which you must change inside `config.py`:

 - **`SECRET_KEY`:**  
   It's important that you change the `SECRET_KEY` to a random value, as this will be used by Flask to encrypt the sessions.

 - **`TWITTER_KEY`:**  
    Spilltweet requires a valid Twitter API Key to work, which you can get by creating a [Twitter App](https://apps.twitter.com/). There are numerous tutorials on the web explaing how to do this.
   
   After you have created a Twitter app, navigate to it's *Keys and Access Tokens* section. Copy the value against the _Consumer Key (API Key)_ field. This is your `TWITTER_KEY`.

 - **`TWITTER_SECRET`:**  
   On the same page, copy the value against the *Consumer Secret (API Secret)* field. This is your `TWITTER_SECRET`.

Save `config.py` and exit.

> **Note:** Never include this file in your repo or share it publicly, as this contains your API keys.

-

### Running Spilltweet

To run Spilltweet for development, you can use the `runserver.py` script that comes bundled with Spilltweet.
```
 $ chmod a+x runserver.py
 $ ./runserver.py
```
You can see the app by navigating to `http://127.0.0.1:5000/` on your web browser.

If you don't want to flood your Twitter timeline while testing, you can set the `SPILLTWEET_DEBUG` environment variable. This will cause Spilltweet to save the posted images to the `app/tmp/` directory instead of tweeting them.

```
 $ export SPILLTWEET_DEBUG=1
 $ ./runserver.py
```

-

### Copying and Distributing

Spilltweet is a hobby project. You are welcome to use Spilltweet, copy it, tinker with it and distribute it. You may use it for commercial purposes, but you may not sell / charge for Spilltweet or the service / functionality it provides.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Attribution-ShareAlike 4.0 International License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>

-

### Credits

Spilltweet relies on [HTML2Canvas](https://github.com/niklasvh/html2canvas) and [Quill.js](https://github.com/quilljs/quill), and is thankful to their developers.

-

All copyrights and trademarks belong to their respective owners.

Spilltweet is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. in no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
