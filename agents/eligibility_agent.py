from agents.base_agent import BaseAgent


class LandEligibilityFilterAgent(BaseAgent):
    def __init__(self):
        super().__init__("Land Eligibility Filter Agent")

    def run(self, lands, intent):
        eligible_lands = []

        for land in lands:
            price = land.get("price_per_sqft")
            if price is None:
                continue

            if price <= intent["budget"] and land.get("type") == "vacant":
                eligible_lands.append(land)

        self._trace = {
            "total_lands": len(lands),
            "eligible_lands": len(eligible_lands),
            "budget_price_per_sqft": intent["budget"]
        }
        return eligible_lands
