class GameItem:
    def __init__(self, item_id: str, title: str, platform: str, category: str, new_price: float, base_trade_value: float, initial_stock: dict):
        self.item_id = item_id                      # Unique identifier for the item
        self.title = title                          # Title of the item (e.g., game name, console model)
        self.platform = platform                    # Platform of the item (e.g., 'PlayStation', 'Xbox', 'Nintendo')
        self.category = category                    # Category of the item (e.g., 'Fantasy', 'Adventure', 'Console', 'Accessory')
        self.new_price = new_price                  # Retail price for a brand new item
        self.base_trade_value = base_trade_value    # Standard trade-in value (Set for games, effected by condtion for hardware)
        self.stock = initial_stock                  # Dictionary tracking stock per condition tier


    def get_retail_price(self, condition: str) -> float:
        """Calculates retail price based on item type and condition."""
        if self.item_id.startswith("G"):  # Games
            if condition == "New":
                return self.new_price
            else:
                return round(self.new_price * 0.70, 2)
        else:  # Hardware
            # Hardware multipliers: Like New = 100%, Like New = 90%, Refurbihsed = 80%, Used = 75%
            if condition == "New":
                return self.new_price
            elif condition == "Like New":
                return round(self.new_price * 0.90, 2)
            elif condition == "Refurbished":
                return round(self.new_price * 0.80, 2)
            elif condition == "Used":
                return round(self.new_price * 0.75, 2) 
            return self.new_price


    def get_trade_value(self, condition: str) -> float:
        """Calculates trade-in payout value based on condition."""
        if self.item_id.startswith("G"):  # Games
            return round(self.base_trade_value, 2)
        else:  # Hardware
            # Hardware multipliers: Like New = 100%, Used = 80%, Damaged = 40%
            if condition == "Like New":
                return round(self.base_trade_value * 1.0, 2)
            elif condition == "Used":
                return round(self.base_trade_value * 0.8, 2)
            elif condition == "Damaged":
                return round(self.base_trade_value * 0.4, 2)
            return round(self.base_trade_value, 2)



class TradeEvaluator:
    CREDIT_BONUS_MULTIPLIER = 1.15 # +15% bonus for choosing in-store credit as payout

    @staticmethod
    def calculate_session_payout(subtotal: float, payout_method: str) -> float:
        """Applies the 15% store credit bonus if selected."""
        if payout_method.lower() == "credit":
            return round(subtotal * TradeEvaluator.CREDIT_BONUS_MULTIPLIER, 2)
        return round(subtotal, 2)



class InventoryManager:
    def __init__(self):
        # Master dictionary storing item_id -> GameItem object
        self.inventory = {}

    def add_item_to_catalog(self, item: GameItem):
        """Adds an item to the inventory catalog"""
        self.inventory[item.item_id] = item

    def check_stock(self, item_id: str, condition: str) -> int:
        """Returns the current quantity available for a specific condition"""
        if item_id in self.inventory:
            return self.inventory[item_id].stock.get(condition, 0)
        return 0

    def update_stock(self, item_id: str, condition: str, amount: int):
        """Increases or decreases stock for an item condition."""
        if item_id in self.inventory:
            current = self.inventory[item_id].stock.get(condition, 0)
            new_qty = max(0, current + amount)
            self.inventory[item_id].stock[condition] = new_qty