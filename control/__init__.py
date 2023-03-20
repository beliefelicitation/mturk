from otree.api import *
c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = 'control'
    players_per_group = None
    num_rounds = 3
    bonus_label = "How much is the fixed participation fee (HIT reward)?"
    earning_label = "How much (bonus) can you earn on each of the 24 screens?"
    #all_screen_label = "Will all screens be paid?"
    score_label = "The more your bar-graph matches the target picture, the lower your score:"
    interaction_label = "How do you adjust the bar-graph?"
    interaction_choice = {
            "ours": 'by adding and moving anchor points',
            "bins": 'by dragging each individual bar up or down',
            "number": 'by inputting the height of the bar in a text field',
            "metaculus": 'by moving the horizontal slider below the graph'
    }


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if 'interface' in subsession.session.config:
        for player in subsession.get_players():
            player.interface = subsession.session.config["interface"]
            player.participant.interface = player.interface
    else:
        import itertools
        interfaces = itertools.cycle(["ours", "number","bins","metaculus"])
        for player in subsession.get_players():
            player.interface = next(interfaces)
            player.participant.interface = player.interface

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    failed = models.BooleanField()

    timeout = models.BooleanField()

    interface = models.StringField()

    bonus = models.FloatField(
        label= Constants.bonus_label,
        choices=[[0.1,cu(0.1)], [0.2,cu(0.2)], [0.5,cu(0.5)], [1,cu(1)]]
    )
    earning = models.FloatField(
        label= Constants.earning_label,
        choices=[[0.1,cu(0.1)], [0.2,cu(0.2)], [0.5,cu(0.5)], [1,cu(1)]]
    )
    #all_screen = models.BooleanField(
    #    label= Constants.all_screen_label,
    #)
    score = models.BooleanField(
        label=Constants.score_label,
        choices=[
            [1, "True"],
            [0, "False"]
        ]
    )
    interaction = models.StringField(
        label= Constants.interaction_label,
        choices= [
            ["ours",Constants.interaction_choice["ours"]],
            ["bins",Constants.interaction_choice["bins"]],
            ["number", Constants.interaction_choice["number"]],
            ["metaculus", Constants.interaction_choice["metaculus"]],
        ]
    )


    device = models.StringField()
    os = models.StringField()


# FUNCTIONS
# PAGES
class Playground(Page):
    timer_text = 'Time left to familiarize yourself (you can not validate before 45s):'

    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def get_timeout_seconds(player):
        if player.session.config["timeout"]:
            return 90

    @staticmethod
    def js_vars(player):
        model_data = "[0, 0.092, 0.104, 0.116, 0.129, 0.141, 0.132, 0.123, 0.114, 0.049]"

        return dict(
            model_data = model_data,
            interface = player.participant.interface,
            min_timeout = 45,
            playground=True,
            screen_payoff=player.session.config['screen_payoff']
        )

    def vars_for_template(player: Player):
        return dict(
            interface=player.participant.interface,
            validate_btn=True,
        )


class Survey(Page):
    form_model = 'player'
    form_fields = ["bonus","earning","score","interaction"]

    @staticmethod
    def app_after_this_page(player, upcoming_apps):

        if player.timeout is False and float(player.bonus) == float(player.session.config["participation_fee"]) \
                and float(player.earning) == float(player.session.config["screen_payoff"]) \
                and player.score is False \
                and player.interaction == player.participant.interface:
            player.participant.kickout = False
            player.failed = False
            return upcoming_apps[0]
        else:
            player.failed = True
            if player.round_number == Constants.num_rounds or player.timeout:
                player.participant.kickout = True
                return upcoming_apps[-1]

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.timeout = True
            player.bonus = None
            player.earning = None
            #player.all_screen = None
            player.score = None
        else:
            player.timeout = False

    timer_text = 'Time left to answer the following questions:'

    @staticmethod
    def get_timeout_seconds(player):
        return 120

    @staticmethod
    def live_method(player, data):
        player.device = data["device"]
        player.os = data["os"]


class Answers(Page):

    def vars_for_template(player: Player):

        return dict(
            interaction = Constants.interaction_choice[player.interaction],
            interface = Constants.interaction_choice[player.participant.interface],
            number_of_trials = Constants.num_rounds - 1
        )

class Introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Task(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Payment(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Procedures(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Confidentiality(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Intro_Playground(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
page_sequence = [Introduction, Procedures, Confidentiality, Payment, Task, Intro_Playground,Playground, Survey, Answers]
