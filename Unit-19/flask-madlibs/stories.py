"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story_2 = Story(
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
When I got home I {verb, past tense} my
mom for a{adjective} day at the zoo. """
)

story_3 = Story(
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
