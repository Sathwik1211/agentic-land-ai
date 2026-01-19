from agents.base_agent import BaseAgent


class ForecastingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Forecasting Agent")

    def run(self, final_scores, lands, years=5):
        forecasts = {}

        for land_id, score in final_scores.items():
            base_price = next(l["price_per_sqft"] for l in lands if l["id"] == land_id)
            yearly = {}
            current = base_price

            for year in range(1, years + 1):
                growth_rate = score * 0.10
                current = round(current * (1 + growth_rate), 2)
                yearly[f"Year {year}"] = current

            forecasts[land_id] = yearly

        self._trace = forecasts
        return forecasts
