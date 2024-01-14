import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from event import read_event_info_from_file
from event import update_event_reserved_seats_by_name
from event import Event
from reservation import Reservation

class TicketReservationApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x720")
        self.events_db_path = "./data/events_data.txt"
        self.events = read_event_info_from_file(self.events_db_path)
        self.selected_event = Event()
        self.reservation = Reservation()
        self.home_scene()
    
    def home_scene(self):
        for widget in self.master.winfo_children():
            widget.destroy()
            
        self.events = read_event_info_from_file(self.events_db_path)
        self.selected_event = Event()
        self.reservation = Reservation()

        home_frame = ttk.Frame(self.master, width=1280, height=720)
        home_frame.pack()

        home_label = ttk.Label(home_frame, text='Welcome to Ticket Reservation System', font=("Helvetica", 16))
        home_label.pack(pady=10)
				
        self.event_listbox = tk.Listbox(home_frame, selectmode=tk.SINGLE, font=("Helvetica", 12))
        for event in self.events:
            self.event_listbox.insert(tk.END, event.event_name)
        self.event_listbox.pack(pady=10)

        self.select_event_button = ttk.Button(home_frame, text="Select Event", command=self.set_selected_event)
        self.select_event_button.pack(pady=10, ipadx=5, ipady=3)
                
        #todo: reservation scene
        # self.select_event_button = ttk.Button(home_frame, text="Show Reservations", command=self.booking_scene)
        # self.select_event_button.pack(pady=10, ipadx=5, ipady=3)
		
    def booking_scene(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.booking_frame = ttk.Frame(self.master, width=1280, height=720)
        self.booking_frame.pack()

        booking_label = ttk.Label(self.booking_frame, text='Select Seats and Confirm Booking', font=("Helvetica", 16))
        booking_label.pack(pady=10)
        
        reserved_seats_label = ttk.Label(self.booking_frame, text="Reserved seats: " + ', '.join(self.selected_event.reserved_seats), font=("Helvetica", 16))
        reserved_seats_label.pack(pady=10)

        self.display_seating_map()
		        
    def confirmation_scene(self):
        for widget in self.master.winfo_children():
            widget.destroy()
    
        confirmation_frame = ttk.Frame(self.master, width=1280, height=720)
        confirmation_frame.pack()
    
        # Add labels for headers
        ttk.Label(confirmation_frame, text="Reservation Details", font=("Helvetica", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
        ttk.Label(confirmation_frame, text="Name:", font=("Helvetica", 14)).grid(row=1, column=0, pady=10, sticky="w")
        # Simulate adding an Entry for customer name
        self.customer_name_entry = ttk.Entry(confirmation_frame, font=("Helvetica", 14))
        self.customer_name_entry.grid(row=1, column=1, pady=10, sticky="w")
    
        # Add labels to display reservation details in a grid
        details_labels = [
            ("Event:", self.reservation.event_name),
            ("Selected Seat:", self.reservation.selected_seat),
            ("Ticket Type:", self.reservation.ticket_type),
            ("Total Cost:", f"${self.reservation.total_cost:.2f}")
        ]
    
        for row_index, (header, detail) in enumerate(details_labels, start=2):
            ttk.Label(confirmation_frame, text=header).grid(row=row_index, column=0, pady=5, sticky="w")
            ttk.Label(confirmation_frame, text=detail).grid(row=row_index, column=1, pady=5, sticky="w")
    
        # Simulate a button to finish and go back to home scene
        finish_button = ttk.Button(confirmation_frame, text="Finish", command=self.confirm_booking)
        finish_button.grid(row=row_index + 1, column=0, columnspan=2, pady=10, ipadx=5, ipady=3)
        finish_button = ttk.Button(confirmation_frame, text="cancel", command=self.home_scene)
        finish_button.grid(row=row_index + 2, column=0, columnspan=2, pady=10, ipadx=5, ipady=3)



    def set_selected_event(self):
        # Get the selected event from the listbox
        selected_event_index = self.event_listbox.curselection()
        
        if selected_event_index:
            selected_event_index = selected_event_index[0]  # Grab the first selected index
            self.selected_event = self.events[selected_event_index]
            self.reservation.event_name = self.selected_event.event_name
            print("Selected Event: " + self.reservation.event_name)
            self.booking_scene()
      
    def display_seating_map(self):
      seating_map = [
                ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
                ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
                ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
                ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
                ['VIP1', 'VIP2', 'VIP3', 'VIP4', 'VIP5', 'VIP6', 'VIP7', 'VIP8'],
                ['VIP9', 'VIP10', 'VIP11', 'VIP12', 'VIP13', 'VIP14', 'VIP15', 'VIP16']
            ]
      frame_seating = ttk.Frame(self.booking_frame)
      frame_seating.pack(pady=10)

      for row_index, row in enumerate(seating_map):
        for col_index, seat in enumerate(row):
            # Use a lambda function to pass the seat parameter
            seat_buttons = ttk.Button(frame_seating, text=seat, command=lambda s=seat: self.select_seat(s))
            seat_buttons.grid(row=row_index, column=col_index, padx=5, pady=5)

    def select_seat(self, seat):
      if seat in self.selected_event.reserved_seats:
        messagebox.showerror("Seat Reserved", f"Seat {seat} is already reserved for {self.selected_event.event_name}")
        return 
        
      self.reservation.selected_seat = seat
      if self.reservation.selected_seat.startswith("VIP"):
        self.reservation.total_cost = self.selected_event.event_cost[1]
        self.reservation.ticket_type = "VIP"
      else:
        self.reservation.total_cost = self.selected_event.event_cost[0]
        self.reservation.ticket_type = "standard " + self.reservation.selected_seat[0]
      self.confirmation_scene()
      
    def confirm_booking(self):
        customer_name = self.customer_name_entry.get()

        if customer_name.isspace() or not customer_name:
            messagebox.showerror("Confirmation Error!","Please enter your name in the entry to confirm the ticket reservation!")
            return

        update_event_reserved_seats_by_name(self.events_db_path, self.reservation.event_name, self.reservation.selected_seat)
        self.reservation.customer_name = customer_name
        self.reservation.save_reservation()
        print(self.reservation.to_string())
        self.home_scene()

      
if __name__ == "__main__":
    root = tk.Tk()
    app = TicketReservationApp(root)
    root.mainloop()
