from Company import Company
from Lesson5.Homework2.load_helper import load_balance, load_warehouse, load_operations
from Lesson5.Homework2.save_helper import save_balance, save_warehouse, save_operations


def main():
    my_company = Company()
    my_company.balance = load_balance("balance.csv")
    my_company.warehouse = load_warehouse("warehouse.csv")
    my_company.operations = load_operations("operations.csv")

    while True:
        print("\n--- MENU ---")
        print("1. Balance")
        print("2. Sale")
        print("3. Purchase")
        print("4. Account")
        print("5. List")
        print("6. Warehouse")
        print("7. Review")
        print("8. Exit")

        choice = input("Choose option")


        if choice == '1':
            print("Balance:", my_company.balance)

        elif choice == '2':
            product = input("Product name")
            if product not in my_company.warehouse:
                print("Product not found in warehouse!")
                continue
            price = float(input("Sale price"))
            quantity = int(input("Quantity"))
            if my_company.warehouse[product]["quantity"] < quantity:
                print("Not enough quantity in warehouse!")
                continue
            income = price * quantity
            my_company.warehouse[product]["quantity"] -= quantity
            my_company.balance += income
            my_company.operations.append(("sale", product, quantity, price))
            print("Sale completed.")
        elif choice == '3':
            product = input("Product name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            if quantity <= 0 or price < 0:
                raise ValueError("Invalid price or quantity")
            cost = price * quantity
            if my_company.balance < cost:
                print("Insufficient funds.")
                continue
            if product not in my_company.warehouse:
                my_company.warehouse[product] = {"price": price, "quantity": quantity}
            else:
                my_company.warehouse[product]["quantity"] += quantity
            my_company.balance -= cost
            my_company.operations.append(("purchase", product, quantity, price))
            print("Purchase completed.")
        elif choice == '4':
            print("Current balance:", my_company.balance)
        elif choice == '5':
            if not my_company.warehouse:
                print("Warehouse is empty.")
            else:
                for product, info in my_company.warehouse.items():
                    print(f"{product}: {info}")
        elif choice == '6':
            product = input("Product name:")
            info = my_company.warehouse.get(product)
            if info:
                print(f"{product}: {info}")
            else:
                print("Product not found.")

        elif choice == '7':
            if not my_company.operations:
                print("No operations recorded.")
            else:
                for i, op in enumerate(my_company.operations):
                    op_type, product, quantity, price = op
                    if op_type == "balance":
                        print(f"{i}: Balance change: {quantity}")
                    elif op_type == "sale":
                        print(f"{i}: Sold {quantity} x {product} at {price}")
                    elif op_type == "purchase":
                        print(f"{i}: Bought {quantity} x {product} at {price}")



        elif choice == '8':

            save_balance(my_company)
            save_warehouse(my_company)
            save_operations(my_company)
            print("Program ending.")
            break
        else:

            print("Wrong option")

main()