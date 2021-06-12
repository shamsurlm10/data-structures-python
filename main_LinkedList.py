from LinkedList import LinkedList

l1 = LinkedList()

l1.append(10)
l1.append(90)
l1.append(80)
l1.insert(2, 15)
l1.insert_at_beginning(50)

removedValue1 = l1.pop()
removedValue2 = l1.remove_at_beginning()
removedValue2 = l1.remove(2)


found1 = l1.find(15)
found1 = l1.find(10)

searchedValue = l1.search(4)

print(l1)

l1.reverse()

print(l1)
