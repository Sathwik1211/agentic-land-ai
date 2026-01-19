from agents.base_agent import BaseAgent


class MarketMomentumAgent(BaseAgent):
    def __init__(self):
        super().__init__("Market Momentum Agent")

    def run(self, lands):
        results = []

        for land in lands:
            distance = land.get("distance_to_infra", 999)
            momentum = 0.8 if distance < 5 else 0.4

            results.append({
                "land_id": land["id"],
                "momentum_score": momentum,
                "confidence": 0.6
            })

        self._trace = {"evaluated": len(results)}
        return results
