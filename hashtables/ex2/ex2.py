#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Define empty route and hashtable
    dict = {}
    route = []

    # Inserting all flights into the hashtable
    for ticket in tickets:
        dict[ticket.source] = ticket.destination

    # Getting the first destination
    nextStop = dict["NONE"]
    route.append(nextStop)

    while nextStop is not "NONE":
        route.append(dict[nextStop])
        nextStop = dict[nextStop]

    return route
