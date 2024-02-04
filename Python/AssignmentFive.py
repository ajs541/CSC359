

def mergeSortLists(list1, list2):
    newList = []
    count = 0
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            if count == 0:
                newList.append(list1[i])
                count += 1
                i += 1
                j += 1
            elif newList.__contains__(list1[i]) == False:
                newList.append(list1[i])
                count += 1
                i += 1
                j += 1
        elif list1[i] < list2[j]:
            if newList.__contains__(list1[i]) == False:
                newList.append(list1[i])
                count += 1
                i += 1
        elif list2[j] < list1[i]:
            if newList.__contains__(list2[j]) == False:
                newList.append(list2[j])
                count += 1
                j += 1
    if i == len(list1):
        i -= 1
    if j == len(list2):
        j -= 1
    if newList.__contains__(list1[i]) == False and list1[i] > list2[j]:
        newList.append(list1[i]) 
    if newList.__contains__(list2[j]) == False and list2[j] > list1[i]:
        newList.append(list2[j])                
    return newList
    

if __name__ == "__main__":
    l2 = [3, 8, 9, 10, 15, 70]
    l1 = [3, 9, 11, 14, 15, 25]
    print(mergeSortLists(l1,l2))