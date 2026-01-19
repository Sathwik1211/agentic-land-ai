from agents.base_agent import BaseAgent


class InfrastructureIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Infrastructure Intelligence Agent")

    def run(self, lands):
        results = []

        for land in lands:
            distance = land.get("distance_to_infra", 999)
            score = 0.7 if distance < 5 else 0.4

            results.append({
                "land_id": land["id"],
                "infra_score": score,
                "confidence": 0.6
            })

        self._trace = {"evaluated": len(results)}
        return results
