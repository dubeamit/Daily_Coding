# FIND THE MOST FREQUENT ELEMENT IN A LIST/ARRAY
def most_frequent(arr):
    dictionary = {} # stores key-value pair
    frequent_item = 0
    for i in arr:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

        if dictionary[i] > frequent_item:
            frequent_item = i
    if dictionary[frequent_item] == 1:
            return None
    return frequent_item

print('The most frequently occuring item is',most_frequent([5,7,9,5,2,7,5,0,5]))
print('The most frequently occuring item is',most_frequent([1,2,3,4,5])) #NO FREQUENT ITEM HENCE RETURN NONE