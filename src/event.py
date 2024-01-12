class Event:
    def __init__(self, event_name, seating_map, ticket_prices, availability):
        self.event_name = event_name
        self.seating_map = seating_map
        self.ticket_prices = ticket_prices
        self.availability = availability

    def __repr__(self):
        return f"{self.event_name}"

def read_event_info_from_file(file_path):
    events = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Assuming each line in the file contains information separated by commas
                event_data = line.strip().split(',')
                if len(event_data) == 4:
                    # Extracting data for each event
                    event_name, seating_map, ticket_prices, availability = event_data
                    event = Event(event_name, seating_map, ticket_prices, availability)
                    events.append(event)
                else:
                    print(f"Skipping invalid line: {line}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return events

# Updated file path
file_path = 'data/events_data.txt'  # Replace with the actual path to your file
event_list = read_event_info_from_file(file_path)

# Print information for each event
for event in event_list:
    print(f"Event Name: {event.event_name}")
    print(f"Seating Map: {event.seating_map}")
    print(f"Ticket Prices: {event.ticket_prices}")
    print(f"Availability: {event.availability}")
    print()
