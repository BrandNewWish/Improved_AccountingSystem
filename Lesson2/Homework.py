max_items = int(input("Provide the number of items to process"))

current_package_weight = 0
package_sent = 0
total_weight = 0
max_unused_package = None
unused_capacity_per_package =[]
item_count = 0
max_unused_capacity = 0
worst_package = 0



while item_count < max_items:
    current_weight = int(input("Enter the weight of the item (1 - 10 kg), or 0 to quit"))
    if current_weight == 0:
            print("Terminating the program")
            break
    elif 1 <= current_weight <= 10:
        print("The weight of the item is {} kg".format(current_weight))

        if current_package_weight + current_weight > 20:
            package_sent += 1
            total_weight += current_package_weight
            unused_capacity_per_package.append(20 - current_package_weight)
            print("Package {} sent with {} in kg" .format(package_sent, current_package_weight))
            current_package_weight = current_weight
        else:
            current_package_weight += current_weight
        item_count += 1
    else:
        print("Invalid input")
        continue

if current_package_weight > 0:
    package_sent += 1
    total_weight += current_package_weight
    unused_capacity_per_package.append(20 - current_package_weight)
    print("Package {} sent with {} kg".format(package_sent, current_package_weight))

total_unused_capacity = sum(unused_capacity_per_package)
max_unused_capacity = max(unused_capacity_per_package)
worst_package = unused_capacity_per_package.index(max_unused_capacity) + 1


print("Number of packages sent {}, total weight of packages sent {}, total unused capacity {}, Package with the most unused capacity {} in kg {}".format(package_sent, total_weight, total_unused_capacity, worst_package, max_unused_capacity))



