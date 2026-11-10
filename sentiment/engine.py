"""Customer Support Sentiment & Churn Risk Engine for ERPNext."""

import re
from typing import Dict, Any, List
from pydantic import BaseModel


class SupportTicket(BaseModel):
    ticket_id: str
    customer_name: str
    subject: str
    message_body: str


class SentimentAnalysisResult(BaseModel):
    ticket_id: str
    sentiment_label: str  # Positive, Neutral, Negative, Frustrated
    sentiment_score: float  # -1.0 to +1.0
    churn_risk_level: str  # High, Medium, Low
    escalation_required: bool
    recommended_priority: str  # Urgent, High, Medium, Low


class TicketSentimentEngine:
    """Evaluates customer frustration keywords, urgency, and churn probability."""

    NEGATIVE_KEYWORDS = [
        "worst", "pathetic", "fraud", "unacceptable", "delay", "cancel my subscription",
        "refund", "terrible", "waste of money", "complaint", "legal notice", "horrible",
        "broken", "angry", "disappointed", "poor service",
    ]

    POSITIVE_KEYWORDS = [
        "great", "excellent", "thank you", "helpful", "awesome", "good job", "appreciate",
        "solved", "wonderful", "satisfied",
    ]

    def analyze_ticket(self, ticket: SupportTicket) -> SentimentAnalysisResult:
        full_text = f"{ticket.subject} {ticket.message_body}".lower()

        neg_matches = sum(1 for kw in self.NEGATIVE_KEYWORDS if re.search(r"\b" + re.escape(kw) + r"\b", full_text))
        pos_matches = sum(1 for kw in self.POSITIVE_KEYWORDS if re.search(r"\b" + re.escape(kw) + r"\b", full_text))

        # Calculate sentiment score (-1 to +1)
        net_diff = pos_matches - neg_matches
        score = max(-1.0, min(1.0, net_diff * 0.35))

        if neg_matches >= 2 or "cancel" in full_text or "refund" in full_text or "fraud" in full_text:
            sentiment = "Frustrated"
            churn_risk = "High"
            escalate = True
            priority = "Urgent"
        elif neg_matches == 1:
            sentiment = "Negative"
            churn_risk = "Medium"
            escalate = True
            priority = "High"
        elif pos_matches > 0:
            sentiment = "Positive"
            churn_risk = "Low"
            escalate = False
            priority = "Low"
        else:
            sentiment = "Neutral"
            churn_risk = "Low"
            escalate = False
            priority = "Medium"

        return SentimentAnalysisResult(
            ticket_id=ticket.ticket_id,
            sentiment_label=sentiment,
            sentiment_score=round(score, 2),
            churn_risk_level=churn_risk,
            escalation_required=escalate,
            recommended_priority=priority,
        )
