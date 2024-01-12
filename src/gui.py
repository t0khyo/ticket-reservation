import tkinter as tk
from tkinter import Listbox
from event import Event, read_event_info_from_file

class TicketReservationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ticket Reservation System")
        self.master.geometry("1280x720")

        # Create a frame for each scene
        self.home_frame = HomeFrame(self.master, self.show_seats_page, self.show_reservations)
        self.seats_frame = None

    def show_seats_page(self, selected_event_name):
        # Destroy the existing Seats Frame if it exists
        if self.seats_frame:
            self.seats_frame.destroy()

        # Create the Seats Frame
        self.seats_frame = SeatsFrame(self.master, selected_event_name)

    def show_reservations(self):
        # Implement logic to show saved reservations
        pass

class HomeFrame(tk.Frame):
    def __init__(self, master, show_seats_callback, show_reservations_callback):
        super().__init__(master)
        self.pack()

        # Event list (fetch the data from the text file)
        self.events = read_event_info_from_file("./data/events_data.txt")

        # Listbox to display events
        self.event_listbox = Listbox(self, selectmode=tk.SINGLE, font=("Helvetica", 16))
        for event in self.events:
            self.event_listbox.insert(tk.END, event.event_name)
        self.event_listbox.pack(pady=50)

        # Button to select event
        self.select_event_button = tk.Button(self, text="Select Event",
                                            command=lambda: show_seats_callback(self.event_listbox.get(tk.ACTIVE)),
                                            font=("Helvetica", 16))
        self.select_event_button.pack()

        # Label "or"
        or_label = tk.Label(self, text="or", font=("Helvetica", 16))
        or_label.pack(pady=20)

        # Button to show reservations
        self.show_reservations_button = tk.Button(self, text="Show Reservations", command=show_reservations_callback,
                                                  font=("Helvetica", 16))
        self.show_reservations_button.pack()

class SeatsFrame(tk.Frame):
    def __init__(self, master, selected_event_name):
        super().__init__(master)
        self.pack()

        # Find the selected event details
        selected_event = next((event for event in master.home_frame.events if event.event_name == selected_event_name), None)

        if selected_event:
            self.master.title(f"Event Seats - {selected_event.event_name}")
            self.master.geometry("1280x720")

            # Seating Map
            self.seating_map = [
                ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
                ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
                ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
                ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
                ['VIP1', 'VIP2', 'VIP3', 'VIP4', 'VIP5', 'VIP6', 'VIP7', 'VIP8'],
                ['VIP9', 'VIP10', 'VIP11', 'VIP12', 'VIP13', 'VIP14', 'VIP15', 'VIP16']
            ]

            # Display seating map
            self.display_seating_map()

    def display_seating_map(self):
        for row_index, row in enumerate(self.seating_map):
            for col_index, seat in enumerate(row):
                x = col_index * 80  # Adjust the spacing based on your preference
                y = row_index * 80  # Adjust the spacing based on your preference
                seat_label = tk.Label(self, text=seat, borderwidth=1, relief="solid", width=5, height=2)
                seat_label.place(x=x, y=y)


# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = TicketReservationApp(root)
    root.mainloop()













# import tkinter as tk
# from tkinter import Listbox
# from event import Event, read_event_info_from_file

# class TicketReservationApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Ticket Reservation System")
#         self.master.geometry("1280x720")
        
#         # Home Page
#         self.create_home_page()

#     def create_home_page(self):
#         # Event list (fetch the data from the text file)
#         self.events = read_event_info_from_file("./data/events_data.txt")
    
#         # Listbox to display events
#         self.event_listbox = Listbox(self.master, selectmode=tk.SINGLE, font=("Helvetica", 16))
#         for event in self.events:
#             self.event_listbox.insert(tk.END, event.event_name)
#         self.event_listbox.pack(pady=50)
    
#         # Button to select event
#         self.select_event_button = tk.Button(self.master, text="Select Event", command=self.show_seats_page, font=("Helvetica", 16))
#         self.select_event_button.pack()
    
#         # Label "or"
#         or_label = tk.Label(self.master, text="or", font=("Helvetica", 16))
#         or_label.pack(pady=20)
    
#         # Button to show reservations
#         self.show_reservations_button = tk.Button(self.master, text="Show Reservations", command=self.show_reservations, font=("Helvetica", 16))
#         self.show_reservations_button.pack()

    
#     def show_seats_page(self):
#         # Get the selected event name
#         selected_event_name = self.event_listbox.get(tk.ACTIVE)
    
#         # Find the selected event details
#         selected_event = next((event for event in self.events if event.event_name == selected_event_name), None)
    
#         if selected_event:
#             # Create a Toplevel window for the Seats Page
#             seats_page_window = tk.Toplevel(self.master)
#             seats_page = SeatsPage(seats_page_window, selected_event)




#     def show_reservations(self):
#         # Implement logic to show saved reservations
#         pass

# class SeatsPage:
#     def __init__(self, master, selected_event):
#         self.master = master
#         self.master.title(f"Event Seats - {selected_event.event_name}")
#         self.master.geometry("1280x720")

#         # Seating Map
#         self.seating_map = [
#             ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
#             ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
#             ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
#             ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
#             ['VIP1', 'VIP2', 'VIP3', 'VIP4', 'VIP5', 'VIP6', 'VIP7', 'VIP8'],
#             ['VIP9', 'VIP10', 'VIP11', 'VIP12', 'VIP13', 'VIP14', 'VIP15', 'VIP16']
#         ]

#         # Display seating map
#         self.display_seating_map()

#         # Bind the closing event to a method
#         self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

#     def display_seating_map(self):
#         for row_index, row in enumerate(self.seating_map):
#             for col_index, seat in enumerate(row):
#                 x = col_index * 80  # Adjust the spacing based on your preference
#                 y = row_index * 80  # Adjust the spacing based on your preference
#                 seat_label = tk.Label(self.master, text=seat, borderwidth=1, relief="solid", width=5, height=2)
#                 seat_label.place(x=x, y=y)

#     def on_closing(self):
#         # Implement logic to handle the closing of the SeatsPage window
#         self.master.destroy()

#     def __init__(self, master, selected_event):
#         self.master = master
#         self.master.title(f"Event Seats - {selected_event.event_name}")
#         self.master.geometry("1280x720")

#         # Seating Map
#         self.seating_map = [
#             ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
#             ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
#             ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
#             ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
#             ['VIP1', 'VIP2', 'VIP3', 'VIP4', 'VIP5', 'VIP6', 'VIP7', 'VIP8'],
#             ['VIP9', 'VIP10', 'VIP11', 'VIP12', 'VIP13', 'VIP14', 'VIP15', 'VIP16']
#         ]

#         # Display seating map
#         self.display_seating_map()

#     def display_seating_map(self):
#         for row_index, row in enumerate(self.seating_map):
#             for col_index, seat in enumerate(row):
#                 x = col_index * 80  # Adjust the spacing based on your preference
#                 y = row_index * 80  # Adjust the spacing based on your preference
#                 seat_label = tk.Label(self.master, text=seat, borderwidth=1, relief="solid", width=5, height=2)
#                 seat_label.place(x=x, y=y)

# # Other methods and logic will be added here as needed

# # Create the main application window
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TicketReservationApp(root)
#     root.mainloop()
