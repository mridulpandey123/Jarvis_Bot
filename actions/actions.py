# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
class ActionHelloWorld(FormAction):

     def name(self) -> Text:
         return "designation_form"

     def name(self) -> Text:
         return "realname_form"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
         print("required_slots(tracker: Tracker)")
         return ["realname"]


     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
         print("required_slots(tracker: Tracker)")
         return ["designation"]


     def submit(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict]:

         dispatcher.utter_message(template="utter_submit")#
         return []
