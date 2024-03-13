import random
 
def generate_tickets(ticket_count, max_number):
    list_to_return = random.sample(range(0, max_number), ticket_count)
    return (list_to_return, random.sample(list_to_return, 1)[0])