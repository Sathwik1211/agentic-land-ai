from agents.base_agent import BaseAgent


class CulturalSentimentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Cultural Sentiment Agent")

    def run(self, lands):
        results = []

        for land in lands:
            sentiment = 0.7 if land["id"] % 2 == 1 else 0.5

            results.append({
                "land_id": land["id"],
                "sentiment_score": sentiment,
                "confidence": 0.5
            })

        self._trace = {"evaluated": len(results)}
        return results
