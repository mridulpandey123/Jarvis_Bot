# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# from rasa_sdk import Tracker,FormValidationAction
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict

# class ValidateVidhansabhaForm(FormValidationAction):
#     def name(self) -> Text:
#          return "validate_vidhansabha_form"

#     def validate_vidhansabha(
#         self,
#         slot_value: Any, 
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#      ) ->Dict[Text,Any]:
         
#          print(f"Vidhansabha_name given={slot_value}")
#          if slot_value in [Bishnupur
# Khundrakpam (GEN)
# Heingang (GEN)
# Khurai (GEN)
# Kshetrigao
# Thongju
# Keirao
# Andro
# Lamlai
# Thangmeiband
# Uripok
# Sagolband
# Keishamthong
# Singjamei
# Yaiskul
# Wangkhei
# Sekmai
# Lamsang
# Konthoujam
# Patsoi
# Langthabal
# Naoriya pakhanglakpa
# Wangoi
# Mayang imphal
# Nambol
# Oinam
# Moirang
# Thanga
# Kumbi
# Lilong
# Thoubal
# Wangkhem
# Heirok
# Wangjing tentha','Khangabok','Wabgai','Kakching','Hiyanglam','Sugnu','Jiribam','Chandel','Tengnoupal','Phungyar','Ukhrul','Chingai','Saikul','Karong','Mao','Tadubi','Kangpokpi (Gen)','Saitu','Tamei','Tamenglong','Nungba','Tipaimukh','Thanlon','Henglep','Churachandpur','Saikot', 'Singhat']

#           dispatcher.utter_message(template="utter_askdateofbirth")

#           return [SlotSet('profession',tracker.latest_message['text'])]

# class ActionSubmit(Action):
#      def name(self)-> Text:
#           return "action_submit"
#      def run(self,dispatcher:CollectingDispatcher,tracker: )