"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MartinFeller import app
import sqlite3


@app.route('/')
@app.route('/home')
def home():
    conn = sqlite3.connect("martinfeller.db")
    c = conn.cursor()
    """Renders the home page."""
    c.execute('SELECT * FROM songs')
    rowlist = []
    for row in c.execute('SELECT * FROM songs'):
        rowlist.append(row)
    return render_template(
        'index.html',
        title='Home Page',
        rowlist = rowlist,
        len = len(rowlist),
        year=datetime.now().year,
    )

@app.route('/jsontest')
def jsontest():
    """Renders the home page."""
    return jsonify(jsondata)


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contact'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='About'
    )

@app.route('/merch')
def merch():
    """Renders the about page."""
    return render_template(
        'merch.html',
        title='Merch',
        year=datetime.now().year,
        message='Merchandise'
    )

@app.route('/checkout')
def checkout():
    """Renders the about page."""
    return render_template(
        'checkout.html',
        title='Checkout',
        year=datetime.now().year,
        message='Checkout'
    )

@app.route('/<string:song>')
def music(song):
    conn = sqlite3.connect("martinfeller.db")
    c = conn.cursor()
    # [str(song)] was used to prevent tuple supply issues, previous error was: incorrect number of bindings supplied.
    c.execute('SELECT * FROM songs WHERE songid=?', [str(song)])
    data = (c.fetchone())
    return render_template(
        'music.html',
        title='Music',
        songname = data[1],
        musiclogo =  data[2],
        spotifyembed =  data[3],
        youtubeembed =  data[4],
        year=datetime.now().year,
        message='Music',
        song_description = data[5]
    )