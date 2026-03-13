import pymysql

connection = pymysql.connect(
    host="helpdesk-db.cih06ea00gby.us-east-1.rds.amazonaws.com",
    user="admin",
    password="cloudmasa123",
    database="helpdesk",
    cursorclass=pymysql.cursors.DictCursor,
    ssl={
        "ca": "global-bundle.pem"
    }
)

def create_ticket(user, message, intent):

    cursor = connection.cursor()

    query = """
    INSERT INTO tickets (user, message, intent)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (user, message, intent))
    connection.commit()

    ticket_id = cursor.lastrowid

    return {
        "id": ticket_id,
        "user": user,
        "message": message,
        "intent": intent
    }


def get_tickets():

    cursor = connection.cursor()

    query = "SELECT * FROM tickets"

    cursor.execute(query)

    result = cursor.fetchall()

    return result