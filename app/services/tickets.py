from app.models.entities import Ticket
from app.models.enums import TicketStatus


class TicketService:
    def __init__(self):
        self._tickets: list[Ticket] = []
        self._next_id = 1

    def create(
        self,
        title: str,
        description: str,
        category: str,
        priority: str,
        requester_id: int,
    ) -> Ticket:
        """Create a new ticket."""

        ticket = Ticket(
            id=self._next_id,
            title=title,
            description=description,
            category=category,
            priority=priority,
            requester_id=requester_id,
        )

        self._tickets.append(ticket)
        self._next_id += 1

        return ticket

    def assign_technician(
        self,
        ticket_id: int,
        technician_id: int,
    ) -> Ticket:
        """Assign a technician to a ticket."""

        for ticket in self._tickets:
            if ticket.id == ticket_id:
                ticket.assignee_id = technician_id
                return ticket

        raise ValueError(f"Ticket with id {ticket_id} not found")

    def list_by_technician(
        self,
        technician_id: int,
    ) -> list[Ticket]:
        """Return tickets assigned to one technician."""

        return [
            ticket
            for ticket in self._tickets
            if ticket.assignee_id == technician_id
        ]

    def list_by_category(
        self,
        category: str,
    ) -> list[Ticket]:
        """Return tickets that belong to one category."""

        return [
            ticket
            for ticket in self._tickets
            if ticket.category == category
        ]

    def list_by_status(
        self,
        status: str | TicketStatus,
    ) -> list[Ticket]:
        """Return tickets with a specific status."""

        if isinstance(status, str):
            status = TicketStatus(status)

        return [
            ticket
            for ticket in self._tickets
            if ticket.status == status
        ]