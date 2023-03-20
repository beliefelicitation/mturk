from otree.api import *
import json, numpy
c = Currency  # old name for currency; you can delete this.


doc = """
Elicitation belief app
"""


class Constants(BaseConstants):
    name_in_url = 'distribution'
    players_per_group = None
    num_rounds = 24
    instructions_template = 'distribution/instructions.html'
    data = {'71': [0.035, 0.125, 0.215, 0.25, 0.215, 0.125, 0.035], '72': [0.034, 0.075, 0.115, 0.201, 0.286, 0.238, 0.051], '73': [0.05, 0.196, 0.109, 0.023, 0.198, 0.374, 0.05], '74': [0.043, 0.184, 0.061, 0.027, 0.391, 0.251, 0.043], '151': [0.015, 0.018, 0.022, 0.04, 0.06, 0.105, 0.155, 0.17, 0.155, 0.105, 0.06, 0.04, 0.022, 0.018, 0.015], '152': [0.011, 0.016, 0.021, 0.027, 0.032, 0.046, 0.06, 0.087, 0.115, 0.142, 0.16, 0.143, 0.077, 0.047, 0.016], '153': [0.019, 0.069, 0.12, 0.093, 0.067, 0.04, 0.03, 0.02, 0.01, 0.041, 0.073, 0.105, 0.19, 0.105, 0.018], '154': [0.017, 0.068, 0.119, 0.038, 0.059, 0.081, 0.102, 0.007, 0.023, 0.04, 0.095, 0.13, 0.165, 0.039, 0.017], '301': [0.002, 0.004, 0.006, 0.008, 0.01, 0.015, 0.02, 0.023, 0.035, 0.042, 0.05, 0.061, 0.07, 0.077, 0.0815, 0.0815, 0.077, 0.07, 0.061, 0.05, 0.042, 0.035, 0.023, 0.02, 0.015, 0.01, 0.008, 0.006, 0.004, 0.002], '302': [0.004, 0.006, 0.007, 0.008, 0.009, 0.01, 0.011, 0.012, 0.013, 0.014, 0.015, 0.018, 0.022, 0.025, 0.028, 0.031, 0.043, 0.054, 0.065, 0.077, 0.086, 0.095, 0.086, 0.077, 0.062, 0.046, 0.03, 0.023, 0.015, 0.008], '303': [0.005, 0.017, 0.03, 0.062, 0.093, 0.081, 0.069, 0.057, 0.048, 0.039, 0.03, 0.021, 0.018, 0.014, 0.011, 0.008, 0.005, 0.002, 0.01, 0.02, 0.028, 0.036, 0.045, 0.053, 0.062, 0.05, 0.039, 0.027, 0.016, 0.004], '304': [0.003, 0.012, 0.021, 0.03, 0.039, 0.027, 0.015, 0.034, 0.054, 0.044, 0.033, 0.023, 0.013, 0.003, 0.007, 0.01, 0.014, 0.018, 0.022, 0.072, 0.122, 0.089, 0.056, 0.023, 0.044, 0.065, 0.05, 0.034, 0.019, 0.004], '71b': [0.035, 0.125, 0.215, 0.25, 0.215, 0.125, 0.035], '72b': [0.051, 0.238, 0.286, 0.201, 0.115, 0.075, 0.034], '73b': [0.05, 0.374, 0.198, 0.023, 0.109, 0.196, 0.05], '74b': [0.043, 0.251, 0.391, 0.027, 0.061, 0.184, 0.043], '151b': [0.015, 0.018, 0.022, 0.04, 0.06, 0.105, 0.155, 0.17, 0.155, 0.105, 0.06, 0.04, 0.022, 0.018, 0.015], '152b': [0.016, 0.047, 0.077, 0.143, 0.16, 0.142, 0.115, 0.087, 0.06, 0.046, 0.032, 0.027, 0.021, 0.016, 0.011], '153b': [0.018, 0.105, 0.19, 0.105, 0.073, 0.041, 0.01, 0.02, 0.03, 0.04, 0.067, 0.093, 0.12, 0.069, 0.019], '154b': [0.017, 0.040, 0.165, 0.13, 0.095, 0.04, 0.023, 0.007, 0.102, 0.081, 0.059, 0.038, 0.119, 0.068, 0.017], '301b': [0.002, 0.004, 0.006, 0.008, 0.01, 0.015, 0.02, 0.023, 0.035, 0.042, 0.05, 0.061, 0.07, 0.077, 0.082, 0.082, 0.077, 0.07, 0.061, 0.05, 0.042, 0.035, 0.023, 0.02, 0.015, 0.01, 0.008, 0.006, 0.004, 0.002], '302b': [0.008, 0.015, 0.023, 0.03, 0.046, 0.062, 0.077, 0.086, 0.095, 0.086, 0.077, 0.065, 0.054, 0.043, 0.031, 0.028, 0.025, 0.022, 0.018, 0.015, 0.014, 0.013, 0.012, 0.011, 0.01, 0.009, 0.008, 0.007, 0.006, 0.004], '303b': [0.005, 0.016, 0.027, 0.039, 0.05, 0.062, 0.053, 0.045, 0.036, 0.028, 0.02, 0.01, 0.002, 0.005, 0.008, 0.011, 0.014, 0.018, 0.021, 0.03, 0.039, 0.048, 0.057, 0.069, 0.081, 0.093, 0.062, 0.03, 0.017, 0.004], '304b': [0.004, 0.019, 0.034, 0.05, 0.065, 0.044, 0.023, 0.056, 0.089, 0.122, 0.072, 0.022, 0.018, 0.014, 0.01, 0.007, 0.003, 0.013, 0.023, 0.033, 0.044, 0.054, 0.034, 0.015, 0.027, 0.039, 0.03, 0.021, 0.012, 0.003]}
    sequence = ['71', '72', '73', '74', '151', '152', '153', '154', '301', '302', '303', '304', '71b', '72b', '73b',
                '74b', '151b', '152b', '153b', '154b', '301b', '302b', '303b', '304b']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    model_data = models.StringField()
    data = models.StringField()
    history = models.LongStringField(initial="[]")
    score = models.FloatField(blank=True, initial=0)


# PAGES


class Distributions(Page):

    form_model = 'player'
    form_fields = []

    timer_text = 'Time left before next screen:'

    @staticmethod
    def get_timeout_seconds(player):
        if player.session.config["timeout"]:
            if player.round_number <= 12:
                return player.session.config["phase1_timout"]
            else:
                return player.session.config["phase2_timout"]

    @staticmethod
    def live_method(player, data):
        score = round(1-sum(numpy.absolute(numpy.subtract(data["history"]["data"], json.loads(player.model_data)))),2)
        if score < 0:
            score = 0
        historyscore = data["history"]
        historyscore['score'] = score
        player.score = score
        history = json.loads(player.history)
        history.append(historyscore)
        player.history = json.dumps(history)
        player.data = json.dumps(data["history"]["data"])

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.payoff = player.score*player.session.config['screen_payoff']
        if player.round_number == 1:
            player.participant.vars["round_payoff"] = json.dumps([{"score":100*player.score,"payoff":float(player.payoff)}])
        else:
            round_payoff = json.loads(player.participant.vars["round_payoff"])
            round_payoff.append({"score":100*player.score,"payoff":float(player.payoff)})
            player.participant.vars["round_payoff"] = json.dumps(round_payoff)
#        if timeout_happened:
#            player.timeout = True

    @staticmethod
    def js_vars(player):
        player.model_data = str(Constants.data[Constants.sequence[((player.round_number - 1) % (len(Constants.data)))]])
        if player.session.config["beta"]:
            interface = player.session.config["interface_sequence"][
                            int((player.round_number - 1) / len(Constants.data))],
        else:
            interface = player.participant.interface,

        return dict(
            model_data=player.model_data,
            interface=interface,
            min_timeout=45,
            screen_payoff = player.session.config['screen_payoff']
        )

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            interface=player.participant.interface,
            validate_btn=False,
            screen_number = (player.round_number - 1) % (int(len(Constants.data)/2)) + 1
        )

class Intro_Distribution(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1 or player.round_number == 13


page_sequence = [Intro_Distribution, Distributions]
