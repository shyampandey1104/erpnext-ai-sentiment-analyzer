"""Unit tests for TicketSentimentEngine."""

from sentiment.engine import TicketSentimentEngine, SupportTicket


def test_frustrated_ticket_escalation():
    engine = TicketSentimentEngine()
    ticket = SupportTicket(
        ticket_id="ISSUE-2026-909",
        customer_name="Acme Corp",
        subject="Unacceptable delay in shipment - terrible service",
        message_body="This is pathetic. We demand an immediate refund or we will cancel our contract.",
    )
    res = engine.analyze_ticket(ticket)
    assert res.sentiment_label == "Frustrated"
    assert res.churn_risk_level == "High"
    assert res.escalation_required is True
    assert res.recommended_priority == "Urgent"


def test_positive_ticket():
    engine = TicketSentimentEngine()
    ticket = SupportTicket(
        ticket_id="ISSUE-2026-910",
        customer_name="Happy Client",
        subject="Thank you for the quick resolution",
        message_body="Your team did an awesome job, very helpful and solved our problem.",
    )
    res = engine.analyze_ticket(ticket)
    assert res.sentiment_label == "Positive"
    assert res.escalation_required is False
