# JupyterNotifier
Cell magic for sending notifications for long code

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
 - Include different types of notifications, like cell or email
