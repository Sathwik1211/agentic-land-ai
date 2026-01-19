from agents.intent_agent import UserIntentAgent
from agents.eligibility_agent import LandEligibilityFilterAgent

class AgentController:
    def __init__(self):
        self.intent_agent = UserIntentAgent()
        self.eligibility_agent = LandEligibilityFilterAgent()

    def run(self, user_input, lands):
        intent = self.intent_agent.run(user_input)
        eligible_lands = self.eligibility_agent.run(lands, intent)
        return eligible_lands
