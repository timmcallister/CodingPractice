#Solution for problem:
#https://practice.geeksforgeeks.org/problems/missing-number-in-array/0

tests_input = int(input())

length_input, array_input = ([] for i in range(2))

for i in range(tests_input):
    length_input.append(int(input()))
    array_input.append(list(map(int, input().split())))

for ind in range(tests_input):
    for i in range(len(array_input[ind])):
        if array_input[ind][i+1] - array_input[ind][i] == 2:
            print(array_input[ind][i] + 1)
            break
        
