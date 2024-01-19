       #TASK

def calculate_discount(cart, discounts):
    # this is to Check for "flat_10_discount"
    if cart["total"] > 200:
        return discounts["flat_10_discount"]

    # this is to Check for "bulk_5_discount"
    for product in cart["products"]:
        if product["quantity"] > 10:
            return discounts["bulk_5_discount"]

    # this is to Check for "bulk_10_discount"
    if cart["total_quantity"] > 20:
        return discounts["bulk_10_discount"]

    # this is to Check for "tiered_50_discount"
    if cart["total_quantity"] > 30:
        for product in cart["products"]:
            if product["quantity"] > 15:
                return discounts["tiered_50_discount"]

    # if there is No applicable discount
    return None


def main():
    # this is for Product prices
    prices = {"Product A": 20, "Product B": 40, "Product C": 50}

    # this is for Discount rules
    discounts = {
        "flat_10_discount": 10,
        "bulk_5_discount": 5,
        "bulk_10_discount": 10,
        "tiered_50_discount": 50,
    }

    # To Get user input for product quantities and gift wrapping
    cart = {"products": [], "total_quantity": 0, "total": 0}
    for product_name, price in prices.items():
        quantity = int(input(f"Enter quantity for {product_name}: "))
        is_gift_wrapped = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == "yes"

        product_total = quantity * price
        cart["products"].append({"name": product_name, "quantity": quantity, "total": product_total})
        cart["total_quantity"] += quantity
        cart["total"] += product_total

        if is_gift_wrapped:
            cart["total"] += quantity  # Gift wrap fee of $1 per unit

    # to Calculate discount
    discount_name = "No discount"
    discount_amount = 0
    applied_discount = calculate_discount(cart, discounts)
    if applied_discount is not None:
        discount_name = applied_discount[0]
        discount_amount = applied_discount[1]
        cart["total"] -= (discount_amount / 100) * cart["total"]

    # to Calculate shipping fee
    shipping_fee = (cart["total_quantity"] // 10) * 5

    # Output details
    print("\nDetails:")
    for product in cart["products"]:
        print(f"{product['name']} - Quantity: {product['quantity']} - Total: ${product['total']}")

    print(f"\nSubtotal: ${cart['total']}")

    print(f"\nDiscount Applied: {discount_name} - Discount Amount: ${discount_amount}")

    print(f"\nShipping Fee: ${shipping_fee}")
    
    print("\nTotal: ${:.2f}".format(cart['total'] + shipping_fee))


if __name__ == "__main__":
    main()
