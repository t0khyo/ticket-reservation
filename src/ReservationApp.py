import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from event import read_event_info_from_file, update_event_reserved_seats_by_name, Event
from reservation import Reservation

class TicketReservationApp:
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720
    FONT_LARGE = ("consolas", 16)
    FONT_MEDIUM = ("consolas", 14)
    FONT_SMALL = ("consolas", 12)
    EVENTS_DB_PATH = "./data/events_data.txt"

    def __init__(self, master):
        self.master = master
        self.configure_window()
        self.configure_styles()
        self.initialize_data()
        self.display_home_scene()
    
    def configure_window(self):
        self.master.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
    
    def configure_styles(self):
        style = ttk.Style()
        style.configure('Reserved.TButton', background='red', font=('Helvetica', 10))
        style.configure('Available.TButton', background='green', font=('Helvetica', 10))
    
    def initialize_data(self):
        self.events = read_event_info_from_file(self.EVENTS_DB_PATH)
        self.selected_event = Event()
        self.reservation = Reservation()
        self.seating_map = [
                ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
                ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
                ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
                ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
                ['VIP1', 'VIP2', 'VIP3', 'VIP4', 'VIP5', 'VIP6', 'VIP7', 'VIP8'],
                ['VIP9', 'VIP10', 'VIP11', 'VIP12', 'VIP13', 'VIP14', 'VIP15', 'VIP16']
            ]
    
    def clear_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()
    
# *Home Scene*
    def display_home_scene(self):
        self.clear_widgets()
        self.refresh_events()
        self.create_frame()
        self.add_label('Welcome to Ticket Reservation System', self.FONT_LARGE)
        self.populate_event_listbox()
        self.add_button("Select Event", self.handle_event_selection)
    
    def refresh_events(self):
        self.events = read_event_info_from_file(self.EVENTS_DB_PATH)
        self.selected_event = Event()
        self.reservation = Reservation()
    
    def create_frame(self):
        self.current_frame = ttk.Frame(self.master)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
    
    def add_label(self, text, font, padding_y=10):
        label = ttk.Label(self.current_frame, text=text, font=font)
        label.pack(pady=padding_y)
    
    def populate_event_listbox(self):
        self.event_listbox = tk.Listbox(self.current_frame, selectmode=tk.SINGLE, font=self.FONT_SMALL)
        for event in self.events:
            self.event_listbox.insert(tk.END, event.event_name)
        self.event_listbox.pack(pady=10)
    
    def add_button(self, text, command, padding_y=10, padding_x=5):
        button = ttk.Button(self.current_frame, text=text, command=command)
        button.pack(pady=padding_y, ipadx=padding_x, ipady=3)
    
    def handle_event_selection(self):
        selected_index = self.get_selected_event_index()
        if selected_index is None:
          messagebox.showerror("Event Selection Error", "Please select an event to continue!")
          return
        self.update_selected_event(selected_index)
        self.display_booking_scene()
    
    def get_selected_event_index(self):
        selection = self.event_listbox.curselection()
        return selection[0] if selection else None
    
    def update_selected_event(self, index):
        self.selected_event = self.events[index]
        self.reservation.event_name = self.selected_event.event_name
        print(f"Selected Event: {self.reservation.event_name}")
		
# *booking scent*
    def display_booking_scene(self):
        self.clear_widgets()
        self.create_frame()
        self.add_label('Select Seats and Confirm Booking', self.FONT_LARGE)
        self.display_reserved_seats()
        self.display_seating_map()
    
    def display_reserved_seats(self):
        reserved_seats_text = "Reserved seats: " + ', '.join(self.selected_event.reserved_seats)
        self.add_label(reserved_seats_text, self.FONT_MEDIUM)
    
    def display_seating_map(self):
        seating_map_frame = ttk.Frame(self.current_frame)
        seating_map_frame.pack(pady=10)
        self.create_seating_buttons(seating_map_frame)
    
    def create_seating_buttons(self, frame):
        for row_index, row in enumerate(self.seating_map):
            for col_index, seat in enumerate(row):
                if seat in self.selected_event.reserved_seats:
                    seat_button = ttk.Button(frame, text=seat, command=lambda s=seat: self.select_seat(s),style='Reserved.TButton')
                else:
                    seat_button = ttk.Button(frame, text=seat, command=lambda s=seat: self.select_seat(s), style='Available.TButton')

                seat_button.grid(row=row_index, column=col_index, padx=5, pady=5)
    
    def select_seat(self, seat):
        if seat in self.selected_event.reserved_seats:
            messagebox.showerror("Seat Reserved", f"Seat {seat} is already reserved for {self.selected_event.event_name}")
            return
          
        self.reservation.selected_seat = seat
        
        if self.reservation.selected_seat.startswith("VIP"):
            self.reservation.total_cost = self.selected_event.event_cost[1]
            self.reservation.ticket_type = "VIP "
        else:
            self.reservation.total_cost = self.selected_event.event_cost[0]
            self.reservation.ticket_type = "standard " + self.reservation.selected_seat[0]
            
        self.display_confirmation_scene()    
        
        
# *Confirmation Scene*
    def display_confirmation_scene(self):
        self.clear_widgets()
        self.create_frame()
        self.add_label("Reservation Details", self.FONT_LARGE)
        self.add_customer_name_entry()
        self.display_reservation_details()
        self.add_finish_buttons()
    
    def add_customer_name_entry(self):
        ttk.Label(self.current_frame, text="Name:", font=self.FONT_MEDIUM).pack(pady=10, anchor='w')
        self.customer_name_entry = ttk.Entry(self.current_frame, font=self.FONT_MEDIUM)
        self.customer_name_entry.pack(pady=10)
    
    def display_reservation_details(self):
        details = self.reservation.get_details()
        for detail in details:
            ttk.Label(self.current_frame, text=detail[0], font=self.FONT_MEDIUM).pack(anchor='w')
            ttk.Label(self.current_frame, text=detail[1], font=self.FONT_MEDIUM, foreground="#77FdF1").pack(anchor='w')
    
    def add_finish_buttons(self):
        self.add_button("Finish", self.confirm_booking, padding_y=20)
        self.add_button("Cancel", self.display_home_scene)
    
    def confirm_booking(self):
        customer_name = self.customer_name_entry.get().strip()
        if not customer_name:
            messagebox.showerror("Confirmation Error!", "Please enter your name to confirm the ticket reservation!")
            return
        self.reservation.customer_name = customer_name
        self.finalize_booking()
    
    def finalize_booking(self):
        update_event_reserved_seats_by_name(self.EVENTS_DB_PATH, self.reservation.event_name, self.reservation.selected_seat)
        self.reservation.save()
        print(self.reservation.to_string())
        self.display_home_scene()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketReservationApp(root)
    root.mainloop()
