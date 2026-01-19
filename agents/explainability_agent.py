from agents.base_agent import BaseAgent


class ExplainabilityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Explainability Agent")

    def run(self, eligible_lands, agent_outputs, final_scores, forecasts):
        explanations = {}

        for land in eligible_lands:
            land_id = land["id"]
            reasons = []

            if next(x for x in agent_outputs["infra"] if x["land_id"] == land_id)["infra_score"] > 0.6:
                reasons.append("Strong future infrastructure support")

            if next(x for x in agent_outputs["policy"] if x["land_id"] == land_id)["policy_score"] > 0.5:
                reasons.append("Favorable policy and governance conditions")

            if next(x for x in agent_outputs["sentiment"] if x["land_id"] == land_id)["sentiment_score"] > 0.6:
                reasons.append("Positive local and cultural sentiment")

            if next(x for x in agent_outputs["momentum"] if x["land_id"] == land_id)["momentum_score"] > 0.6:
                reasons.append("Strong market momentum")

            if next(x for x in agent_outputs["risk"] if x["land_id"] == land_id)["risk_score"] > 0.4:
                reasons.append("Higher volatility and risk detected")

            forecast = forecasts[land_id]
            years = list(forecast.keys())

            forecast_description = [
                f"Conservative outlook: around ₹{forecast[years[0]]} per sqft in {years[0]}",
                f"Expected growth: around ₹{forecast[years[len(years)//2]]} per sqft mid-term",
                f"Optimistic outlook: up to ₹{forecast[years[-1]]} per sqft by end of period"
            ]

            explanations[land_id] = {
                "final_score": final_scores[land_id],
                "forecast_description": forecast_description,
                "key_reasons": reasons if reasons else ["Balanced opportunity with moderate signals"]
            }

        self._trace = explanations
        return explanations
