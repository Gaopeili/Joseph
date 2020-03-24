class Node():
    def __init__(self,val,index):
        self.index = index
        self.val = val
        self.next = None

class DNode():
    def __init__(self,index,code):
        self.index = index
        self.code = code
        self.pre = None
        self.next = None


class CircleList(object):
    """单链表"""

    def __init__(self):
        self._head = None
        self.length = 0
        self._tail = None

    def create_list(self, datas):
        """创建一个单向循环链表"""
        cur = Node(datas[0], 1)
        cur.next = None
        self._head = cur
        n = 2
        for data in datas[1:]:
            node = Node(data, n)
            cur.next = node
            cur = cur.next
            n += 1
        self._tail = cur
        self._tail.next = self._head
        self.length = len(datas)

    def deleteNode(self,pre,cur):
        pre.next = cur.next
        cur = pre.next
        self.length -= 1
        return cur

class DCirclelist(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def creat_list(self,datas):
        # 创建一个起始节点
        cur = DNode(1,datas[0])
        # 赋值给head
        self.head = cur
        # 用n当做双向循环链表的索引
        n = 2
        # 用剩余的元素创建双向循环链表
        for data in datas[1:]:
            # 创建一个新的节点
            node = DNode(n,data)
            # 将新节点和前驱连接起来
            node.pre = cur
            # 前驱和新节点连接起来
            cur.next = node
            # 前驱往下顺延
            cur = node
            # 每次n都自增
            n+=1
        # 将最后一个节点和头结点连接起来
        cur.next = self.head
        # 头结点和最后一个节点连接起来
        self.head.pre = cur
        # 双向循环链表的长度设置为n
        self.length = n

    def deleteNode(self,pre,cur):
        pre.next = cur.next
        cur.next.pre = pre
        cur = pre.next
        self.length -= 1
        return cur











