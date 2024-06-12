from typing import Dict, Type
from abc import ABC, abstractmethod
from typing import List
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, 'r') as file:
            data = json.load(file)

        product_list = []
        for item in data:
            product = Product(
                id=item['id'],
                product_name=item['product_name'],
                company_name=item['company_name'],
                manufacturing_date=item['manufacturing_date'],
                expiration_date=item['expiration_date'],
                serial_number=item['serial_number'],
                storage_instructions=item['storage_instructions']
            )
            product_list.append(product)

        return product_list


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
