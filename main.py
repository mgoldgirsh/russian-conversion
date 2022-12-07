from pynput.keyboard import Listener
from controller.russian_conversion_controller import on_press, on_release
from language.valid_words import ValidWordList


if __name__ == "__main__":
    valid_words = None
    path = "language/russian_words.txt"
    
    valid_words = ValidWordList(path)
    
    # initializes the listener so that it can translate letters
    with Listener(
            on_press= lambda key: on_press(key, valid_words=valid_words),
            on_release=lambda key: on_release(key, valid_words=valid_words)) as listener:
        listener.join()