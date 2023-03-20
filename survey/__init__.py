from otree.api import *
c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=18, max=100)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    easy = models.IntegerField(
        label="On a scale from 1 to 7, did you find the interface easy or difficult to use?",
        choices=[
            [1, '1 (Easy)'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7 (Very difficult)']
        ],
        widget=widgets.RadioSelect,
    )
    frustrating = models.IntegerField(
        label="On a scale from 1 to 7, was the interface frustrating to use?",
        choices=[
            [1, '1 (Not frustrating)'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7 (Very frustrating)']
        ],
        widget=widgets.RadioSelect,
    )
    understood = models.IntegerField(
        label="On a scale from 1 to 7, did you feel that you understood the interface: immediately, after a while, never?",
        choices=[
            [1, '1 (Immediately)'],
            [2, '2'],
            [3, '3'],
            [4, '4 (After a while)'],
            [5, '5'],
            [6, '6'],
            [7, '7 (Never)']
        ],
        widget=widgets.RadioSelect,
    )
    commentary = models.LongStringField(
        label="Do you have any commentary ? (bug / complaints / comments)",
        blank=True
    )
    keyboard = models.BooleanField(
        label="Did you use a keyboard?",
    )
    mouse = models.BooleanField(
        label="Did you use a mouse?",
    )
    touchpad = models.BooleanField(
        label="Did you use a touchpad?",
    )
    touchscreen = models.BooleanField(
        label="Did you use a touchscreen?",
    )


# FUNCTIONS
# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','easy','frustrating','understood','keyboard','mouse','touchpad','touchscreen','commentary']

page_sequence = [Survey]
