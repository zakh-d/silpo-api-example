from silpo_api import Product


def search_prodects():
    print("Enter product name: ", end="")
    search_query = input()
    products = Product.search(search_query)
    print(f"Found {len(products)} products")
    for product in products:
        print(product)


if __name__ == "__main__":
    while True:
        search_prodects()

        print("Do you want to search again? (y/n): ", end="")
        answer = input()
        if answer != "y":
            break
