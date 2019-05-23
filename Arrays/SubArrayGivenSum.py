#Solution for problem:
#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

tests_input = int(input())

size_input, sum_input, array_input = ([None] * tests_input for i in range(3))
result = [-1] * tests_input

for i in range(tests_input):
    size_input[i], sum_input[i] = list(map(int, input().split()))
    array_input[i] = list(map(int, input().split()))
  
found = False

for ind in range(tests_input):
    size = len(array_input[ind])
    for i in range(size):
        for j in range(size):
            if i+j >= size:
                break
            s = sum(array_input[ind][i:i+j+1])
            if s == sum_input[ind]:
                found = True
                result[ind] = str(i+1) + " " + str(i+j+1)
                break
        if found:
            break
    print(result[ind])
    
    

