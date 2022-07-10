def main():
    PHOTO_PRICES = {
        10: 0.18,
        11: 0.34,
        13: 0.50,
        20: 3.56
    }

    SHIPPING_COSTS = 4.95

    total = 0

    order_sum = {}

    latest_order = input("Enter a photo size and the number of photos separated by a comma. Stop with an empty line.\n")
    while latest_order != "":
        order_data = latest_order.split(",")
        if len(order_data) != 2:
            print("Invalid input. Enter exactly two integers separated by a comma.")
        elif int(order_data[0]) not in PHOTO_PRICES:
            print("Wrong size. Choose one of the following sizes: 10, 11, 13 and 20 cm.")
        else:
            if int(order_data[0]) in order_sum:
                order_sum[int(order_data[0])] += int(order_data[1])
            else:
                order_sum[int(order_data[0])] = int(order_data[1])
            total += int(order_data[1]) * PHOTO_PRICES[int(order_data[0])]
            print(f"{order_data[1]} photo prints of size {order_data[0]} cm were added into your order.")
        latest_order = input("Enter a photo size and the number of photos separated by a comma. Stop with an empty "
                             "line.\n")

    print("ORDER:\nSize  | Count\n-------------")
    for key in order_sum:
        print(f"{key} cm | {order_sum[key]}")
    print(f"\n     The price: {total:5.2f} eur")
    if total > 100:
        SHIPPING_COSTS = 0
    print(f"Shipping costs: {SHIPPING_COSTS:5.2f} eur")
    print(f"   Total price: {total + SHIPPING_COSTS:5.2f} eur")


main()
