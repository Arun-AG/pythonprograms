"""
Given a Array of Integers and Integer target ,
Find the Indices of two numbers such that they add up to the target
"""
def twosum_bruteforce(array, target):
    """
    :param array:
    :param target:
    :return: index
    :soln Time complexity: O(n^2)
    """
    for i in range(0,len(array)):
        for j in range(1,len(array)):
            if array[i] + array [j] == target :
                print(array[i],array[j],i,j)
                return i,j


if __name__ == "__main__":
    array =[1,2,4,6,7,9,11]
    target = 9
    index1,index2 = twosum_bruteforce(array,target)