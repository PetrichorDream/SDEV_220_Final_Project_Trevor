import tkinter as tk
from tkinter import ttk, messagebox

def open_purchase_window(parent_root, inventory_manager):
    """Opens the Process Purchase window for the employee terminal"""
    purchase_win = tk.Toplevel(parent_root)
    purchase_win.title("GameStop - Process Purchase")
    purchase_win.geometry("1100x720")
    purchase_win.configure(bg="#121212")
    purchase_win.transient(parent_root)
    purchase_win.grab_set()

    # Header
    header_lbl = tk.Label(
        purchase_win, text="Process Customer Purchase", 
        font=("Arial", 16, "bold"), fg="white", bg="#121212"
    )
    header_lbl.pack(pady=15)

    # Container split (Left: Catalog lookup and selection, Right: Purchase cart and totals)
    main_container = tk.Frame(purchase_win, bg="#121212")
    main_container.pack(expand=True, fill="both", padx=20, pady=10)

    # Left frame: Catalog search and selection
    left_frame = tk.Frame(main_container, bg="#121212")
    left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    cat_lbl = tk.Label(left_frame, text="1. Select Item to Purchase", font=("Arial", 12, "bold"), fg="white", bg="#121212")
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

    # Catalog Treeview
    cat_table_frame = tk.Frame(left_frame, bg="#121212")
    cat_table_frame.pack(fill="both", expand=True, pady=5)

    cat_scroll = ttk.Scrollbar(cat_table_frame)
    cat_scroll.pack(side="right", fill="y")

    cat_columns = ("id", "title", "platform", "new_price")
    cat_tree = ttk.Treeview(
        cat_table_frame, columns=cat_columns, show="headings", 
        yscrollcommand=cat_scroll.set, height=14
    )
    cat_scroll.config(command=cat_tree.yview)

    cat_tree.heading("id", text="ID")
    cat_tree.heading("title", text="Item Name")
    cat_tree.heading("platform", text="Platform")
    cat_tree.heading("new_price", text="Retail (New)")

    cat_tree.column("id", width=70, anchor="center")
    cat_tree.column("title", width=220, anchor="w")
    cat_tree.column("platform", width=100, anchor="center")
    cat_tree.column("new_price", width=110, anchor="e")

    cat_tree.pack(fill="both", expand=True)

    # Condition controls for selected catalog item
    controls_frame = tk.LabelFrame(
        left_frame, text=" Item Condition and Action ", font=("Arial", 10, "bold"), 
        fg="white", bg="#121212", bd=2, relief="groove", padx=10, pady=10
    )
    controls_frame.pack(fill="x", pady=(10, 0))

    cond_lbl = tk.Label(controls_frame, text="Condition:", font=("Arial", 10), fg="#cccccc", bg="#121212")
    cond_lbl.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    condition_var = tk.StringVar(value="New")
    condition_combo = ttk.Combobox(
        controls_frame, textvariable=condition_var, 
        values=["New", "Used"], state="readonly", width=15
    )
    condition_combo.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    add_btn = tk.Button(
        controls_frame, text="Add to Cart", font=("Arial", 10, "bold"),
        bg="#006699", fg="white", padx=15, pady=6, relief="flat", cursor="hand2",
        command=lambda: add_to_purchase_cart()
    )
    add_btn.grid(row=0, column=2, padx=15, pady=5)


    # Right frame: Purchase cart and totals summary
    right_frame = tk.Frame(main_container, bg="#121212")
    right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

    cart_lbl = tk.Label(right_frame, text="2. Shopping Cart", font=("Arial", 12, "bold"), fg="white", bg="#121212")
    cart_lbl.pack(anchor="w", pady=(0, 5))

    cart_table_frame = tk.Frame(right_frame, bg="#121212")
    cart_table_frame.pack(fill="both", expand=True, pady=5)

    cart_scroll = ttk.Scrollbar(cart_table_frame)
    cart_scroll.pack(side="right", fill="y")

    cart_columns = ("id", "title", "condition", "unit_price")
    cart_tree = ttk.Treeview(
        cart_table_frame, columns=cart_columns, show="headings", 
        yscrollcommand=cart_scroll.set, height=12
    )
    cart_scroll.config(command=cart_tree.yview)

    cart_tree.heading("id", text="ID")
    cart_tree.heading("title", text="Item Name")
    cart_tree.heading("condition", text="Condition")
    cart_tree.heading("unit_price", text="Price")

    cart_tree.column("id", width=70, anchor="center")
    cart_tree.column("title", width=170, anchor="w")
    cart_tree.column("condition", width=90, anchor="center")
    cart_tree.column("unit_price", width=100, anchor="e")

    cart_tree.pack(fill="both", expand=True)

    empty_cart_btn = tk.Button(
        right_frame, text="Empty Cart", font=("Arial", 9, "bold"),
        bg="#dc3545", fg="white", padx=10, pady=5, relief="flat", cursor="hand2",
        command=lambda: empty_cart()
    )
    empty_cart_btn.pack(anchor="e", pady=5)

    # Summary and sales tax frames
    summary_frame = tk.LabelFrame(
        right_frame, text=" Payment Summary ", font=("Arial", 10, "bold"), 
        fg="white", bg="#121212", bd=2, relief="groove", padx=15, pady=10
    )
    summary_frame.pack(fill="x", pady=5)

    tax_lbl = tk.Label(summary_frame, text="Estimated Tax (7%): $0.00", font=("Arial", 10), fg="#cccccc", bg="#121212")
    tax_lbl.pack(anchor="w", pady=2)

    final_total_lbl = tk.Label(summary_frame, text="Total Due: $0.00", font=("Arial", 13, "bold"), fg="#006699", bg="#121212")
    final_total_lbl.pack(anchor="w", pady=(5, 2))

    # Complete purchase button things
    complete_btn = tk.Button(
        right_frame, text="Complete Purchase and Update Inventory", font=("Arial", 11, "bold"),
        bg="#006699", fg="white", pady=10, relief="flat", cursor="hand2",
        command=lambda: complete_purchase()
    )
    complete_btn.pack(fill="x", pady=(10, 5))

    # Close window button
    close_btn = tk.Button(
        right_frame, text="Close Window", font=("Arial", 10, "bold"),
        bg="#5a6268", fg="white", pady=8, relief="flat", cursor="hand2",
        command=purchase_win.destroy
    )
    close_btn.pack(fill="x", pady=(0, 5))

    # Cart data structure
    purchase_cart = []

    def populate_catalog(filter_text=""):
        for row in cat_tree.get_children():
            cat_tree.delete(row)
        
        for item_id, item_obj in inventory_manager.inventory.items():
            search_str = f"{item_id} {item_obj.title} {item_obj.platform} {item_obj.category}".lower()
            if filter_text.lower() in search_str:
                retail_new = item_obj.new_price if hasattr(item_obj, "new_price") else 0.0
                cat_tree.insert("", "end", values=(
                    item_obj.item_id,
                    item_obj.title,
                    item_obj.platform,
                    f"${retail_new:.2f}"
                ), tags=(item_id,))

    def on_catalog_select(event):
        selected = cat_tree.selection()
        if not selected:
            return
        item_values = cat_tree.item(selected[0], "values")
        item_id = item_values[0]

        if item_id.startswith("G"):
            # Games: New or Used (No Refurbished/Damaged for games)
            condition_combo["values"] = ["New", "Used"]
            if condition_var.get() not in ["New", "Used"]:
                condition_var.set("New")
        else:
            # Hardware/Accessories: New, Like New, Refurbished, Used
            condition_combo["values"] = ["New", "Like New", "Refurbished", "Used"]

    cat_tree.bind("<<TreeviewSelect>>", on_catalog_select)

    def update_totals():
        subtotal = sum(item["unit_price"] for item in purchase_cart)
        tax = round(subtotal * 0.07, 2)
        total = round(subtotal + tax, 2)

        tax_lbl.config(text=f"Estimated Tax (7%): ${tax:.2f}")
        final_total_lbl.config(text=f"Total Due: ${total:.2f}")

    def add_to_purchase_cart():
        selected = cat_tree.selection()
        if not selected:
            messagebox.showwarning("Selection Warning", "Please select an item from the catalog to purchase.")
            return
        
        item_values = cat_tree.item(selected[0], "values")
        item_id = item_values[0]
        item_obj = inventory_manager.inventory.get(item_id)
        condition = condition_var.get()

        if item_obj:
            # Count how many of this item and condition are already in the cart
            cart_count = sum(1 for item in purchase_cart if item["item_id"] == item_id and item["condition"] == condition)
            current_stock = inventory_manager.check_stock(item_id, condition)

            if cart_count >= current_stock:
                messagebox.showerror("Stock Limit Reached", f"Cannot add more. Only {current_stock} available in stock for '{condition}' condition.")
                return

            unit_price = item_obj.get_retail_price(condition) if hasattr(item_obj, "get_retail_price") else item_obj.new_price

            purchase_cart.append({
                "item_id": item_id,
                "title": item_obj.title,
                "condition": condition,
                "unit_price": unit_price
            })

            cart_tree.insert("", "end", values=(
                item_id,
                item_obj.title,
                condition,
                f"${unit_price:.2f}"
            ))
            update_totals()

    def empty_cart():
        """Clears all items from the purchase cart and resets totals."""
        purchase_cart.clear()
        for row in cart_tree.get_children():
            cart_tree.delete(row)
        update_totals()

    def complete_purchase():
        if not purchase_cart:
            messagebox.showwarning("Empty Cart", "Shopping cart is empty. Add items before completing.")
            return

        # Deducts from inventory after completing
        for entry in purchase_cart:
            inventory_manager.update_stock(entry["item_id"], entry["condition"], -1)

        subtotal = sum(item["unit_price"] for item in purchase_cart)
        tax = round(subtotal * 0.07, 2)
        total = round(subtotal + tax, 2)

        messagebox.showinfo(
            "Purchase Complete", 
            f"Transaction successfully processed!\nTotal Items: {len(purchase_cart)}\nTotal Due: ${total:.2f}\n\nInventory stock has been updated."
        )
        purchase_win.destroy()

    search_var.trace("w", lambda *args: populate_catalog(search_var.get()))
    populate_catalog()