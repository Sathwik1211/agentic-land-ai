from agents.intent_agent import UserIntentAgent
from agents.eligibility_agent import LandEligibilityFilterAgent


class AgentController:
    """
    Central orchestrator (AI Principal).
    Controls the flow:
    User Intent → Eligibility Filtering → Downstream Agents
    """

    def __init__(self):
        self.intent_agent = UserIntentAgent()
        self.eligibility_agent = LandEligibilityFilterAgent()

    def run(self, user_input, lands):
        """
        Runs the initial pipeline:
        1. Interpret user intent
        2. Filter eligible lands
        """

        # Step 1: Understand user intent
        intent = self.intent_agent.run(user_input)

        # Step 2: Filter lands based on intent
        eligible_lands = self.eligibility_agent.run(lands, intent)

        return eligible_lands
