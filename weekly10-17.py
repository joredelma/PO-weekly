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

class Stack:
    def __init__(self):
        self.vals = []
        self.top = None
        self.maxx = None
        self.prev = False
    
    def push(self, val):
        self.vals.append(val)
        if self.maxx == None:
            self.maxx = val
            self.prev = True
        if val > self.maxx:
            self.maxx = val
            self.prev = True
        else:
            self.prev = False
    
    def pop(self):
        if len(self.vals) == 0:
            print("error stack empty")
            return
        r = self.vals[-1]
        self.vals.pop(-1)
        self.maxx = max(self.vals)
        return r

    def max2(self):
        if len(self.vals) == 0:
            print("error stack empty")
            return
        return self.maxx

st = Stack()
st.pop()
st.max2()
st.push(1)
st.push(2)
st.push(3)
print(st.max2())
print(st.pop())
print(st.pop())
print(st.max2())