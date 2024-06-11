from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
            "1",
            "product",
            "company",
            "01/01/2021",
            "01/01/2022",
            "123",
            "keep it cool",
        )
    assert product.id == "1"
    assert product.product_name == "product"
    assert product.company_name == "company"
    assert product.manufacturing_date == "01/01/2021"
    assert product.expiration_date == "01/01/2022"
    assert product.serial_number == "123"
    assert product.storage_instructions == "keep it cool"
