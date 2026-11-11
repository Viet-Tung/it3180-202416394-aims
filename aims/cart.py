class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= 20:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print(f"The disc '{dvd.title}' has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        print("***********************CART***********************")
        print("Ordered Items:")
        for i, dvd in enumerate(self.items, 1):
            print(f"{i}. DVD - {dvd.title} - {dvd.category} - {dvd.director} - {dvd.cost} $")
        print(f"Total cost: {self.total_cost()} $")
        print("***************************************************")
    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Invalid discount percent")
        return self.total_cost() * (1 - percent / 100)