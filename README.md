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
and then import the notification module:
```python
from JupyterNotifier.notifications import sound_notification
```
now whenever you want a notification, use the magic `%%sound_notification` at the top of the relevant cell.

Note: `numpy` is the only package used not from the Standard Library. Make sure that is installed (the specific version shouldn't matter much because it's not doing anything too fancy).

## Contents
This package contains two modules, `notifications.py` and `sounds.py`. The latter is intended as a helper module to enable sound effect notifications. Nonetheless, `sounds.py` can be used as a stand alone module to make any sound byte. Each function within the `SoundMaker` class can be used separately or in conjunction with each other. The following example shows the creation of the Imperial March motif and should play automatically in a jupyter notebook.
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
 - Fix make melody to support different size chords
 - Include different types of notifications, like text or email.
    * I used to use [yagmail](https://github.com/kootenpv/yagmail) or even just [smtplib](https://docs.python.org/3/library/smtplib.html) with my gmail. However, since Google has stopped supporting Less Secure Apps, this is more challenging.
    * I attempted to use an App Password with 2-step Authentication, but have not been successful
