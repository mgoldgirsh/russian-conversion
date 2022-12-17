from pynput.keyboard import Listener
from controller.russian_conversion_controller import on_press, on_release
from language.valid_words import ValidWordList
import sys


if __name__ == "__main__":
    path = None
    index = 0

    # obtains arguments from the command line to determine spell checking list
    while index < len(sys.argv):
        if sys.argv[index] == '-p' or sys.argv[index] == "--path":
            index += 1
            path = sys.argv[index]
    
        index += 1
    
    if path is not None:
        valid_words = ValidWordList(path)
    else:
        valid_words = None
    
    # initializes the listener so that it can translate letters
    with Listener(
            on_press= lambda key: on_press(key, valid_words=valid_words),
            on_release=lambda key: on_release(key, valid_words=valid_words)) as listener:
        listener.join()