from IPython.core.magic import register_cell_magic
from IPython.core.display  import display
from IPython.display import Audio

from utils.sounds import SoundMaker

s = SoundMaker()
beethoven_5 = s.make_melody([
    (['g4', 'g3'],.5), 
    (['g4', 'g3'],.5), 
    (['g4', 'g3'],.5), 
    (['eb4', 'eb3'],1),
])

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

@register_cell_magic('sound_notification')
def sound_notification(line, cell):
    try:
        exec(cell)
        display(Audio(s.make_woooop(), rate=s.default_rate, autoplay=True, normalize=True))
    except Exception as e:
        display(Audio(imperial_march, rate=s.default_rate, autoplay=True, normalize=True))
        raise e