from agents.base_agent import BaseAgent


class VolatilityRiskAgent(BaseAgent):
    def __init__(self):
        super().__init__("Volatility & Risk Agent")

    def run(self, lands):
        results = []

        for land in lands:
            price = land.get("price_per_sqft")
            if price is None:
                continue

            risk = 0.2 if price < 7500 else 0.5

            results.append({
                "land_id": land["id"],
                "risk_score": risk,
                "confidence": 0.8
            })

        self._trace = {"evaluated": len(results)}
        return results
