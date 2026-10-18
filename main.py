import tkinter as tk
from tkinter import ttk, messagebox
from dataset import load_initial_inventory
from inventory_window import open_inventory_window
from trade_window import open_trade_window
from purchase_window import open_purchase_window

class GameStopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GameStop Service System")
        self.root.geometry("850x600")
        self.root.minsize(750, 500)

        self.root.configure(bg="#121212")  # Dark background for the main window
        self.inventory_manager = load_initial_inventory()
        self.create_main_menu()

    def create_main_menu(self):
        """Creates dashboard with buttons for each service"""
        # Clear any existing widgets when returning to the main menu
        for widget in self.root.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.root, bg="#121212", pady=30)
        header_frame.pack(fill="x")

        # Container frame to hold "Game" and "Stop", and the rest of the text side byside
        title_container = tk.Frame(header_frame, bg="#121212")
        title_container.pack(pady=(33, 0))

        # "Game" in white
        tk.Label(
            title_container, text="Game",
            font=("Arial", 18, "bold"), fg="white", bg="#121212"
        ).pack(side="left")

        # "Stop" in red
        tk.Label(
            title_container, text="Stop",
            font=("Arial", 18, "bold"), fg="#e60012", bg="#121212"
        ).pack(side="left")

        # " Service System" in white
        tk.Label(
            title_container, text=" Service System",
            font=("Arial", 18, "bold"), fg="white", bg="#121212"
        ).pack(side="left")

        # Employee termianl text stuff
        subtitle_label = tk.Label(
            text="Employee Terminal",
            font=("Arial", 11),
            fg="#aaaaaa",
            bg="#121212"
        )
        subtitle_label.pack(pady=5)

        # Content area for menu buttons
        body_frame = tk.Frame(self.root, bg="#121212", padx=40, pady=20)
        body_frame.pack(expand=True, fill="both")

        # Center buttons
        body_frame.grid_columnconfigure(0, weight=1, uniform="equal_cols")
        body_frame.grid_columnconfigure(1, weight=1, uniform="equal_cols")
        body_frame.grid_rowconfigure(0, weight=1)
        body_frame.grid_rowconfigure(1, weight=1)

        """Dashboard buttons"""
        btn_inventory = tk.Button(
            body_frame, text="Check Inventory",
            font=("Arial", 12, "bold"), bg="#e60012", fg="white",
            width=22, pady=15, relief="flat", cursor="hand2",
            command=self.open_inventory_window
        )
        btn_inventory.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        btn_purchase = tk.Button(
            body_frame, text="Process Purchase",
            font=("Arial", 12, "bold"), bg="#006699", fg="white",
            width=22, pady=15, relief="flat", cursor="hand2",
            command=self.open_purchase_window
        )
        btn_purchase.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        btn_trade = tk.Button(
            body_frame, text="Process Trade-In",
            font=("Arial", 12, "bold"), bg="#28a745", fg="white",
            width=22, pady=15, relief="flat", cursor="hand2",
            command=self.open_trade_window
        )
        btn_trade.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")

        btn_exit = tk.Button(
            body_frame, text="Exit System",
            font=("Arial", 12, "bold"), bg="#6c757d", fg="white",
            width=22, pady=15, relief="flat", cursor="hand2",
            command=self.root.quit
        )
        btn_exit.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")

    def open_inventory_window(self):
        """Triggers the inventory lookup window from the separate module."""
        open_inventory_window(self.root, self.inventory_manager)

    def open_purchase_window(self):
        """Triggers the purchase window from the separate module"""
        open_purchase_window(self.root, self.inventory_manager)

    def open_trade_window(self):
        """Triggers the trade-in window from the separate module"""
        open_trade_window(self.root, self.inventory_manager)


if __name__ == "__main__":
    root = tk.Tk()
    app = GameStopApp(root)
    root.mainloop()