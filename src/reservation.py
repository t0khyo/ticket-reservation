class Reservation:
    def __init__(self, customer_name=None, event_name=None, selected_seat=None, ticket_type=None, total_cost=None):
        self.customer_name = customer_name
        self.event_name = event_name
        self.selected_seat = selected_seat
        self.ticket_type = ticket_type
        self.total_cost = total_cost
    
    def to_string(self):
        return f"{self.customer_name},{self.event_name},{self.selected_seat},{self.ticket_type},{self.total_cost}"
    
    def save_reservation(reservation):
        file_path = "data/reservation_data.txt"
        with open(file_path, 'a') as file:
            file.write(reservation.to_string() + "\n")