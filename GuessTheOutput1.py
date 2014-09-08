
#Guess the output of the following:

aList = [2,3,5]
for num in aList:
    if num % 2 == 0:
        aList.append(sum(aList))
    if len(aList) > 35:
        break
        
print [x/10 for x in aList[3:]]



'''
Answer:
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 
65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 
33554432, 67108864, 134217728, 268435456L, 536870912L, 1073741824L, 2147483648L,
4294967296L]

'''
