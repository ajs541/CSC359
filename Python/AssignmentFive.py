def mergeSortLists(list1, list2):
    newList = []
    count = 0
    if list1 == None or list2 == None:
        raise Exception("One or both of the lists are empty")
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if count == 0:
                    newList.append(list1[i])
                    count += 1
                elif newList.__contains__(list1[i]) == False:
                    newList.append(list1[i])
                    count += 1
            if list1[i] < list2[j]:
                if newList.__contains__(list1[i]) == False:
                    newList.append(list1[i])
                    count += 1
            if list2[j] < list1[i]:
                if newList.__contains__(list2[j]) == False:
                    newList.append(list2[j])
                    count += 1        
    if newList.__contains__(list1[i]) == False and list1[i] > list2[j]:
        newList.append(list1[i]) 
    if newList.__contains__(list2[j]) == False and list2[j] > list1[i]:
        newList.append(list2[j])                
    return newList

if __name__ == "__main__":
    l1 = [1,3,8,11,12]
    l2 = [1,2,3,7,9,11]
    print(mergeSortLists(l1,l2))