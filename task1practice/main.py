import json

FILE_NAME = "items.json"

def load_items():
    """Loads data from the JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_items(items):
    """Saves data to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)

def report_found_item():
    """Adds a newly found item to the database."""
    item_name = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter found location: ")
    date_found = input("Enter date (YYYY-MM-DD): ")

    items = load_items()
    item_id = len(items) + 1

    new_item = {
        "id": item_id,
        "name": item_name,
        "category": category,
        "location": location,
        "date_found": date_found,
        "claimed": False
    }

    items.append(new_item)
    save_items(items)
    print("✅ Item added to the system!")

def search_items():
    """Searches for an item by name, category, or location."""
    search_term = input("Enter item name, category, or found location: ").lower()
    items = load_items()

    found_items = [item for item in items if 
                   search_term in item["name"].lower() or 
                   search_term in item["category"].lower() or 
                   search_term in item["location"].lower()]

    if found_items:
        for item in found_items:
            print(f"🔹 {item['name']} found at {item['location']} ({item['date_found']})")
    else:
        print("❌ No items found.")

def claim_item():
    """Allows the user to claim their lost item by ID."""
    try:
        item_id = int(input("Enter the item ID you want to claim: "))
    except ValueError:
        print("❌ Error: Please enter a number!")
        return

    items = load_items()
    for item in items:
        if item["id"] == item_id and not item["claimed"]:
            item["claimed"] = True
            save_items(items)
            print("✅ Item marked as claimed!")
            return

    print("❌ Item already claimed or not found.")

def main():
    while True:
        print("\n📌 Lost and Found Office")
        print("1. Report a found item")
        print("2. Search for a lost item")
        print("3. View all unclaimed items")
        print("4. Claim an item")
        print("5. Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            report_found_item()
        elif choice == "2":
            search_items()
        elif choice == "3":
            items = load_items()
            for item in items:
                if not item["claimed"]:
                    print(f"🔹 {item['name']} found at {item['location']} ({item['date_found']})")
        elif choice == "4":
            claim_item()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid input. Please try again.")

if __name__ == "__main__":
    main()
