import asyncio
import logging
import json
import numpy as np
import datetime

from dateutil.relativedelta import relativedelta
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
    Restarted
)
logger = logging.getLogger(__name__)


class ActionSetSlotsAfterNER(Action):

    def name(self) -> Text:
        return "action_set_slots_after_ner"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        intent_action = next(tracker.get_latest_entity_values("intent_action"), None)
        subject = next(tracker.get_latest_entity_values("subject"), None)
        events = []
        if intent_action:
            events.append(SlotSet("slot_intent_action", intent_action))
        if subject:
            events.append(SlotSet("slot_subject", subject))
        events.append(FollowupAction("check_form"))
        return events


class CheckForm(FormAction):

    def name(self) -> Text:
        return "check_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["slot_intent_action",
                "slot_subject",
                "slot_name"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"slot_intent_action": [self.from_text()],
                "slot_subject": [self.from_text()],
                "slot_name": [self.from_text()]}

    def custom_request_next_slot(self, dispatcher, tracker, domain) -> Optional[List[EventType]]:

        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):

                if slot == "slot_intent_action":
                    text = f"Вы хотите записаться или отменить запись?"
                    buttons = [{"title": "Записаться", "payload": 'Записаться'},
                               {"title": "Отменить запись", "payload": 'Отменить запись'}]
                    dispatcher.utter_message(text=text, buttons=buttons)
                    return [SlotSet(REQUESTED_SLOT, slot)]
                if slot == "slot_subject":
                    text = f"Какой предмет интересует?"
                    buttons = [{"title": "Math", "payload": 'Math'},
                               {"title": "Physics", "payload": 'Physics'},
                               {"title": "IT", "payload": 'IT'}]
                    dispatcher.utter_message(text=text, buttons=buttons)
                    return [SlotSet(REQUESTED_SLOT, slot)]
                if slot == "slot_name":
                    text = f"Укажите имя студента:"
                    dispatcher.utter_message(text=text)
                    return [SlotSet(REQUESTED_SLOT, slot)]
        return None

    def request_next_slot(self, dispatcher, tracker, domain) -> Optional[List[EventType]]:
        return self.custom_request_next_slot(dispatcher, tracker, domain)

    def validate_slot_intent_action(self, value, dispatcher, tracker, domain):
        if value in ["Записаться", "Отменить запись"]:
            return {"slot_intent_action": value}
        else:
            text_init = "Выберите значение с помощью кнопок!"
            buttons = [{"title": "Записаться", "payload": 'Записаться'},
                       {"title": "Отменить запись", "payload": 'Отменить запись'}]
            dispatcher.utter_message(text=text_init, buttons=buttons)
            return {"slot_intent_action": None}

    def validate_slot_subject(self, value, dispatcher, tracker, domain):
        if value in ["Math", "Physics", "IT"]:
            return {"slot_subject": value}
        else:
            text_init = "Выберите значение с помощью кнопок!"
            buttons = [{"title": "Math", "payload": 'Math'},
                       {"title": "Physics", "payload": 'Physics'},
                       {"title": "IT", "payload": 'IT'}]
            dispatcher.utter_message(text=text_init, buttons=buttons)
            return {"slot_subject": None}

    async def submit(self, dispatcher, tracker, domain) -> List[Dict]:
        return [FollowupAction("action_get_table")]


class ActionGetTable(Action):

    def name(self) -> Text:
        return "action_get_table"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        dispatcher.utter_message(text="Ок")
        return [Restarted()]
