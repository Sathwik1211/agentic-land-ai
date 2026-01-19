from agents.base_agent import BaseAgent


class PolicyGovernanceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Policy & Governance Agent")

    def run(self, lands):
        results = []

        for land in lands:
            price = land.get("price_per_sqft")
            if price is None:
                continue

            score = 0.6 if price < 8000 else 0.4

            results.append({
                "land_id": land["id"],
                "policy_score": score,
                "confidence": 0.5
            })

        self._trace = {"evaluated": len(results)}
        return results
