from enum import IntEnum, auto

# Create an enumerate for every possible status for a bowling frame. 
class RollStatus(IntEnum):
    REGULAR = auto()
    SPARE = auto()
    STRIKE = auto()


class BowlingGame:
    def __init__(self):
        self.__frames = [[] for i in range(10)]
        self.__statuses = [[] for i in range(10)]
        self.__current_frame = 0 
        self.__pins_last_frame = 10 # Given the nature of the bonus rolls, we have to keep track of how pins there are.

    def roll(self, pins: int):
        if pins < 0 or pins > 10: # Verify impossible roll
            raise ValueError("Invalid number of pins")
        if self.__current_frame != 9: # Every frame pre-last uses the same rules.
            self.__frames[self.__current_frame].append(pins) # We attach the pins to the list representing the current frame.
        if sum(self.__frames[self.__current_frame]) > 10 and self.__current_frame < 9: # Every normal frame can only have max 10 pins.
            raise ValueError("There are not more than 10 pins in a frame")
        # Last frame is very special and requires a logic of its own.
        if self.__current_frame == 9:
            if self.__statuses[self.__current_frame] != RollStatus.REGULAR and self.__pins_last_frame == 0:
                # If we have a strike or spare AND the pins were cleared, we put 10 more. 
                self.__pins_last_frame = 10 
            self.__pins_last_frame -= pins 
            if self.__pins_last_frame < 0: # If we roll more than we can, we get negative pins and the roll was invalid. The game was over.
                raise ValueError("There are no more rolls. Game over.")  
            if self.__statuses[self.__current_frame] != RollStatus.REGULAR: # If we have a strike or spare, the last frame has 3 rolls.
                expected_len = 3
            else: # If not, it's just 2 rolls as usual.
                expected_len = 2            
            self.__frames[self.__current_frame].append(pins)
            if len(self.__frames[self.__current_frame]) > expected_len: # If we have more rolls than expected, the game should've ended.
                raise ValueError("There are no more rolls. Game over.")  
        # This part only attributes the proper status to the frame
        if pins == 10: # Strike
            self.__statuses[self.__current_frame] = RollStatus.STRIKE
            if self.__current_frame < 9: # Once the strike happens, usually we go to the next frame.
                self.__current_frame += 1
        elif sum(self.__frames[self.__current_frame]) == 10: # Spare
            self.__statuses[self.__current_frame] = RollStatus.SPARE
        elif not self.__statuses[self.__current_frame]: # Only if it's not strike or spare and we have no status it's a regular.
            self.__statuses[self.__current_frame] = RollStatus.REGULAR # This not prevents overwrite of the last frame's status post-strike.
        if len(self.__frames[self.__current_frame]) >= 2 and self.__current_frame < 9: # Normal frames will end after 2 rolls.
            self.__current_frame +=1

    def score(self) -> int: 
        if len(self.__frames[0]) == 0 or len(self.__frames[9]) == 0: # If there's not enough throws in the first or last frame, the game wasn't done yet.
            raise ValueError("Not enough throws")
        score = 0
        for frame_counter, frame in enumerate(self.__frames): # Iterate over everything. 
            if frame_counter != 9: # Again, scoring for all frames but the last is the same. 
                if self.__statuses[frame_counter] == RollStatus.STRIKE: # Strike rule: score the following 2 rolls once again.
                    if len(self.__frames[frame_counter + 1]) < 2: # If the next frame is 1 roll long (a strike)
                        score += self.__frames[frame_counter+2][0] # Then we have to go to the first roll 2 frames ahead! (So we get the following 2 rolls)
                    score += sum(self.__frames[frame_counter+1][0:2]) # Regardless, we sum the first two rolls of the next frame (no error if the frame is shorter/longer)
                elif self.__statuses[frame_counter] == RollStatus.SPARE: # Spare rule: score the following roll once again.
                    score += self.__frames[frame_counter+1][0]
            else: 
                if self.__statuses[frame_counter] != RollStatus.REGULAR: # We do the same logic as in the roll method.
                    expected_len = 3
                else:
                    expected_len = 2
                if len(frame) < expected_len: # However, here we check to see if the score method was only called AFTER all rolls have been done.
                    raise ValueError("Unable to score, the game is not over.")     
            score += sum(frame)
        return score

