#Solution for problem:
#https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

def recursive_add(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        sum1 = recursive_add(arr[:int(len(arr)/2)])
        sum2 = recursive_add(arr[int(len(arr)/2):])
        total_sum = sum1 + sum2

        if total_sum > sum1 or total_sum > sum2:
            return total_sum
        elif sum1 > sum2:
            return sum1
        else:
            return sum2
        

tests_input = int(input())

length_input, array_input = ([] for i in range(2))

for i in range(tests_input):
    length_input.append(int(input()))
    array_input.append(list(map(int, input().split())))

for ind in range(tests_input):
    print(recursive_add(array_input[ind]))



    
