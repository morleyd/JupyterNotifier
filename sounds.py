import json, os, re
import numpy as np

def correct_case(note):
    """Normalizes the case of an inputted note."""
    n = len(note)
    note_match = re.compile(r'^[A-Ga-g][#Bb]?[0-8]$')
    if not bool(re.search(note_match, note)) or n < 1 or n > 3:
        raise ValueError(f"Invalid note format {repr(note)}. Should be in form 'Ab4'")
    elif n == 1:
        return note.upper() + '4'
    elif n == 2:
        return note.upper()
    elif n == 3:
        return note[0].upper() + note[1].lower() + note[2]
    else:
        raise ValueError(f"Invalid note format {repr(note)}. Should be in form 'Ab4'")


class SoundMaker:
    def __init__(self, default_rate=44100):
        self.default_rate = default_rate
        fpath = os.path.join(os.path.dirname(__file__),'notes_map.json')
        with open(fpath) as f:
            self.notes_map = json.load(f)
            
    def get_freq(self, note):
        return self.notes_map[correct_case(note)]

    def make_note(self, note, duration=0.3):
        """    
        Parameters:       
           note in string form, e.g. 'c4', 'f#2', 'ab5'
           duration of the sound (in seconds)
        Returns np.array data with the tone
        """
        nsamples = int(self.default_rate*duration)
        t = np.linspace(0, duration, nsamples)
        return np.sin(self.get_freq(note)*2*np.pi*t)

    def make_pause(self, shape=1, duration=.1):
        """Helper function that creates a brief pause between notes"""
        nsamples = int(self.default_rate*duration)
        t = np.linspace(0, duration, nsamples)
        return np.vstack([t for _ in range(shape)])

    def make_chord(self, notes, duration=0.3):
        """
        Combines a list of notes into a single chord
        Parameters:       
           list of notes in string form, e.g. ['c4', 'f#2', 'ab5']
           duration of the sound (in seconds)
        Returns np.array data with the tone    
        """
        if isinstance(notes, list):
            return np.vstack([self.make_note(note, duration) for note in notes])
        elif isinstance(notes, str):
            return self.make_note(notes, duration)
        else:
            raise ValueError(f"Invalid note format {repr(notes)}.")

    def make_melody(self, notes):
        """Combines a list of chords into a melody
        Parameters:
           list of chord tuples where first element is list of notes and second 
                is the duration in seconds, e.g. [(['c4', 'f#2', 'ab5'], .5)]
        Returns np.array data with the tone 
        """
        out = []
        for note, duration in notes:
            chord_n = len(note) if isinstance(note, list) else 1
            out.append(np.hstack([self.make_chord(note, duration), self.make_pause(chord_n)]))
        return np.hstack(out)

    def make_woooop(self, duration=1.5):
        """Fun function playing with other types of sine waves"""
        nsamples = int(self.default_rate*duration)
        t = np.linspace(0, duration, nsamples)
        woop = np.sin(220*2*np.pi*t**2)
        return np.hstack([woop[:-35], woop[::-1]])