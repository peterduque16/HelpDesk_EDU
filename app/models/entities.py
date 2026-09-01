from dataclasses import dataclass
from typing import Optional

from app.models.enums import TicketStatus


@dataclass
class Ticket:
    id: int
    title: str
    description: str
    category: str
    priority: str
    requester_id: int
    assignee_id: Optional[int] = None
    status: TicketStatus = TicketStatus.OPEN