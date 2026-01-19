from agents.base_agent import BaseAgent


class ConsensusEngineAgent(BaseAgent):
    def __init__(self):
        super().__init__("Consensus Engine Agent")

        self.weights = {
            "infra_score": 0.20,
            "policy_score": 0.15,
            "sentiment_score": 0.15,
            "momentum_score": 0.20,
            "rumor_score": 0.10,
            "risk_score": -0.20
        }

    def run(self, agent_outputs):
        final_scores = {}

        for outputs in agent_outputs.values():
            for entry in outputs:
                land_id = entry["land_id"]
                final_scores.setdefault(land_id, 0.0)

                for key, value in entry.items():
                    if key.endswith("_score"):
                        final_scores[land_id] += value * self.weights.get(key, 0)

        if not final_scores:
            self._trace = {"status": "no_scores"}
            return {}

        max_score = max(final_scores.values())
        min_score = min(final_scores.values())

        for land_id in final_scores:
            if max_score != min_score:
                final_scores[land_id] = round(
                    (final_scores[land_id] - min_score) / (max_score - min_score), 3
                )
            else:
                final_scores[land_id] = 0.5

        self._trace = final_scores
        return final_scores
