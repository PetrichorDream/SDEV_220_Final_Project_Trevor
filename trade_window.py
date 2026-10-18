import tkinter as tk
from tkinter import ttk, messagebox
from classes import TradeEvaluator

def open_trade_window(parent_root, inventory_manager):
    """Opens the Process Trade-In window for employee terminal"""
    trade_win = tk.Toplevel(parent_root)
    trade_win.title("GameStop - Process Trade-In")
    trade_win.geometry("1100x720")
    trade_win.configure(bg="#121212")
    trade_win.transient(parent_root)
    trade_win.grab_set()

    # Header
    header_lbl = tk.Label(
        trade_win, text="Process Customer Trade-In", 
        font=("Arial", 16, "bold"), fg="white", bg="#121212"
    )
    header_lbl.pack(pady=15)

    # Main container split (Left: Catalog lookup and selection, Right: Trade cart and payout)
    main_container = tk.Frame(trade_win, bg="#121212")
    main_container.pack(expand=True, fill="both", padx=20, pady=10)

    # Left frame: catalog search and selection
    left_frame = tk.Frame(main_container, bg="#121212")
    left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    cat_lbl = tk.Label(left_frame, text="1. Select Item to Trade In", font=("Arial", 12, "bold"), fg="white", bg="#121212")
    cat_lbl.pack(anchor="w", pady=(0, 5))

    # Search bar
    search_frame = tk.Frame(left_frame, bg="#121212")
    search_frame.pack(fill="x", pady=5)
    
    tk.Label(search_frame, text="Search:", font=("Arial", 10), fg="#cccccc", bg="#121212").pack(side="left", padx=(0, 5))
    search_var = tk.StringVar()
    search_entry = tk.Entry(
        search_frame, textvariable=search_var, font=("Arial", 10), width=25, 
        bg="#2a2a2a", fg="white", insertbackground="white"
    )
    search_entry.pack(side="left")

    # Catalog treeview
    cat_table_frame = tk.Frame(left_frame, bg="#121212")
    cat_table_frame.pack(fill="both", expand=True, pady=5)

    cat_scroll = ttk.Scrollbar(cat_table_frame)
    cat_scroll.pack(side="right", fill="y")

    # Condition and quantity controls for selected catalog item
    cat_columns = ("id", "title", "platform", "base_trade")
    cat_tree = ttk.Treeview(
        cat_table_frame, columns=cat_columns, show="headings", 
        yscrollcommand=cat_scroll.set, height=14
    )
    cat_scroll.config(command=cat_tree.yview)

    cat_tree.heading("id", text="ID")
    cat_tree.heading("title", text="Item Name")
    cat_tree.heading("platform", text="Platform")
    cat_tree.heading("base_trade", text="Base Trade Value")

    cat_tree.column("id", width=70, anchor="center")
    cat_tree.column("title", width=220, anchor="w")
    cat_tree.column("platform", width=100, anchor="center")
    cat_tree.column("base_trade", width=110, anchor="e")

    cat_tree.pack(fill="both", expand=True)

    # Condition and quantity controls for selected catalog item
    controls_frame = tk.LabelFrame(
        left_frame, text=" Item Condition and Action ", font=("Arial", 10, "bold"), 
        fg="white", bg="#121212", bd=2, relief="groove", padx=10, pady=10
    )
    controls_frame.pack(fill="x", pady=(10, 0))

    cond_lbl = tk.Label(controls_frame, text="Condition:", font=("Arial", 10), fg="#cccccc", bg="#121212")
    cond_lbl.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    condition_var = tk.StringVar(value="Used")
    condition_combo = ttk.Combobox(
        controls_frame, textvariable=condition_var, 
        values=["New", "Used"], state="readonly", width=15
    )
    condition_combo.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    add_btn = tk.Button(
        controls_frame, text="Add to Trade Cart", font=("Arial", 10, "bold"),
        bg="#28a745", fg="white", padx=15, pady=6, relief="flat", cursor="hand2",
        command=lambda: add_to_trade_cart()
    )
    add_btn.grid(row=0, column=2, padx=15, pady=5)


    # Right frame: Trade-in cart and payout summary
    right_frame = tk.Frame(main_container, bg="#121212")
    right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

    cart_lbl = tk.Label(right_frame, text="2. Trade-In Cart", font=("Arial", 12, "bold"), fg="white", bg="#121212")
    cart_lbl.pack(anchor="w", pady=(0, 5))

    cart_table_frame = tk.Frame(right_frame, bg="#121212")
    cart_table_frame.pack(fill="both", expand=True, pady=5)

    cart_scroll = ttk.Scrollbar(cart_table_frame)
    cart_scroll.pack(side="right", fill="y")

    # Cart columns for details
    cart_columns = ("id", "title", "condition", "unit_val")
    cart_tree = ttk.Treeview(
        cart_table_frame, columns=cart_columns, show="headings", 
        yscrollcommand=cart_scroll.set, height=12
    )
    cart_scroll.config(command=cart_tree.yview)

    cart_tree.heading("id", text="ID")
    cart_tree.heading("title", text="Item Name")
    cart_tree.heading("condition", text="Condition")
    cart_tree.heading("unit_val", text="Trade Value")

    cart_tree.column("id", width=70, anchor="center")
    cart_tree.column("title", width=170, anchor="w")
    cart_tree.column("condition", width=90, anchor="center")
    cart_tree.column("unit_val", width=100, anchor="e")

    cart_tree.pack(fill="both", expand=True)

    # Button to empty cart
    empty_cart_btn = tk.Button(
        right_frame, text="Empty Cart", font=("Arial", 9, "bold"),
        bg="#dc3545", fg="white", padx=10, pady=5, relief="flat", cursor="hand2",
        command=lambda: empty_cart()
    )
    empty_cart_btn.pack(anchor="e", pady=5)

    # Summary and payout frame
    summary_frame = tk.LabelFrame(
        right_frame, text=" Payout Summary ", font=("Arial", 10, "bold"), 
        fg="white", bg="#121212", bd=2, relief="groove", padx=15, pady=10
    )
    summary_frame.pack(fill="x", pady=5)

    payout_lbl_text = tk.Label(summary_frame, text="Select Payout Method:", font=("Arial", 10, "bold"), fg="#cccccc", bg="#121212")
    payout_lbl_text.pack(anchor="w", pady=(2, 2))

    payout_var = tk.StringVar(value="Cash")
    payout_combo = ttk.Combobox(
        summary_frame, textvariable=payout_var,
        values=["Cash", "Store Credit (+15% Bonus)"], state="readonly", width=28
    )
    payout_combo.pack(anchor="w", pady=5)
    payout_combo.bind("<<ComboboxSelected>>", lambda e: update_totals())

    final_payout_lbl = tk.Label(summary_frame, text="Final Payout: $0.00", font=("Arial", 13, "bold"), fg="#28a745", bg="#121212")
    final_payout_lbl.pack(anchor="w", pady=(8, 2))

    # Complete trade button
    complete_btn = tk.Button(
        right_frame, text="Complete Trade-In and Update Inventory", font=("Arial", 11, "bold"),
        bg="#28a745", fg="white", pady=10, relief="flat", cursor="hand2",
        command=lambda: complete_trade()
    )
    complete_btn.pack(fill="x", pady=(10, 5))

    # Close window button
    close_btn = tk.Button(
        right_frame, text="Close Window", font=("Arial", 10, "bold"),
        bg="#5a6268", fg="white", pady=8, relief="flat", cursor="hand2",
        command=trade_win.destroy
    )
    close_btn.pack(fill="x", pady=(0, 5))

    #Cart data structure from here on
    trade_cart = []

    # Fills catalog
    def populate_catalog(filter_text=""):
        for row in cat_tree.get_children():
            cat_tree.delete(row)
        
        for item_id, item_obj in inventory_manager.inventory.items():
            search_str = f"{item_id} {item_obj.title} {item_obj.platform} {item_obj.category}".lower()
            if filter_text.lower() in search_str:
                base_t = item_obj.base_trade_value if hasattr(item_obj, "base_trade_value") else 0.0
                cat_tree.insert("", "end", values=(
                    item_obj.item_id,
                    item_obj.title,
                    item_obj.platform,
                    f"${base_t:.2f}"
                ), tags=(item_id,))

    # Gets details about items before I add to cart
    def on_catalog_select(event):
        selected = cat_tree.selection()
        if not selected:
            return
        item_values = cat_tree.item(selected[0], "values")
        item_id = item_values[0]

        if item_id.startswith("G"):
            # Games: Only New or Used. No Like New or Damaged
            condition_combo["values"] = ["New", "Used"]
            if condition_var.get() not in ["New", "Used"]:
                condition_var.set("Used")
        else:
            # Hardware/Accessories: Full range of conditions
            condition_combo["values"] = ["New", "Like New", "Used", "Damaged"]

    cat_tree.bind("<<TreeviewSelect>>", on_catalog_select)

    # Adds to total when adding to cart
    def update_totals():
        subtotal = sum(item["unit_val"] for item in trade_cart)
        selected_method = payout_var.get()
        payout_method = "Credit" if "Store Credit" in selected_method else "Cash"
        final_payout = TradeEvaluator.calculate_session_payout(subtotal, payout_method)

        final_payout_lbl.config(text=f"Final Payout ({'Store Credit' if payout_method == 'Credit' else 'Cash'}): ${final_payout:.2f}")

    # Thingy to add to trade-in cart
    def add_to_trade_cart():
        selected = cat_tree.selection()
        if not selected:
            messagebox.showwarning("Selection Warning", "Please select an item from the catalog to trade in.")
            return
        
        item_values = cat_tree.item(selected[0], "values")
        item_id = item_values[0]
        item_obj = inventory_manager.inventory.get(item_id)
        condition = condition_var.get()

        if item_obj:
            if item_id.startswith("G") and condition not in ["New", "Used"]:
                messagebox.showerror("Invalid Condition", "Game discs can only be traded in as New or Used.")
                return

            unit_val = item_obj.get_trade_value(condition) if hasattr(item_obj, "get_trade_value") else item_obj.base_trade_value

            trade_cart.append({
                "item_id": item_id,
                "title": item_obj.title,
                "condition": condition,
                "unit_val": unit_val
            })

            # Inserts details (ID, Name, Condition, Trade Value) back into the cart tree
            cart_tree.insert("", "end", values=(
                item_id,
                item_obj.title,
                condition,
                f"${unit_val:.2f}"
            ))
            update_totals()

    # Clears cart in case you choose the wrong thing
    def empty_cart():
        """Clears all items from the trade-in cart and resets totals."""
        trade_cart.clear()
        for row in cart_tree.get_children():
            cart_tree.delete(row)
        update_totals()

    # Pops up a box confirming completion
    def complete_trade():
        if not trade_cart:
            messagebox.showwarning("Empty Cart", "Trade-In cart is empty. Add items before completing.")
            return

        for entry in trade_cart:
            inventory_manager.update_stock(entry["item_id"], entry["condition"], 1)

        subtotal = sum(item["unit_val"] for item in trade_cart)
        selected_method = payout_var.get()
        payout_method = "Credit" if "Store Credit" in selected_method else "Cash"
        final_payout = TradeEvaluator.calculate_session_payout(subtotal, payout_method)

        messagebox.showinfo(
            "Trade-In Complete", 
            f"Trade-In successfully processed!\nTotal Items: {len(trade_cart)}\nPayout Method: {selected_method}\nTotal Payout: ${final_payout:.2f}\n\nInventory stock has been updated."
        )
        trade_win.destroy()

    search_var.trace("w", lambda *args: populate_catalog(search_var.get()))
    populate_catalog()