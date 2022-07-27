import os
from IPython.core.magic import register_cell_magic
from IPython.core.display  import display
from IPython.display import Audio
from time import time

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .sounds import SoundMaker

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

@register_cell_magic('message_notification')
def message_notification(line, cell):
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    try:
        start = time()
        exec(cell)
        display(Audio(s.make_woooop(), rate=s.default_rate, autoplay=True))
        message = Mail(
            from_email=os.environ.get('FROM_EMAIL'),
            to_emails=os.environ.get('TO_EMAIL'),
            subject='Success!',
            plain_text_content=f'Code executed in {(time()-start)/60:.2f} minutes.'
        )
        response = sendgrid_client.send(message)
    except Exception as e:
        display(Audio(imperial_march, rate=s.default_rate, autoplay=True))
        message = Mail(
            from_email=os.environ.get('FROM_EMAIL'),
            to_emails=os.environ.get('TO_EMAIL'),
            subject='Failure',
            plain_text_content=f'Code raised {repr(e)} after {(time()-start)/60:.2f} minutes.'
        )
        response = sendgrid_client.send(message)
        raise e