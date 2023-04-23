from os import environ


SESSION_CONFIGS = [
    dict(
        name='mturk',
        display_name="Mturk",
        app_sequence=['control', 'distribution', 'prediction', 'survey', 'payment_info'],
        beta=False,
        timeout=True,
        num_demo_participants=1,
    ),
    dict(
        name='elicitation_belief_our_timeout',
        display_name="Our Interface",
        app_sequence=['control','distribution', 'prediction', 'survey', 'payment_info'],
        beta=False,
        interface="ours",
        timeout=True,
        num_demo_participants=1,
    ),
    dict(
        name='elicitation_belief_number_timeout',
        display_name="Number-input interface",
        app_sequence=['control','distribution', 'prediction', 'survey', 'payment_info'],
        beta=False,
        interface="number",
        timeout=True,
        num_demo_participants=1,
    ),
    dict(
        name='elicitation_belief_slider_not_norm_timeout',
        display_name="Slider-input interface",
        app_sequence=['control','distribution', 'prediction', 'survey', 'payment_info'],
        beta=False,
        interface="bins",
        timeout=True,
        num_demo_participants=1,
    ),
    dict(
        name='elicitation_belief_metaculus_timeout',
        display_name="The metaculus normal distribution",
        app_sequence=['control','distribution', 'prediction', 'survey', 'payment_info'],
        beta=False,
        interface="metaculus",
        timeout=True,
        num_demo_participants=1,
    ),
    dict(
        name='elicitation_belief_our',
        display_name="Our Interface (Without timeout)",
        app_sequence=['control','distribution', 'prediction', 'survey', 'payment_info'],
        beta=False,
        interface="ours",
        timeout=False,
        num_demo_participants=1,
    ),
    dict(
        name='elicitation_belief_number',
        display_name="Number-input interface  (Without timeout)",
        app_sequence=['control','distribution', 'prediction', 'survey', 'payment_info'],
        beta=False,
        interface="number",
        timeout=False,
        num_demo_participants=1,
    ),
    dict(
        name='elicitation_belief_slider_not_norm',
        display_name="Slider-input interface  (Without timeout)",
        app_sequence=['control','distribution', 'prediction', 'survey', 'payment_info'],
        beta=False,
        interface="bins",
        timeout=False,
        num_demo_participants=1,
    ),
    dict(
        name='elicitation_belief_metaculus',
        display_name="The metaculus normal distribution  (Without timeout)",
        app_sequence=['control','distribution', 'prediction', 'survey', 'payment_info'],
        interface="metaculus",
        timeout=False,
        beta=False,
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
PARTICIPANT_FIELDS = ["kickout","round_payoff","interface"]

SESSION_CONFIG_DEFAULTS = dict(
    mturk_hit_settings=dict(
        keywords='bonus, study',
        title='Match-the-plot (20 cent for each perfectly matched plot)',
        description='Your task is to recreate a figure with a bar-graph in it. You will receive up to 20 cent per bar-graph depending on how close the shape of your created bar-graph is to the target. You will face 24 graph-matching task, for earnings up to 4.8 USD',
        frame_height=900,
        template='global/mturk_template.html',
        minutes_allotted_per_assignment=60,
        expiration_hours= 24,
        grant_qualification_id=environ.get('GRANT_QUALIFICATION_ID'),  # to prevent retakes
        qualification_requirements=[
            #No-retakers
            {
                'QualificationTypeId': environ.get('GRANT_QUALIFICATION_ID'),
                'Comparator': "DoesNotExist",
            },
            # Only US
            {
                'QualificationTypeId': "00000000000000000071",
                'Comparator': "EqualTo",
                'LocaleValues': [{'Country': "US"}]
            },
            # Minimum 500 HITs approved
            {
                'QualificationTypeId': "00000000000000000040",
                'Comparator': "GreaterThanOrEqualTo",
                'IntegerValues': [500]
            },
            # Minimum 95% HITs approved
            {
                'QualificationTypeId': "000000000000000000L0",
                'Comparator': "GreaterThanOrEqualTo",
                'IntegerValues': [95]
            },
        ],
        ),
    real_world_currency_per_point=1.00, participation_fee=0.5, prediction_questions=[{"q": "What will be the temperature (°F) in New York City at noon on the 4th of July, 2022?",
                                                                                      "min":60,
                                                                                     "step":2,
                                                                                     "nb_bins":31,
                                                                                     "unit":"°"},
                                                                                     {
                                                                                     "q": "20 years from now, what will be the temperature (°F) in New York City at noon on the 4th of July, 2042?",
                                                                                     "min": 60,
                                                                                     "step": 2,
                                                                                     "nb_bins": 31,
                                                                                     "unit":"°"}],
    screen_payoff=0.2, phase1_timout=45, phase2_timout=15, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')



DEMO_PAGE_INTRO_HTML = """
Here are all the treatments available
"""


SECRET_KEY = environ.get('OTREE_SECRET_KEY') or 'kbohidoecdoatukacaanqthanapanhanan'

INSTALLED_APPS = ['otree']
