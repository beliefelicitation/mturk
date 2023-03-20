from otree.api import *
import json, numpy
c = Currency  # old name for currency; you can delete this.


doc = """
Elicitation belief app
"""


class Constants(BaseConstants):
    name_in_url = 'prediction'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    data = models.StringField()
    history = models.LongStringField(initial="[]")

# PAGES


class Prediction(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Distributions(Page):

    form_model = 'player'
    form_fields = []

    timer_text = 'Time left to make your prediction:'

    @staticmethod
    def get_timeout_seconds(player):
        if player.session.config["timeout"]:
            return 90

    @staticmethod
    def live_method(player, data):
        history = json.loads(player.history)
        history.append(data["history"])
        player.history = json.dumps(history)
        player.data = json.dumps(data["history"]["data"])

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass
#        if timeout_happened:
#            player.timeout = True


    @staticmethod
    def js_vars(player):
        return dict(
            interface = player.participant.interface,
            prediction = True,
            yMax = 1,
            min = player.session.config["prediction_questions"][player.round_number-1]["min"],
            step = player.session.config["prediction_questions"][player.round_number-1]["step"],
            nb_bins = player.session.config["prediction_questions"][player.round_number-1]["nb_bins"],
            xUnit = player.session.config["prediction_questions"][player.round_number-1]["unit"],
            min_timeout=30,
        )

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            prediction_questions = player.session.config["prediction_questions"][player.round_number-1]["q"],
            interface=player.participant.interface,
        )

page_sequence = [Prediction, Distributions]
