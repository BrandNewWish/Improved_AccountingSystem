import csv

def save_balance(company):
    with open("balance.csv", "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["balance"])
        writer.writerow([company.balance])

def save_warehouse(company):
    with open("warehouse.csv", "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["product", "price", "quantity"])
        for product, info in company.warehouse.items():
            writer.writerow([product, info["price"], info["quantity"]])


def save_operations(company):
    with open("operations.csv", "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["type", "product", "quantity", "price"])
        for op in company.operations:
            writer.writerow(list(op))