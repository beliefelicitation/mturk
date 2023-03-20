from otree.api import *
import json
c = Currency  # old name for currency; you can delete this.


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    completed = models.BooleanField(initial=False)

# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.completed = True
        if participant.kickout:
            participant.payoff = - player.session.config["participation_fee"]
            return dict(
                redemption_code=participant.label or participant.code,
            )
        else:
            return dict(
                round_payoff=json.loads(participant.round_payoff),
                redemption_code=participant.label or participant.code
            )


page_sequence = [PaymentInfo]
