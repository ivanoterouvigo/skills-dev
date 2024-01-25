# -*- coding: utf-8 -*-

import logging
import ask_sdk_core.utils as ask_utils      # Import Alexa Skills Kit's classes
import ask_sdk_model as ..........
                                            # Other libraries could be imported.



class LaunchRequestHandler(AbstractRequestHandler):
    """
    Handler for Skill Launch. When the skill is firstly launched, the request type created is of LaunchRequest, and this is the handler for it.
    All implemented skills must have it.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
      
        # 
        speak_output = "Welcome, Hello World!!!!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# Create other implemented Handler classes, inheriting from AbstractRequestHandler.
# Typically, each one of them handles one single ossible response from the user.

# Create a custom Skill Builder object and add the handlers
sb = CustomSkillBuilder()

# Add all reques handlers created
sb.add_request_handler(LaunchRequestHandler())

# The default name in the Lambda console is lambda_function.lambda_handler
lambda_handler = sb.lambda_handler()
