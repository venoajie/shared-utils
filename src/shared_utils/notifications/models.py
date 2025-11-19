# src/shared/notifications/models.py

from pydantic import BaseModel


class TradeNotification(BaseModel):
    """A structured model for a trade notification."""

    direction: str
    amount: float
    instrument_name: str
    price: float


class SystemAlert(BaseModel):
    """A structured model for a system-level alert."""

    component: str
    event: str
    details: str
    # severity defaulting to CRITICAL.
    # Options can be INFO, WARNING, CRITICAL.
    severity: str = "CRITICAL"
