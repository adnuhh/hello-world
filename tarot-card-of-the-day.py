#!/bin/python3

import webbrowser
import random


def generate_tarot_card():
    suits = {"w", "s", "c", "p", "maj"}
    suit_values = {"a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "pg", "kn", "qn", "kg"}
    arcana_values = {"00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"}
    
    my_card = ""
    my_suit = random.sample(suits, 1)[0]
    
    if my_suit == "maj":
        my_card = my_suit + random.sample(arcana_values, 1)[0]
    else:
        my_card = my_suit + random.sample(suit_values, 1)[0]
    
    return my_card

def main():
    card = generate_tarot_card()
    url = "learntarot.com/{}.htm"
    webbrowser.open(url.format(card))
    return

if __name__=="__main__":
    main()
