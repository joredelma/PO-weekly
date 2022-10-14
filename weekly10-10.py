class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def findInter(list1, list2):
    while True:
        if list1 is list2:
            return list1
        list1=list1.next
        list2 =list2.next
        if (list1.next == None or list2.next == None):
            return None


tail = Node(5, None)
inter4 = Node(4, tail)
inter = Node(3, inter4)
list12 = Node(2, inter)
list22 = Node(2, inter)
list1 = Node(1, list12)
list2 = Node(1, list22)

print(findInter(list1, list2).val)

def findCirc(circ):
    log = []
    while True:
        if circ in log:
            for node in log:
                if node is circ:
                    return circ
        log.append(circ)
        circ=circ.next


circ = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
circ.next.next.next.next.next = circ
before = Node(0, circ)
print(findCirc(before).val)