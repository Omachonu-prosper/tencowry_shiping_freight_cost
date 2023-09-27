def shipping_freight_cost(products, shipment_price):
    """
    Function to address "Shipping /Freight cost"

    Input payload:
    [
        {"weight":"", "quantity":"2", "naira_price": "23800"},
        {"weight":"3", "quantity":"1", "naira_price": "3200"},
        {"weight":"3", "quantity":"2", "naira_price": "2100"}
    ]

    Workflow:
    - Get the product with the highest weight
    - Reduce the quantity of that product by 1
        We reduce the quatnity of the highest product by one so
        when we multiply by 2 we wouldnt be adding the max weight product
        in the calculations again
    - Calculate the total weight
    - Compute the total cost (total weight * shipment price)

    Output:
    total_cost -> the cost of shipment the customer is to pay
    """
    max_weight_product = {
        'weight': 0,
        'index_in_products': None
    }
    for x, product in enumerate(products):
        try:
            weight = float(product['weight'])

            if weight < 1:
                weight = 1
        except:
            product['weight'] = 1
            weight = 1

        # The workflow section of the docstring explains this section in more details
        if weight >= max_weight_product['weight']:
            max_weight_product['weight'] = weight
            index = max_weight_product['index_in_products']
            if index is not None:
                products[index]['quantity'] = int(products[index]['quantity']) + 1
            
            product['quantity'] = int(product['quantity']) - 1
            max_weight_product['index_in_products'] = x

    total_weight = max_weight_product['weight'] * 2
    for product in products:
        total_weight += float(product['weight']) * int(product['quantity'])
        
    total_cost = shipment_price * total_weight
    return total_cost


if __name__ == '__main__':
    products1 = [
        {"weight":"1", "quantity":"2", "naira_price": "23800"},
        {"weight":"3", "quantity":"1", "naira_price": "3200"},
        {"weight":"3", "quantity":"2", "naira_price": "2100"}
    ]

    products2 = [
        {"weight":"0.5", "quantity":"2", "naira_price": "2100"},
        {"weight":"1", "quantity":"3", "naira_price": "3200"}
    ]

    products3 = [
        {"weight":"1", "quantity":"3", "naira_price": "3200"}
    ]

    products4 = [
        {"weight":"0.5", "quantity":"3", "naira_price": "3200"}
    ]
    
    print(shipping_freight_cost(products1, 10))
    print(shipping_freight_cost(products2, 10))
    print(shipping_freight_cost(products3, 10))
    print(shipping_freight_cost(products4, 10))