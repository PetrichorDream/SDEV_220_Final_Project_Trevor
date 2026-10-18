from classes import GameItem, InventoryManager

def load_initial_inventory() -> InventoryManager:
    manager = InventoryManager()

    # Helper function to define initial stock counts easily
    def game_stock():
        return {"New": 3, "Used": 2}

    def hardware_stock():
        return {"New": 3, "Like New": 2, "Refurbished": 1, "Used": 2, "Damaged": 0}


    # Games catalog (G001 - G049)
    games_data = [
        # Minecraft
        ("G001", "Minecraft", "Switch", "Sandbox", 29.99, 8.00),
        ("G002", "Minecraft", "Xbox", "Sandbox", 29.99, 8.00),
        ("G003", "Minecraft", "PlayStation", "Sandbox", 29.99, 8.00),
        # Zelda
        ("G004", "The Legend of Zelda: Tears of the Kingdom", "Switch", "Adventure", 69.99, 25.00),
        ("G005", "The Legend of Zelda: Breath of the Wild", "Switch", "Adventure", 59.99, 18.00),
        ("G006", "The Legend of Zelda: Ocarina of Time", "Switch", "Adventure", 59.99, 30.00),
        # Mario and Racing
        ("G007", "Super Mario Odyssey", "Switch", "Platformer", 59.99, 15.00),
        ("G008", "Super Mario Bros. Wonder", "Switch", "Platformer", 59.99, 20.00),
        ("G009", "Mario Kart 8 Deluxe", "Switch", "Racing", 59.99, 18.00),
        # Fire Emblem
        ("G010", "Fire Emblem Engage", "Switch", "RPG", 59.99, 14.00),
        ("G011", "Fire Emblem: Three Houses", "Switch", "RPG", 59.99, 15.00),
        # Red Dead Redemption 2
        ("G012", "Red Dead Redemption 2", "PlayStation", "Action", 59.99, 5.00),
        ("G013", "Red Dead Redemption 2", "Xbox", "Action", 59.99, 5.00),
        # PlayStation Exclusives
        ("G016", "God of War Ragnarok", "PlayStation", "Action", 69.99, 12.00),
        # Elden Ring
        ("G018", "Elden Ring", "PlayStation", "RPG", 59.99, 12.00),
        ("G019", "Elden Ring", "Xbox", "RPG", 59.99, 12.00),
        # Last of Us
        ("G020", "The Last of Us Part II", "PlayStation", "Action", 39.99, 6.00),
        # Switch Hits
        ("G021", "Super Smash Bros. Ultimate", "Switch", "Fighting", 59.99, 20.00),
        ("G022", "Metroid Dread", "Switch", "Platformer", 59.99, 15.00),
        ("G023", "Pokémon Legends: Arceus", "Switch", "Adventure", 59.99, 18.00),
        # Resident Evil 4
        ("G024", "Resident Evil 4 (Remake)", "PlayStation", "Horror", 59.99, 10.00),
        ("G025", "Resident Evil 4 (Remake)", "Xbox", "Horror", 59.99, 10.00),
        # Cyberpunk 2077
        ("G026", "Cyberpunk 2077: Ultimate Edition", "PlayStation", "RPG", 59.99, 12.00),
        ("G027", "Cyberpunk 2077: Ultimate Edition", "Xbox", "RPG", 59.99, 12.00),
        # Other Exclusives
        ("G028", "Horizon Forbidden West", "PlayStation", "Adventure", 69.99, 8.00),
        ("G029", "Halo Infinite", "Xbox", "Action", 59.99, 6.00),
        ("G030", "Forza Horizon 5", "Xbox", "Racing", 59.99, 8.00),
        ("G031", "Starfield", "Xbox", "RPG", 69.99, 8.00),
        # Monster Hunter
        ("G032", "Monster Hunter: World", "PlayStation", "Action", 19.99, 2.00),
        ("G033", "Monster Hunter: World", "Xbox", "Action", 19.99, 2.00),
        # Persona 5 Royal
        ("G034", "Persona 5 Royal", "PlayStation", "RPG", 29.99, 4.00),
        ("G035", "Persona 5 Royal", "Xbox", "RPG", 29.99, 4.00),
        ("G036", "Persona 5 Royal", "Switch", "RPG", 29.99, 4.00),
        # Persona 3 Reload
        ("G037", "Persona 3 Reload", "PlayStation", "RPG", 19.99, 3.00),
        ("G038", "Persona 3 Reload", "Xbox", "RPG", 19.99, 3.00),
        ("G039", "Persona 3 Reload", "Switch", "RPG", 19.99, 3.00),
        # Assassin's Creed
        ("G040", "Assassin's Creed Valhalla", "PlayStation", "RPG", 59.99, 4.00),
        ("G041", "Assassin's Creed Valhalla", "Xbox", "RPG", 59.99, 4.00),
        # Final Fantasy and Kirby
        ("G042", "Final Fantasy VII Rebirth", "PlayStation", "Action RPG", 69.99, 18.00),
        ("G043", "Kirby and the Forgotten Land", "Switch", "Action-Platformer", 59.99, 18.00),
        # Hogwarts Legacy
        ("G044", "Hogwarts Legacy", "PlayStation", "Action RPG", 49.99, 5.00),
        ("G045", "Hogwarts Legacy", "Xbox", "Action RPG", 49.99, 5.00),
        ("G046", "Hogwarts Legacy", "Switch", "Action RPG", 49.99, 5.00),
        # Terraria
        ("G047", "Terraria", "PlayStation", "Adventure", 19.99, 4.00),
        ("G048", "Terraria", "Xbox", "Adventure", 19.99, 4.00),
        ("G049", "Terraria", "Switch", "Adventure", 19.99, 4.00),
    ]

    for item_id, title, platform, category, new_price, trade_val in games_data:
        item = GameItem(item_id, title, platform, category, new_price, trade_val, game_stock())
        manager.add_item_to_catalog(item)


    # Consoles catalog (C001 - C013)
    consoles_data = [
        ("C001", "PlayStation 5 Pro", "PlayStation", "Console", 999.99, 680.00),
        ("C002", "PlayStation 5 Disc Edition", "PlayStation", "Console", 499.99, 280.00),
        ("C003", "PlayStation 5 Digital Edition", "PlayStation", "Console", 449.99, 250.00),
        ("C004", "PlayStation 4 Pro (1TB)", "Sony PlayStation 4", "Console", 249.99, 65.00),
        ("C005", "PlayStation 4", "PlayStation", "Console", 199.99, 45.00),
        ("C006", "Xbox Series X", "Xbox", "Console", 499.99, 280.00),
        ("C007", "Xbox Series S", "Xbox", "Console", 299.99, 130.00),
        ("C008", "Xbox One X", "Microsoft Xbox One", "Console", 249.99, 55.00),
        ("C009", "Xbox One S", "Xbox", "Console", 199.99, 45.00),
        ("C010", "Nintendo Switch 2", "Nintendo", "Handheld Console", 449.99, 275.00),
        ("C011", "Nintendo Switch (OLED Model)", "Nintendo", "Handheld Console", 349.99, 175.00),
        ("C012", "Nintendo Switch", "Nintendo", "Handheld Console", 299.99, 125.00),
        ("C013", "Nintendo Switch Lite", "Nintendo", "Handheld Console", 199.99, 90.00),
    ]

    for item_id, title, platform, category, new_price, trade_val in consoles_data:
        item = GameItem(item_id, title, platform, category, new_price, trade_val, hardware_stock())
        manager.add_item_to_catalog(item)


    # Controllers (A001 - A008)
    accessories_data = [
        ("A001", "DualSense Wireless Controller", "PlayStation", "Controller", 69.99, 20.00),
        ("A002", "DualSense Edge Wireless Controller", "PlayStation", "Controller", 199.99, 70.00),
        ("A003", "DualShock 4 Wireless Controller", "PlayStation", "Controller", 39.99, 8.00),
        ("A004", "Xbox Wireless Controller", "Xbox", "Controller", 59.99, 20.00),
        ("A005", "Xbox Elite Wireless Controller Series 2", "Xbox", "Controller", 179.99, 50.00),
        ("A006", "Xbox Elite Wireless Controller Series 2 - Core", "Xbox", "Controller", 129.99, 35.00),
        ("A007", "Nintendo Switch Joy-Con Pair", "Nintendo", "Controller", 79.99, 25.00),
        ("A008", "Nintendo Switch Pro Controller", "Nintendo", "Controller", 69.99, 25.00),
    ]

    for item_id, title, platform, category, new_price, trade_val in accessories_data:
        item = GameItem(item_id, title, platform, category, new_price, trade_val, hardware_stock())
        manager.add_item_to_catalog(item)

    return manager