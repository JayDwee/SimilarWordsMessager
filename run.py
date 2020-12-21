#!/usr/bin/env python

"""
Similar Word Commenter
Made for HXGI

Commented using reStructuredText (reST)
"""
# Futures

# Built-in/Generic Imports
import time

# Libs
import requests
import keyboard

# Own modules

# Constants
ORIGINAL_WORD = "computer games"

# Variables


def auto_words(words):
    for word in words:
        keyboard.write(word)
        keyboard.press_and_release("enter")
        time.sleep(1)


def manual_words(words):
    for word in words:
        keyboard.write(word)
        keyboard.press_and_release("enter")
        keyboard.wait('esc')


def custom_manual_words(word):
    while True:
        keyboard.write(word)
        keyboard.press_and_release("enter")
        keyboard.wait('esc')


if __name__ == '__main__':
    r = requests.get("https://api.datamuse.com/words?ml="+ORIGINAL_WORD.replace(" ", "+"))
    words = []

    for e in r.json():
        words.append(e.get("word"))

    print(words, "\n\n\n")
    print("Waiting for ESC before starting")
    keyboard.wait('esc')

custom_manual_words("@Julz#1111 pls stop this")
