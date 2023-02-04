def push(arr, num):
    arr.append(num)
    return arr


def maximum(arr):
    if arr:
        print(max(arr))


def minimum(arr):
    if arr:
        print(min(arr))


def delete(arr):
    if arr:
        arr.pop()
    return arr


number = int(input())
stack = []
for _ in range(number):
    command = [int(x) for x in input().split()]
    operation = command[0]
    if operation == 1:
        cur_num = command[1]
        stack = push(stack, cur_num)
    elif operation == 2:
        stack = delete(stack)
    elif operation == 3:
        maximum(stack)
    else:
        minimum(stack)
rev_stack = stack[::-1]
print(", ".join([str(y) for y in rev_stack]))