import logging


def before_scenario(context, scenario):
    logging.info("STARTED SCENARIO: {}".format(scenario.name))
