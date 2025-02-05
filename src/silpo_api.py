from typing import Literal

from pysilpo.services.product import Product as SilpoProduct
from pysilpo.services.product import SortBy


def convert_display_ratio_to_weight_in_kg(displayed_ratio: str) -> float:
    displayed_ratio = displayed_ratio.strip()
    displayed_ratio = displayed_ratio.replace(",", ".")
    if displayed_ratio.endswith("кг"):
        return float(eval(displayed_ratio[:-2]))
    if displayed_ratio.endswith("г"):
        return float(eval(displayed_ratio[:-1])) / 1000
    if displayed_ratio.endswith("мл"):
        return float(eval(displayed_ratio[:-2])) / 1000
    if displayed_ratio.endswith("л"):
        return float(eval(displayed_ratio[:-1]))
    return 0


class Product:
    def __init__(self, title: str, price: float, weight: float):
        """
        :param title: Product title
        :param price: Product price
        :param weight: Product weight in kg
        """
        self.title: str = title
        self.price: float = price
        self.weight: float = weight

    @classmethod
    def search(
        cls,
        search_query: str,
        sort_direction: Literal["desc", "asc"] = "asc",
        sort_by: SortBy = SortBy.PRICE,
    ) -> list["Product"]:
        return [
            cls(
                title=product.title,
                price=product.display_price,
                weight=convert_display_ratio_to_weight_in_kg(product.display_ratio),
            )
            for product in SilpoProduct.all(
                search=search_query, sort_by=sort_by, sort_direction=sort_direction
            )
        ]

    def __repr__(self):
        return f'<Product name: "{self.title}", price: {self.price}, weight: {self.weight}>'
