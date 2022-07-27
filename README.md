# JupyterNotifier
Cell magic for sending notifications for long code

## Background
I made a tool that notifies the user about code evaluation whether or not it met an exception. In my work, I often run long executing code – like training neural networks or mass web scraping – and it’s inefficient to just wait for it to finish. However, it also doesn’t do to have to check back to see if it errored out, when using a Google Colab notebook, if the code raises an exception, it stops executing before any notification code. 

This method fixes that. Whether or not the code finishes successfully this cell magic will send a notification as desired.

## Useage
This code is designed to run in a jupyter/Google Colab notebook, so in any cell, clone this repository:
```Notebook
!git clone https://github.com/morleyd/JupyterNotifier.git
```
### Basic Sound Notification
For the `basic.py` notification (just sounds for now) make sure that `numpy` is installed. Beyond that, just import the module and declare the cell magic:
```python
from JupyterNotifier.basic import sound_notification
```
now whenever you want a notification, use the magic `%%sound_notification` at the top of the relevant cell.

### Email/Text Notifications
This one is a little more tricky because you have to link your email in some way. Before May 2022, I would just use [yagmail](https://github.com/kootenpv/yagmail) or even just [smtplib](https://docs.python.org/3/library/smtplib.html) with my gmail account. However, since Google has stopped supporting Less Secure Apps, this is more challenging. Some have had success with [App Passwords](https://support.google.com/accounts/answer/185833), but not I.

Instead, I recommend setting up a free accound with [SendGrid](https://sendgrid.com/pricing/). It allows you to send 100 emails a day (supposedly forever).

Once you are have an account set up with SendGrid, run `pip install sendgrid` to get your system ready. The last thing you need to do is declare environment variables that store 
  - Your SendGrid API Key
  - An email registered with SendGrid to send from
  - The email (or emails) you are sending to
If you are using a notebook (as this repo assumes) I recommend using `os`:
```python
import os

os.environ['SENDGRID_API_KEY'] = 'Your API Key'
os.environ['FROM_EMAIL'] = 'from@example.com'
os.environ['TO_EMAIL'] = 'to@example.com'
```
Now the useage is the same as with the Basic module: `from JupyterNotifier.email import message_notification` and declare `%%message_notification` at the top of the desired cell.

#### A note about text messages
For my lifestyle, receiving a text notification is far more useful than an email. Luckily, you can send texts as emails as long as you know the service provider.
  - AT&T: phonenumber@txt.att.net
  - T-Mobile: phonenumber@tmomail.net
  - Sprint: phonenumber@messaging.sprintpcs.com
  - Verizon: phonenumber@vtext.com or phonenumber@vzwpix.com
  - Virgin Mobile: phonenumber@vmobl.com
  - Google Fi: phonenumber@msg.fi.google.com
This [resource](https://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/) or a web search will have a more comprehensive list. Also note that the addresses above are for basic SMS messages. Do a quick search to double check it if you need to send a MMS.

## Contents
This package contains two notification modules, `basic.py` & `email.py`. Most of the code is duplicated between the two, but I didn't want to force users to have to install/comment out SendGrid if they didn't plan on using it. This repo also includes a fun helper module, `sounds.py`. This contains the SoundMaker class that simplifies making wacky music. I could have just used a sound byte from the web, but this seemed more fun. 

It should be noted that `sounds.py` can be used as a stand alone module to make any sound byte. Each function within the `SoundMaker` class can be used separately or in conjunction with each other. The following example shows the creation of the Imperial March motif and should play automatically in a jupyter notebook.
```python
from IPython.display import Audio
from JupyterNotifier.sounds import SoundMaker

s = SoundMaker()
imperial_march = s.make_melody([
    (['e4', 'e3'],.6), 
    (['e4', 'e3'],.6), 
    (['e4', 'e3'],.6), 
    (['c4', 'c3'],.4),
    (['g4', 'g3'],.2),
    (['e4', 'e3'],.6), 
    (['c4', 'c3'],.4),
    (['g4', 'g3'],.2),
    (['e4', 'e3'],1),     
])
Audio(imperial_march, rate=s.default_rate, autoplay=True)
```

## TODO
 - Fix `make_melody` to support different size chords