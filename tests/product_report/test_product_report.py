from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
            "1",
            "product",
            "company",
            "01/01/2021",
            "01/01/2022",
            "123",
            "keep it cool",
        )
    assert product.__str__() == (
        f"The product 1 - {product.product_name} "
        f"with serial number {product.serial_number} "
        f"manufactured on {product.manufacturing_date} "
        f"by the company {product.company_name} "
        f"valid until {product.expiration_date} "
        f"must be stored according to "
        f"the following instructions: {product.storage_instructions}."
    )
