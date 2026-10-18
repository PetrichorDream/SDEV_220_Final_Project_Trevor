### How to Run the Application

### Option 1: Double-Click Executable (Recommended)
1. Download this repository and extract the zip.
2. Locate the file named **`GameStop Employee Terminal - RUN THIS.exe`** in the root folder.
3. Double click the file to launch the application instantly with zero configuration or command lines required.

### Option 2: Run from Source Code (Python)
If you prefer running the raw source code:
1. Ensure Python and `tkinter` are installed on your system. (tkinter should be built into Python)
2. Open your windows terminal using win + r, then type cmd.
3. Type "cd " and open file explorer.
4. Drag the gamestop_project folder to the right of "cd ".
5. Type "python main.py"



Client: GameStop
Purpose: A desktop employee terminal system designed to track store inventory, process retail purchases, and handle trade-in valuations for video games, consoles, and accessories
Scope: Features a local database of pre-set items across multiple categories. Trade-in values adjust dynamically based on item condition (New, Like New, Refurbished, Used, Damaged) and payout method (Cash vs. Store Credit with a +15% bonus). Includes a live inventory checker and cart stock validation to prevent overselling. (I was having trouble figuring out how to keep stock saved after closing the terminal and couldn't find an easy way. As such all invntory starts at preset values for testing but does carry between trade-in's and purchases during the same session. So, as long as you don't close the application, stock is dynamic.)



My application used a modular object-oriented architecture to maintain clean code and connectivity needed for dynamic updating inventory
classes.py: Houses the core business logic classes:
GameItem: Manages item attributes, stock tracking dictionaries, and condition-based pricing/trade-in multipliers.
TradeEvaluator: Computes the 15% store credit bonus.
InventoryManager: Controls master catalog lookups and stock updates.
dataset.py: Initializes the store catalog with pre-set games, consoles, and accessories.
main.py: Manages the main dashboard window and navigation routing.
inventory_window.py: Renders live store catalog searches and condition-based stock breakdowns.
trade_window.py: Handles trade-in condition restrictions, cart management, and store credit calculations.
purchase_window.py: Manages retail cart validation, out-of-stock safety limits, and tax calculations.
