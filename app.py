def shipping_freight_cost(weights, shipment_price):
    """
    Function to address "Shipping /Freight cost"

    Input:
    weights -> an array of the weights of all products ordered
    shipment_price -> the price of the shipment per kg

    Output:
    total_cost -> the cost of shipment the customer is to pay
    """
    if type(weights) is not list or not shipment_price:
        return "Check the inputs given to the function"
    
    max_weight = max(weights)
    weights.remove(max_weight)

    # Round up to 1 if the weight of the heaviest product is less than 1kg
    if max_weight < 1:
        max_weight = 1

    total_weight = 2 * max_weight
    for i in weights:
        weight = 1 * i
        total_weight += weight

    total_cost = shipment_price * total_weight
    return total_cost


if __name__ == '__main__':
    print(shipping_freight_cost([1, 1, 1, 0.5, 0.5], 10)) # Based on example 1 in document
    print(shipping_freight_cost([1, 1, 1], 10)) # Based on example 2 in document
    print(shipping_freight_cost([0.5, 0.5, 0.7], 10)) # The max weight is less than one
    print(shipping_freight_cost(2, 10)) # Weights is not an array