from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)


class Story:
    def __init__(self, words, text):
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Given a dictionary of answers, generate the story"""
        text = self.template
        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)
        return text
    
prebuilt_stories = {
        "I like....": Story(["noun", "verb"], "I love to {verb} a good {noun}."),
        "Once upon a time": Story(
            ["place", "noun", "verb", "adjective", "plural_noun"],
            """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
        ),
        "A day at the zoo": Story(
            ['adjective', 'noun', 'verb_past_tense', 'adjective', 'noun', 'noun', 'adjective', 'verb', 'adverb', 'verb_past_tense', 'adjective'], """Today I went to the zoo. I saw a(n)
            {adjective}
            {noun} jumping up and down in its tree.
            He {verb_past_tense} {adverb}
            through the large tunnel that led to its{adjective}
            {noun}. I got some peanuts and passed
            them through the cage to a gigantic gray {noun}
            towering above my head. Feeding that animal made
            me hungry. I went to get a {adjective} scoop
            of ice cream. It filled my stomach. Afterwards I had to
            {verb} {adverb} to catch our bus.
            When I got home I {verb_past_tense} my
            mom for a{adjective} day at the zoo. """
        ),
        "In the jungle": Story(
            ['adjective', 'adjective', 'adjective', 'noun', 'adjective', 'adjective', 'noun', 'verb', 'verb', 'adjective', 'noun', 'verb', 'noun', 'verb', 'adjective'], """I walk through the color jungle. I take out my
            {adjective} canteen. There's a
            {adjective} parrot with a {adjective}
            {noun} in his mouth right there in front
            of me in the {adjective} trees! I gaze at his
            {adjective} {noun}. A sudden
            sound awakes me from my daydream! A panther’s
            {verb} in front of my head! I
            {verb} his {adjective}
            breath. I remember I have a packet of {noun}
            that makes go into a deep slumber! I
            {verb}it away from me in front of the
            {noun}.Yes he's eating it! I
            {verb} away through the
            {adjective} jungle. I meet my parents at the
            tent. Phew! It’s been an exciting day in the jungle."""
                    )
    }


@app.route('/')
def index():
    """Show homepage"""
    return render_template('index.html')


@app.route('/create_your_own')
def create_your_own():
    """Show form for user to create their own story"""
    return render_template('create_your_own.html')


@app.route('/choose_prebuilt')
def choose_prebuilt():
    """Show page with dropdown to prebuilt stories"""
    return render_template('choose_prebuilt.html', prebuilt_stories=prebuilt_stories)


@app.route('/create_story', methods=['POST'])
def create_story():
    """Create story from form input and show story"""
    story_template = request.form['story_template']
    placeholders = re.findall(r'\{(\w+)\}', story_template)
    return render_template('form.html', placeholders=placeholders, story_template=story_template, user_created=True)



@app.route('/create_prebuilt_story', methods=['POST'])
def create_prebuilt_story():
    """Create story from prebuilt story and show story"""
    story_id = request.form['prebuilt_story']
    story = prebuilt_stories[story_id]
    return render_template('form.html', placeholders=story.prompts, story_template=story.template, user_created=False)


@app.route('/show_story', methods=['POST'])
def show_story():
    """Show story"""
    story_template = request.form['story_template']
    placeholders = re.findall(r'\{(\w+)\}', story_template)
    answers = {placeholder: request.form[placeholder].lower()
               for placeholder in placeholders}
    story = Story(placeholders, story_template)
    generated_story = story.generate(answers)
    user_created = request.form.get('user_created') == 'True'
    return render_template('story.html', story=generated_story, user_created=user_created)



