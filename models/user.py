nums = [2,4,1,5,3,-5]
print(f'len of nums is {len(nums)}')
prefixes = [0] * (len(nums)+1)
print(prefixes)
prefixes[0] = 0
#for i, val in enumerate(nums, start = 1):  отличный метод, если нужен индекс и значение сразу
