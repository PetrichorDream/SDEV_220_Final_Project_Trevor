import tkinter as tk
from tkinter import ttk

def open_inventory_window(parent_root, inventory_manager):
    """Opens the Check Inventory lookup window"""
    inv_window = tk.Toplevel(parent_root)
    inv_window.title("GameStop Inventory Lookup")
    inv_window.geometry("900x650")
    inv_window.configure(bg="#121212")  # Dark background for the inventory window
    inv_window.transient(parent_root)  # Keep inventory window on top of main window
    inv_window.grab_set()  # Prevent interaction with main window while open

    # Header
    header_lbl = tk.Label(
        inv_window, text="Live Store Inventory Catalog", font=("Arial", 16, "bold"), fg="white", bg="#121212"
    )
    header_lbl.pack(pady=15)

    # Search bar's frame
    search_frame = tk.Frame(inv_window, bg="#121212")
    search_frame.pack(fill="x", padx=20, pady=5)

    search_lbl = tk.Label(
        search_frame, text="Search Item Name or ID:",
        font=("Arial", 11), fg="#cccccc", bg="#121212"
    )
    search_lbl.pack(side="left", padx=5)

    search_var = tk.StringVar()
    search_entry = tk.Entry(
        search_frame, textvariable=search_var,
        font=("Arial", 11), width=30, bg="#2a2a2a", fg="white", insertbackground="white"
    )
    search_entry.pack(side="left", padx=5)

    # Main to split layout
    main_frame = tk.Frame(inv_window, bg="#121212")
    main_frame.pack(expand=True, fill="both", padx=20, pady=10)

    # Treeview frame
    table_frame = tk.Frame(main_frame, bg="#121212")
    table_frame.pack(side="top", fill="both", expand=True)

    # Scrollbar
    tree_scroll = ttk.Scrollbar(table_frame)
    tree_scroll.pack(side="right", fill="y")

    # Column definitions and proportions
    columns = ("Item ID", "Name", "Platform", "Category", "Retail Price", "Trade-In Value")
    tree = ttk.Treeview(
        table_frame, columns=columns, show="headings", yscrollcommand=tree_scroll.set, height=12
    )
    tree_scroll.config(command=tree.yview)

    tree.heading("Item ID", text="Item ID")
    tree.heading("Name", text="Name")
    tree.heading("Platform", text="Platform")
    tree.heading("Category", text="Category")
    tree.heading("Retail Price", text="Retail Price")
    tree.heading("Trade-In Value", text="Trade-In Value")

    tree.column("Item ID", width=80, anchor="center")
    tree.column("Name", width=250, anchor="w")
    tree.column("Platform", width=120, anchor="center")
    tree.column("Category", width=150, anchor="center")
    tree.column("Retail Price", width=120, anchor="e")
    tree.column("Trade-In Value", width=120, anchor="e")

    tree.pack(fill="both", expand=True)

    # Details panel for conditions and respective stock (Changed to LabelFrame for border/title support in case I forget why)
    details_frame = tk.LabelFrame(
        main_frame, text=" Selected Item Condition and Stock ", font=("Arial", 11, "bold"), fg="white", bg="#121212", bd=2, relief="groove", padx=15, pady=15
    )
    details_frame.pack(side="bottom", fill="x", pady=(15, 0))

    details_lbl = tk.Label(
        details_frame, text="Select an item from the table above to view stock and condition details.",
        font=("Arial", 11), fg="#aaaaaa", bg="#121212", justify="left"
    )
    details_lbl.pack(anchor="w")

    # Function to populate the treeview with inventory data
    def populate_treeview(filter_text=""):
        for row in tree.get_children():
            tree.delete(row)

        for item_id, item_obj in inventory_manager.inventory.items():
            # Matches item_obj.title from classes.py
            search_str = f"{item_id} {item_obj.title} {item_obj.platform} {item_obj.category}".lower()
            if filter_text.lower() in search_str:
                retail_new = item_obj.get_retail_price("New") if hasattr(item_obj, "get_retail_price") else item_obj.new_price
                trade_new = item_obj.get_trade_value("New") if hasattr(item_obj, "get_trade_value") else item_obj.base_trade_value * 0.5

                tree.insert("", "end", values=(
                    item_obj.item_id,
                    item_obj.title,
                    item_obj.category,
                    item_obj.platform,
                    f"${retail_new:.2f}",
                    f"${trade_new:.2f}"
                ), tags=(item_id,))

    # When an item is clicked, show a breakdown of details
    def on_item_select(event):
        selected_items = tree.selection()
        if not selected_items:
            return

        item_values = tree.item(selected_items[0], "values")  # Lowercase "values"
        item_id = item_values[0]
        item_obj = inventory_manager.inventory.get(item_id)

        if item_obj:
            details_text = f"Item: {item_obj.title} ({item_obj.platform}) | ID: {item_obj.item_id}\n\n"
            
            # Should  pull inventory condition stock and pricing directly from the item's stock dict
            details_breakdown = []
            for cond, stock_count in item_obj.stock.items():
                r_price = item_obj.get_retail_price(cond) if hasattr(item_obj, "get_retail_price") else 0.0
                t_val = item_obj.get_trade_value(cond) if hasattr(item_obj, "get_trade_value") else 0.0
                details_breakdown.append(f"• {cond}: Stock = {stock_count}  |  Retail = ${r_price:.2f}  |  Trade = ${t_val:.2f}")
                    
            details_lbl.config(text=details_text + "\n".join(details_breakdown), fg="white")

    # Indents outside of on_item_select function
    tree.bind("<<TreeviewSelect>>", on_item_select)

    # Binds search box typing to live filter
    search_var.trace("w", lambda *args: populate_treeview(search_var.get()))

    # Initial loading of all items
    populate_treeview()

    # Button to close window
    close_btn = tk.Button(
        inv_window, text="Close Window", font=("Arial", 10, "bold"),
        bg="#5a6268", fg="white", padx=20, pady=8, relief="flat",
        command=inv_window.destroy
    )
    close_btn.pack(pady=10)