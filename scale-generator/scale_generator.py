SHARP_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLAT_SCALE = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
USES_SHARP = ["C", "G", "A", "E", "F#", "D", "B", "e", "b", "f#", "c#", "g#", "d#", "a"] # This seems cumbersome, but there is no other way.
import itertools

class Scale:
    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        desired_scale = SHARP_SCALE if self.tonic in USES_SHARP else FLAT_SCALE
        index = desired_scale.index(self.tonic[0].upper() + self.tonic[1:]) # If the scale is minor, the first letter must be upper cased for the search.
        return desired_scale[index:] + desired_scale[0:index] # This reorders the scale so it starts and ends where it should.

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        iter = itertools.cycle(chromatic_scale) # The interval can loop over, so the chromatic scale as base should be cycled.
        scale = [next(iter)] # Start the scale with the tonic itself, iterating over the cycle.
        for interval in intervals: # Now just classify the steps. m is a half step, so advance once in the list. M is two halfs, A is 3. easy.
            if interval == 'm':
                scale.append(next(iter))
            elif interval == 'M':
                next(iter)
                scale.append(next(iter))
            elif interval == 'A':
                next(iter)
                next(iter)
                scale.append(next(iter))
            else:
                raise ValueError('No such type of interval.')
                
        return scale
        