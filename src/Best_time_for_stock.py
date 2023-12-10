"""
Best Time to buy and sell stock
"""
def best_time_to_buy_stock(array):
    """
    :param array:
    :return:
    :Time Complexity : O(n^2)
    """
    max_profit =0;
    for price in range(0,len(array)):
        for price1 in range(1,len(array)):
            profit = (array[price1] - array[price])
            if profit > max_profit:
                max_profit = profit
    return max_profit



if __name__ =="__main__":
    array= [7,1,5,11,6,4]
    max_profit = best_time_to_buy_stock(array)
    print(max_profit)