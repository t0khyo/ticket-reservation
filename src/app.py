import tkinter as tk
from tkinter import ttk
from event import read_event_info_from_file
from reservation import *

class TicketReservationApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x720")
        self.events = read_event_info_from_file("./data/events_data.txt")
        self.selected_event = None
        self.selected_seat = None
        self.home_scene()
    
    def home_scene(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.selected_event = None
        self.selected_seat = None

        self.frame1 = ttk.Frame(self.master, width=1280, height=720)
        self.frame1.pack()

        self.label_home = ttk.Label(self.frame1, text='Welcome to Ticket Reservation System', font=("Helvetica", 16))
        self.label_home.pack(pady=10)
				
        self.event_listbox = tk.Listbox(self.frame1, selectmode=tk.SINGLE, font=("Helvetica", 12))
        for event in self.events:
            self.event_listbox.insert(tk.END, event.event_name)
        self.event_listbox.pack(pady=10)

        self.select_event_button = ttk.Button(self.frame1, text="Select Event", command=self.select_event)
        self.select_event_button.pack(pady=10, ipadx=5, ipady=3)
        
        self.select_event_button = ttk.Button(self.frame1, text="Show Reservations", command=self.booking_scene)
        self.select_event_button.pack(pady=10, ipadx=5, ipady=3)
		
    def booking_scene(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.frame2 = ttk.Frame(self.master, width=1280, height=720)
        self.frame2.pack()

        self.label_booking = ttk.Label(self.frame2, text='Select Seats and Confirm Booking', font=("Helvetica", 16))
        self.label_booking.pack(pady=10)

        self.seating_map = [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
            ['VIP1', 'VIP2', 'VIP3', 'VIP4', 'VIP5', 'VIP6', 'VIP7', 'VIP8'],
            ['VIP9', 'VIP10', 'VIP11', 'VIP12', 'VIP13', 'VIP14', 'VIP15', 'VIP16']
        ]

        self.display_seating_map()
    
        # self.confirm_booking_button = ttk.Button(self.frame2, text="Confirm Booking", command=self.home_scene)
        # self.confirm_booking_button.pack(pady=10)
		        
    def confirmation_scene(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.confirm_frame = ttk.Frame(self.master, width=1280, height=720)
        self.confirm_frame.pack()

        # Simulate adding an Entry for customer name
        self.customer_name_entry = ttk.Entry(self.confirm_frame, font=("Helvetica", 12))
        self.customer_name_entry.pack(pady=10)

        # Simulate a button to finish and go back to home scene
        finish_button = ttk.Button(self.confirm_frame, text="Finish", command=self.confirm_booking)
        finish_button.pack(pady=10 ,ipadx=5, ipady=3)

    def select_event(self):
        # Get the selected event from the listbox
        selected_event_index = self.event_listbox.curselection()
        
        if selected_event_index:
            selected_event_index = selected_event_index[0]  # Grab the first selected index
            self.selected_event = self.events[selected_event_index]
            print("Selected Event: " + self.selected_event.event_name)
            self.booking_scene()
      
    def display_seating_map(self):
      frame_seating = ttk.Frame(self.frame2)
      frame_seating.pack(pady=10)

      for row_index, row in enumerate(self.seating_map):
        for col_index, seat in enumerate(row):
            # Use a lambda function to pass the seat parameter
            seat_buttons = ttk.Button(frame_seating, text=seat, command=lambda s=seat: self.select_seat(s))
            seat_buttons.grid(row=row_index, column=col_index, padx=5, pady=5)

    def select_seat(self, seat):
      self.selected_seat = seat
      print("Selected seat: " + seat)
      self.confirmation_scene()
      
    def confirm_booking(self):
        customer_name = self.customer_name_entry.get()
  
        reservation = Reservation(customer_name, self.selected_event, self.selected_seat, "VIP", "Total Cost")

        reservation.save_reservation()
			
        # Go back to the home scene
        self.home_scene()

      
if __name__ == "__main__":
    root = tk.Tk()
    app = TicketReservationApp(root)
    root.mainloop()
