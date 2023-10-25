from flask import Flask, render_template
from joplin_utils import joplin_note_search, joplin_note_body
import random

app = Flask(__name__)

def deck_generator(deck: str) -> list[str]:
    cards = joplin_note_body(joplin_note_search(f'The Skin-Deep - {deck}')[0]['id']).split('\n\n')
    random.shuffle(cards)
    return cards

@app.route("/")
def home():
    decks = {
        "Self": "#4D167E",
        "Strangers": "#E7A300",
        "Friends": "#EC7A00",
        "Dating": "#D62363",
        "Healing": "#76B42A",
        "Couples": "#CDCDCD",
        "Long-term Couples": "#7A0E2D"
        }
    return render_template('menu.html', decks = decks)

@app.route("/self")
def self():
    return render_template('deck.html', cards = deck_generator('Self'))

@app.route("/strangers")
def strangers():
    return render_template('deck.html', cards = deck_generator('Strangers'))

@app.route("/friends")
def friends():
    return render_template('deck.html', cards = deck_generator('Friends'))

@app.route("/dating")
def dating():
    return render_template('deck.html', cards = deck_generator('Dating'))

@app.route("/healing")
def healing():
    return render_template('deck.html', cards = deck_generator('Healing'))

@app.route("/couples")
def couples():
    return render_template('deck.html', cards = deck_generator('Couples'))

@app.route("/long_term_couples")
def long_term_couples():
    return render_template('deck.html', cards = deck_generator('Long-term Couples'))
