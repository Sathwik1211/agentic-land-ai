from agents.base_agent import BaseAgent


class SpeculationRumorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Speculation & Rumor Agent")

    def run(self, lands):
        results = []

        for land in lands:
            rumor = 0.6 if land["id"] == 1 else 0.3

            results.append({
                "land_id": land["id"],
                "rumor_score": rumor,
                "confidence": 0.4
            })

        self._trace = {"evaluated": len(results)}
        return results
