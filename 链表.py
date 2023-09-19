class ListNote:
    def __init__(self,val,next):
        self.val = val
        self.next = next

def creat_linklist(data:list):
    head = ListNote(data[0], None)
    p = head
    for val in data[1:]:
        p.next = ListNote(val, None)
        p = p.next
    return head

def print_linklist(head:ListNote):
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    data = [2,7,4,3,5]
    head = creat_linklist(data)
    print_linklist(head)




