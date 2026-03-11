tickets = []

def create_ticket(msg):

    ticket = {
        "id": len(tickets)+1,
        "message": msg,
        "status":"open"
    }

    tickets.append(ticket)

    return ticket


def get_tickets():
    return tickets