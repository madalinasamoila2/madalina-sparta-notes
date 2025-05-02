### HANGMAN GAME 🙋‍♂️ ###


# STRUCTURE
# List of possible words
# A way to randomly choose one word
# A loop to allow the player to guess letters
# A win/loss conditions

import random
import streamlit as st

# --- Game Setup ---
st.title("🎯 Hangman Game")
st.markdown("Guess the secret word one letter at a time. You only get :green[6 wrong guesses]!")

# list of 10 words
mylist = ["mangosteen","lychee","guava","pomegranate","cactus","granadilla","pomelo","starfruit","jackfruit","acai"]

# choose random word from mylist
random_word = random.choice(mylist)
guessed_letters = []
tries = 6

# displate the current word state
def display_word():
    return " ".join([letter letter in guessed_letters else "_" for letter in word_to_guess])
# place random word in a letter list
letter_list = list(random_word)

# loop to allow the player to guess letters
for i in letter_list:


