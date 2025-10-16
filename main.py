from pyscript import document, display

# Menu and prices
menu_prices = {
    "Cinnamoroll Cake": 499.00,
    "Banana Cake": 50.00,
    "Chicken Tenders": 150.00,
    "Iced Tea": 30.00,
    "Cinnamoroll Latte": 150.00
}

# Function to create order
def create_order(event=None):
    selected_items = []
    total = 0

    # Loop through all checkboxes
    checkboxes = document.querySelectorAll("input[type='checkbox']")
    for checkbox in checkboxes:
        if checkbox.checked:
            item = checkbox.value
            selected_items.append(item)
            total += menu_prices[item]

    # Get customer details
    name = document.querySelector("#name").value
    address = document.querySelector("#address").value
    contact = document.querySelector("#contact").value

    # Display summary
    if not name or not address or not contact:
        display("⚠️ Please fill in all customer details.", target="output")
        return

    if not selected_items:
        display("⚠️ Please select at least one item.", target="output")
        return

    summary = f"""
    Order for: {name}
    Address: {address}
    Contact number: {contact}
    Ordered items: {', '.join(selected_items)}
    Total: ₱ {total:.2f}
    """
    display(summary.strip(), target="output")


# Function to clear form
def refresh(event=None):
    # Uncheck all checkboxes
    checkboxes = document.querySelectorAll("input[type='checkbox']")
    for checkbox in checkboxes:
        checkbox.checked = False

    # Clear text fields
    document.querySelector("#name").value = ""
    document.querySelector("#address").value = ""
    document.querySelector("#contact").value = ""

    # Clear output box
    display("", target="output")