""" sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def receipt(orders):
    rreceipt = {}
    total = 0
    for order in orders:
        if order["name"] in rreceipt:
            rreceipt[order["name"]]["amount"] += 1
        else:
            rreceipt[order["name"]] = {
                "price": order["price"],
                "amount": 1
            }
    for order, value in rreceipt.items():
        price = value["price"] * value["amount"]
        print(order, value["amount"], price)
        total += price
    print(f"your total is ${total}")
receipt(sushi_orders) """

wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}

for dept, docs in wards.items():
    for doc in docs:
        if doc not in staff:
            staff[doc] = [dept]
        else:
            staff[doc].append(dept)


print(staff["Bob"])
