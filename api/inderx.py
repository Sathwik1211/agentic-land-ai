from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from orchestrator.controller import AgentController
from agents.infra_agent import InfrastructureIntelligenceAgent
from agents.policy_agent import PolicyGovernanceAgent
from agents.sentiment_agent import CulturalSentimentAgent
from agents.momentum_agent import MarketMomentumAgent
from agents.rumor_agent import SpeculationRumorAgent
from agents.risk_agent import VolatilityRiskAgent
from agents.consensus_agent import ConsensusEngineAgent
from agents.forecast_agent import ForecastingAgent
from agents.explainability_agent import ExplainabilityAgent


app = FastAPI(title="Agentic AI – Vacant Land Decision Intelligence")


class UserInput(BaseModel):
    budget: int
    risk: str
    years: int


class Land(BaseModel):
    id: int
    name: str
    price_per_sqft: int
    type: str
    distance_to_infra: int


class RequestPayload(BaseModel):
    user_input: UserInput
    lands: List[Land]

@app.get("/")
def home():
    return {
        "status": "OK",
        "message": "Agentic AI – Vacant Land Decision Intelligence is live on Vercel",
        "usage": {
            "endpoint": "/run",
            "method": "POST",
            "description": "Run Agentic AI pipeline"
        }
    }


@app.post("/run")
def run_agentic_ai(payload: RequestPayload):
    controller = AgentController()
    eligible_lands = controller.run(payload.user_input.dict(), [l.dict() for l in payload.lands])

    if not eligible_lands:
        return {
            "status": "no_results",
            "message": "No lands match the selected price per sqft."
        }

    infra = InfrastructureIntelligenceAgent()
    policy = PolicyGovernanceAgent()
    sentiment = CulturalSentimentAgent()
    momentum = MarketMomentumAgent()
    rumor = SpeculationRumorAgent()
    risk_agent = VolatilityRiskAgent()

    agent_outputs = {
        "infra": infra.run(eligible_lands),
        "policy": policy.run(eligible_lands),
        "sentiment": sentiment.run(eligible_lands),
        "momentum": momentum.run(eligible_lands),
        "rumor": rumor.run(eligible_lands),
        "risk": risk_agent.run(eligible_lands),
    }

    consensus = ConsensusEngineAgent()
    final_scores = consensus.run(agent_outputs)

    forecast_agent = ForecastingAgent()
    forecasts = forecast_agent.run(final_scores, eligible_lands, payload.user_input.years)

    explainability = ExplainabilityAgent()
    explanations = explainability.run(
        eligible_lands,
        agent_outputs,
        final_scores,
        forecasts
    )

    return {
        "eligible_lands": eligible_lands,
        "final_scores": final_scores,
        "forecasts": forecasts,
        "explanations": explanations
    }
