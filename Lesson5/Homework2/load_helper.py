import csv



def load_balance(filename):
    try:
        with open (filename, newline="", encoding='utf-8') as f:
            reader = csv.reader(f)
            try:
                next(reader)
                balance_line = next(reader)
                return float(balance_line[0])
            except StopIteration:
                print("Balance file is emtpy. Using default balance.")
                return 1000
    except FileNotFoundError:
        print("Balance file missing or invalid")
        return 1000

def load_warehouse(filename):
    warehouse_temp = {}
    try:
        with open(filename, newline="", encoding='utf-8') as f:
            reader = csv.reader(f)
            try:
                next(reader)
            except StopIteration:
                print("Warehouse file is empty. Starting with empty warehouse.")
                return warehouse_temp
            
            for row in reader:
                if len(row) != 3:
                    continue
                product = row [0].strip()
                price = float(row[1].strip())
                quantity = int(row[2].strip())
                warehouse_temp[product] = {"price": price,"quantity": quantity}
            return warehouse_temp

    except FileNotFoundError:
        print("Warehouse file is missing. Using empty warehouse.")
        return warehouse_temp
    except ValueError:
        print("Warehouse file contains invalid data.")
        return warehouse_temp

def load_operations(filename):
    operations_temp = []
    try:
        with open(filename, newline="", encoding='utf-8') as f:
            reader = csv.reader(f)
            try:
                next(reader)
            except StopIteration:
                print("Operations file is empty. Starting with empty history.")
                return operations_temp
            
            for row in reader:
                if not row:
                    continue
                while len(row) < 4:
                    row.append(None)

                operation_type = row[0].strip() if row[0] else None
                product = row[1].strip() if row[1] else None
                quantity = float(row[2].strip()) if row[2] else None
                price = float(row[3].strip()) if row[3] else None

                operations_temp.append((operation_type, product, quantity, price))


    except FileNotFoundError:
        print("Operations file not found. Starting with empty history.")
    except ValueError:
        print("Operations file contains invalid data.")

    return operations_temp
