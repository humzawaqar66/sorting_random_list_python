import random

def rand_lst(start, end, num):
    rand_l = []
    for i in range(num):
        rand_l.append(random.randint(start, end))
    return rand_l

def bub_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def search_number(arr, search_num):
    search_result = search_num in arr
    if search_result:
        print("The search number", search_num, "is in the list.")
    else:
        print("The search number", search_num, "is not in the list.")
    return search_result

print("Welcome to List Sorting and Searching Program!")

num = int(input("Enter the length of the list: "))
start = int(input("Enter the minimum value for random numbers: "))
end = int(input("Enter the maximum value for random numbers: "))

generated_list = rand_lst(start, end, num)
print("Generated list:", generated_list)

sorted_list = bub_sort(generated_list)
print("Sorted list:", sorted_list)

search_num = int(input("Enter the target number to search for in the list: "))
search_result = search_number(sorted_list, search_num)

#print("Search result:", search_result)

print("Thank you for using List Sorting and Searching Program!")