import pyfiglet
import colorama
import time


def initialize_game():
    font = pyfiglet.Figlet(font = 'doh', width = 50)
    print(font.rendertext('This is a test text.'))