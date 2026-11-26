#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 100:
            print("Not valid discount")
            value = 0
        self._discount = value

    def add_item(self, item, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
            return

        if self.discount:
            self.total -= self.total * (self.discount / 100)

        if float(self.total).is_integer():
            display_total = str(int(self.total))
        else:
            display_total = f"{self.total:.2f}".rstrip("0").rstrip(".")
        print(f"After the discount, the total comes to ${display_total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()
        quantity = transaction["quantity"]
        transaction_total = transaction["price"] * quantity
        self.total = round(self.total - transaction_total, 10)

        for _ in range(quantity):
            if transaction["item"] in self.items:
                item_index = len(self.items) - 1 - self.items[::-1].index(transaction["item"])
                self.items.pop(item_index)
