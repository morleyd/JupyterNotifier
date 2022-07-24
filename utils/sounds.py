import numpy as np
import json
    
def correct_case(note):
    """Normalizes the case of an inputted note.
    TODO: Edit so that value error catches all malformed notes, e.g. Bb
    """
    n = len(note)
    if n == 1:
        return note.upper() + '4'
    elif n == 2:
        return note.upper()
    elif n == 3:
        return note[0].upper() + note[1:]
    else:
        raise ValueError(f"Invalid note format {repr(notes)}. Should be in form 'Ab4'")


class SoundMaker:
    def __init__(self, default_rate=44100):
        self.default_rate = default_rate

        with open('notes_map.json') as f:
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
        nsamples = int(self.default_rate*duration)
        t = np.linspace(0, duration, nsamples)
        return np.vstack([t for _ in range(shape)])

    def make_chord(self, notes, duration=0.3):
        """
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
        out = []
        for note, duration in notes:
            chord_n = len(note) if isinstance(note, list) else 1
            out.append(np.hstack([self.make_chord(note, duration), self.make_pause(chord_n)]))
        return np.hstack(out)

    def make_woooop(self, duration=1.5):
        nsamples = int(self.default_rate*duration)
        t = np.linspace(0, duration, nsamples)
        woop = np.sin(220*2*np.pi*t**2)
        return np.hstack([woop[:-35], woop[::-1]])