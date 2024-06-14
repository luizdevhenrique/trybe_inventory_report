from datetime import datetime
from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing = min(
            datetime.strptime(product.manufacturing_date, '%Y-%m-%d')
            for inventory in self.inventories
            for product in inventory.data
        )

        closest_expiration_date = min(
            datetime.strptime(product.expiration_date, '%Y-%m-%d')
            for inventory in self.inventories
            for product in inventory.data if datetime.strptime(
                product.expiration_date, '%Y-%m-%d')
            > datetime.now()
        )

        inventory_count = {}

        for inventory in self.inventories:
            for product in inventory.data:
                if product.company_name in inventory_count:
                    inventory_count[product.company_name] += 1
                else:
                    inventory_count[product.company_name] = 1

        company_with_largest_inventory = max(
            inventory_count, key=inventory_count.get
        )

        return (
            f"Oldest manufacturing date: {oldest_manufacturing}\n "
            f"Closest expiration date: {closest_expiration_date}\n "
            f"Company with the largest "
            f"inventory: {company_with_largest_inventory}"
        )
