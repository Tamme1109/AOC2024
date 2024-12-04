def readFile():
    with open ("question2test.txt","r") as file:
      data = file.read()
    return data
    
    
data = readFile()
str_list = data.split("\n")

def all_increase(lst):
    bool = False
    for i in range(len(lst)):
        if((i + 1) == len(lst)):
            break
        diff = int(lst[i]) - int(lst[i+1])
        if(diff < 0 and abs(diff) >= 1 and abs(diff) <= 3):
            bool = True
        else:
            bool = False
            break
    return bool


def all_decrease(lst):
    bool = False
    for i in range(len(lst)):
        if((i + 1) == len(lst)):
            break
        diff = (int(lst[i]) - int(lst[i+1]))
        if( diff > 0 and abs(diff) >= 1 and abs(diff) <= 3):
            bool = True
        else:
            bool = False
            break
    return bool

def is_safe(arr):
    if(all_increase(arr) or all_decrease(arr)):
        return 1
    else:
        return 0
    
    
    
def check_safe():
    count = 0
    for str in str_list:
        arr = str.split()
        count += is_safe((arr))
        print(arr)
    return count


#----------------------------PART 2------------------------------#


def dampener(list):
    for i in range(len(list)):
        if((i + 2) == len(list)):
            break
        diff = (int(list[i]) - int(list[i+1]))
        diff2 = (int(list[i]) - int(list[i+2]))
        
        slope = int(list[0]) - int(list[-1])
        if slope > 0:
            if not(diff > 0 and abs(diff) >= 1 and abs(diff) <= 3):
                if (diff2 > 0 and abs(diff) >= 1 and abs(diff) <= 3):
                    list.pop(i+1)
                    break
                else:
                    list.pop(i)
                    break
        else:
            if (diff2 < 0 and abs(diff) >= 1 and abs(diff) <= 3):
                    list.pop(i+1)
                    break
            else:
                list.pop(i)
                break
    return list
    
def check_safe_new():
    count = 0
    for str in str_list:
        arr = str.split()
        count += is_safe(dampener(arr))
        print(arr)
    return count

print(check_safe_new())

arr = [1,2,4,8,0]
arr1 = [1,2,7,8,9]
print(dampener(arr1))