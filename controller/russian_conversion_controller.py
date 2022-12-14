#!/usr/bin/env/python3

# script to convert english letters into russian
from pynput.keyboard import Key, Controller, Listener
from language.russian_conversion_map import russian_conversion_map, max_layer
from language.valid_words import ValidWordList
from model.russian_conversion_model import translate, spellcheck

# initialize global variables
stream = []
finished = False
output = ""
controller = Controller()
position = 0

# callback function for pressing a key on the keyboard
def on_press(key, valid_words: ValidWordList = None) -> None:
    global stream
    global finished
    global output
    global position

    try:
        print(key, position) # log key pressed and position at the stream

        # stop the running code
        if key == Key.esc:
            # end conversion
            return False

        # delete the last character from the stream
        elif key == Key.backspace:
            if len(stream) > 0:
                stream.pop()
            if len(output) > 0:
                output.pop()
            
            if (position > 0):
                position -= 1

        # translate the stream
        elif key == Key.space:
            if len(stream) == 0:
                finished = False
                positon = 0
            else:
                finished = True
                position = 0

        # move the position of the stream translation to the start
        elif key == Key.down:
            position = 0

        # move the position of the stream translation to the end
        elif key == Key.up:
            position = len(stream) - 1

        # move the position of the stream trasnlation left 1 (if exists)
        elif key == Key.left:
            if (position > 0):
                position -= 1
        
        # move the position of the stream translation to the right 1 (if exists)
        elif key == Key.right:
            if (position < len(stream)):
                position += 1

        # if the key pressed in the map of keys then we can insert it into the stream
        elif str(key).replace("'", "").lower() in russian_conversion_map.keys():
            stream.insert(position, str(key).replace("'", "").lower())
            position += 1
            # output = convert_to_russian(stream)
            # make stream process one input at a time
            # NOTE: remember a stream does not have to be an individual character added
    
    except AttributeError:
        print('key pressed: {0}'.format(key))


# callback function when the key is released from the keyboard
def on_release(key, valid_words: ValidWordList = None) -> None:   
    global controller
    global stream
    global finished
    global output
    global position

    # try translating the strema
    try:
        output = translate(stream, max_layer, russian_conversion_map)
    except:
        print("failed")

    print(stream, output) # log the stream and output
    
    # if the process is determined to be finished (if key space is pressed) then we can output the translated stream
    if finished:
        # clean up the typed english
        for _ in range(len(stream)+1):
            controller.press(Key.backspace)
            controller.release(Key.backspace)
        
        if valid_words is not None:
            output = spellcheck(output=output, valid_words=valid_words)
        
        # output the translated letters in the output
        for letter in output:
            controller.press(letter)
            controller.release(letter)

        # add one more space
        controller.press(" ")
        controller.release(" ")

        # reset everything back to its original position
        stream = []
        output = ""
        position = 0
        finished = False

    # if the esc key is pressed then stop the listener
    if key == Key.esc:
        # Stop listener
        return False   
