from agents.base_agent import BaseAgent


class UserIntentAgent(BaseAgent):
    def __init__(self):
        super().__init__("User Intent Agent")

    def run(self, user_input):
        intent = {
            "budget": user_input.get("budget"),
            "risk": user_input.get("risk", "medium"),
            "years": user_input.get("years", 5)
        }
        self._trace = intent
        return intent
