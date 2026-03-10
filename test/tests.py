def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
        return total


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {

           "name": "nike", "price": 5
         
         }
    ]

    print(calculate_total(products))
    assert calculate_total(products) == 5

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    