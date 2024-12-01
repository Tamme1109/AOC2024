
def readFile():
    with open ("question1.txt","r") as file:
      data = file.read()
    return data
    
    
data = readFile()
array_data = data.split("\n")
#print(array_data)

new_array = []
for str in array_data:
    new_array.append(str.split())
    

arr1 = []
arr2 = []
for arr in new_array:
    strnmr = arr[0]
    arr1.append(int(strnmr))
    strnmr = arr[1]
    arr2.append(int(strnmr))
        
arr1.sort()
arr2.sort()

result = 0
for i in range (len(arr1)):
    result += abs(arr1[i] - arr2[i])

print(result)