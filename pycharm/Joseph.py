import random
import matplotlib.pyplot as plt
from json import dumps,dump
from circle_list import CircleList,DCirclelist
import numpy as np
import time

class Joseph():
    def __init__(self,datas,m):
        # 初始为datas为输入的列表形式的datas
        self.datas = datas
        # 初始化MyLinkedList为一个单向循环链表对象
        self.MyLinkedList = CircleList()
        # 初始化一个双向循环链表对象
        self.MyDLinkedList = DCirclelist()
        # 初始化一个列表
        self.lst = []
        # 初始起始元素的位置
        self.m = m
        # 初始datas的长度
        self.length = len(self.datas)


    # 用循环链表的方式来往下计算
    def josephByCirlist(self):
        """
        :param: self
        :return: None
        """
        # 根据提供的数据建立一个单向循环链表
        self.MyLinkedList.create_list(self.datas)
        # 初始化计数器
        cnt = (self.m - 1)%self.MyLinkedList.length
        # 将pre设置为循环链表的表尾
        pre = self.MyLinkedList._tail
        # 将cur设置为循环链表的表头
        cur = self.MyLinkedList._head

        # 链表长度大于0则继续循环
        while self.MyLinkedList.length > 0:
            # 根据cnt找到要删除的位置
            while cnt > 0:
                pre = cur
                cur = cur.next
                cnt -= 1
            # 打印出需要的index
            # print(cur.index)

            # 除数不为0的情况，用cnt定位到下一个被删除的位置
            if self.MyLinkedList.length-1 > 0:
                # 当cur.val大于0的时候
                if cur.val>0:
                    # cur.val减去1(因为之后删除节点的时候cur已经放到下一个了)再取余之后链表的长度
                    cnt = (cur.val - 1)%(self.MyLinkedList.length-1)
                else:
                    # cur.val小于0的时候
                    # 相当于往前数-cur.val个长度，所以往后数就是下面的结果了
                    cnt = cur.val%(self.MyLinkedList.length-1)
            # 除数为0的情况
            else:
                cnt = cur.val-1
            # 每次cnt计数完毕删除节点并更新cur到下一个位置
            cur = self.MyLinkedList.deleteNode(pre, cur)


    # 创建一个字典列表
    def createList(self):
        '''
        :param: self:将self.lst初始化为一个字典列表
        :return:    无
        '''
        i = 1
        while i <= self.length:
            # 创建一个字典，键值对含有index和code
            a = dict(index=i, code=self.datas[i-1])
            i += 1
            # 将该字典放到列表中
            self.lst.append(a)

    # 用字典列表实现的约瑟夫环
    def josephByList(self):
        # 初始化lst为字典列表
        self.createList()
        # 初始化下标为m取余lst长度
        index = 0
        if self.m % self.length == 0:
            index = self.length-1
        else:
            index = self.m % self.length-1
        # 当列表不为空就继续
        while self.length > 0:
            # 将该index下的字典弹出
            subdict = self.lst.pop(index)
            # 弹出之后列表的长度就减一
            self.length-=1

            # 打印出我们需要的信息
            # print(subdict['index'])

            # 接下来寻找下一个需要弹出的对象
            # 这个是为了避免除数为0的情况
            if self.length > 0:
                if subdict['code']>0:
                    # 如果code的值大于0那么新的下标即为在原来的基础上加对应的code减去一(因为该元素已经被删除掉了)除以总长度
                    index = (index + subdict['code']-1)%self.length
                else:
                    # 如果code的值小于0那么相当于从前往后数，但是从前往后数的时候这个节点对下标没有影响所以不需要减一
                    index = (index+subdict['code'])%self.length
            else:
                index = 0
        # 将self.length归为，避免再次调用该类中的方法
        self.length = len(self.datas)

    def josephDCircle(self):
        self.MyDLinkedList.creat_list(self.datas)
        # 初始化cnt
        cnt = (self.m - 1)%self.MyDLinkedList.length
        # 将pre初始化为head的前一个即最后一个
        pre = self.MyDLinkedList.head.pre
        # 将cur初始化为head
        cur = self.MyDLinkedList.head
        # 链表的长度大于0就继续遍历
        while self.MyDLinkedList.length > 0:
            # 找到要删除的节点位置
            # cnt大于0的时候往后移动
            while cnt > 0:
                pre = cur
                cur = cur.next
                cnt -= 1
            # cnt小于0的时候往前移动
            while cnt < 0:
                cur = pre
                pre = pre.pre
                cnt += 1
            # 打印出需要的index
            # print(cur.index)

            # 除数不为0的情况，用cnt定位到下一个被删除的位置
            if self.MyDLinkedList.length - 1 > 0:
                # 当cur.val大于0的时候
                if cur.code > 0:
                    # cur.val减去1(因为之后删除节点的时候cur已经放到下一个了)再取余之后链表的长度
                    cnt = (cur.code - 1) % (self.MyDLinkedList.length - 1)
                else:
                    # cur.val小于0的时候
                    cnt = self.MyDLinkedList.length - cur.code % (self.MyDLinkedList.length - 1)
            # 除数为0的情况
            else:
                cnt = cur.code - 1
            # 每次cnt计数完毕删除节点并更新cur到下一个位置
            cur = self.MyDLinkedList.deleteNode(pre,cur)




def main():
    """单向循环链表/数组测试"""
    """测试时只需修改调用方法即可
       单向循环链表测试时的跨度为1k到1M
       数组测试时的数据跨度为1k到500k"""
    # lst = []
    # # 设置随机种子,便于多次调试比较
    # np.random.seed(666)
    #
    # # 经过多次测验已经发现在大数量的情况下链表处理起来较快，所以人为的增大链表的测试数据区间差
    # # 从1K到100K随机取出20个数
    # nums = np.random.randint(1000,500000,50)
    # for num in nums:
    #     # 从1-50取出num个数组成一维向量
    #     matrix = np.random.randint(1, 50,num)
    #     # 将向量转换为一个列表
    #     datas = matrix.tolist()
    #     # 构建Joseph类的实例，并人为的把m设置为2
    #     Answer = Joseph(datas, m=2)
    #     # 测试每次链表需要的时间,并把时间存放到列表中
    #     t2 = time.time()
    #     Answer.josephByList()
    #     t3 = time.time()
    #     lst.append(t3-t2)
    #
    # # 指定默认字体
    # plt.rcParams['font.sans-serif'] = 'FangSong'
    # # 解决保存图像是负号'-'显示为方块的问题
    # plt.rcParams['axes.unicode_minus'] = False
    #
    # # 绘制折线图
    # plt.scatter(nums,lst)
    # plt.xlabel("数量/个")
    # plt.ylabel("时间/秒")
    # plt.title("列表数据测试")
    # plt.show()
    
    """平均时间链表列表对比测试"""
    # # 存储List的平均时间
    # List = []
    # # 存储Link的平均时间
    # Link = []
    # # 创建一个列表存放着数据的数目
    # nums = [i**2 for i in range(100,300,10)]
    # for num in nums:
    #     # 重复30次取平均值
    #     i = 30
    #     # 存储30次List时间数据
    #     ListTime = []
    #     # 存储30次Link时间数据
    #     LinkTime = []
    #     while i>0:
    #         # 创建一个向量
    #         matrix = np.random.randint(1,30,num)
    #         datas = matrix.tolist()
    #         Answers = Joseph(datas,m=2)
    #         t1 = time.time()
    #         Answers.josephByCirlist()
    #         t2 = time.time()
    #         Answers.josephByList()
    #         t3 = time.time()
    #         # 把List的时间存储下来
    #         ListTime.append(t3-t2)
    #         # 把Link的时间存储下来
    #         LinkTime.append(t2-t1)
    #         i -= 1
    #     # 将Listtime转为向量
    #     array1 = np.array(ListTime)
    #     # 将Linktime转为向量
    #     array2 = np.array(LinkTime)
    #     # 把list30次的平均值存入到List中
    #     List.append(array1.mean())
    #     # 把Link30次的平均值存入到Link中
    #     Link.append(array2.mean())
    #
    # # 指定默认字体
    # plt.rcParams['font.sans-serif'] = 'FangSong'
    # # 解决保存图像是负号'-'显示为方块的问题
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.scatter(nums,List,cmap='b')
    # plt.scatter(nums,Link,cmap='r')
    # plt.xlabel("数量/个")
    # plt.ylabel("平均时间/秒")
    # plt.title("列表链表对比")
    # plt.legend(['列表','链表'])
    # plt.show()

    """非平均时间的列表链表对比测试"""
    # # 存储List的时间
    # List = []
    # # 存储Link的时间
    # Link = []
    # # 创建一个列表存放着数据的数目
    # nums = [i**2 for i in range(400,600,10)]
    # for num in nums:
    #     # 创建一个向量
    #     matrix = np.random.randint(1,30,num)
    #     datas = matrix.tolist()
    #     Answers = Joseph(datas,m=2)
    #     t1 = time.time()
    #     Answers.josephByCirlist()
    #     t2 = time.time()
    #     Answers.josephByList()
    #     t3 = time.time()
    #     # 把List的时间存储下来
    #     List.append(t3-t2)
    #     # 把Link的时间存储下来
    #     Link.append(t2-t1)
    #
    #
    # # 指定默认字体
    # plt.rcParams['font.sans-serif'] = 'FangSong'
    # # 解决保存图像是负号'-'显示为方块的问题
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.scatter(nums,List,cmap='b')
    # plt.scatter(nums,Link,cmap='r')
    # plt.xlabel("数量/个")
    # plt.ylabel("时间/秒")
    # plt.title("列表链表对比")
    # plt.legend(['列表','链表'])
    # plt.show()

    """仅有负数的链表单向循环列表对比测试"""
    # # 存储List的时间
    # List = []
    # # 存储Link的时间
    # Link = []
    # # 创建一个列表存放着数据的数目
    # nums = [i**2 for i in range(100,200,10)]
    # np.random.seed(666)
    # for num in nums:
    #     # 创建一个向量
    #     matrix = np.random.randint(-10,-1,num)
    #     datas = matrix.tolist()
    #     Answers = Joseph(datas,m=2)
    #     t1 = time.time()
    #     Answers.josephByCirlist()
    #     t2 = time.time()
    #     Answers.josephByList()
    #     t3 = time.time()
    #     # 把List的时间存储下来
    #     List.append(t3-t2)
    #     # 把Link的时间存储下来
    #     Link.append(t2-t1)
    #
    #
    # # 指定默认字体
    # plt.rcParams['font.sans-serif'] = 'FangSong'
    # # 解决保存图像是负号'-'显示为方块的问题
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.scatter(nums,List,cmap='b')
    # plt.scatter(nums,Link,cmap='r')
    # plt.xlabel("数量/个")
    # plt.ylabel("时间/秒")
    # plt.title("列表链表对比")
    # plt.legend(['列表','链表'])
    # plt.show()

    """带负数的链表列表对比测试"""
    # # 存储List的时间
    # List1 = []
    # # 存储Link的时间
    # List2 = []
    # # 创建一个列表存放着数据的数目
    # nums = [i ** 2 for i in range(400, 600, 10)]
    # for num in nums:
    #     # 创建一个向量
    #     matrix1 = np.random.randint(-10, 10, num)
    #     matrix2 = np.random.randint(1,10,num)
    #     Answers1 = Joseph(matrix1.tolist(), m=2)
    #     Answers2 = Joseph(matrix2.tolist(),m = 2)
    #     t1 = time.time()
    #     Answers1.josephByList()
    #     t2 = time.time()
    #     Answers2.josephByList()
    #     t3 = time.time()
    #     # 把List的时间存储下来
    #     List1.append(t2 - t1)
    #     # 把Link的时间存储下来
    #     List2.append(t3 - t2)
    #
    # # 指定默认字体
    # plt.rcParams['font.sans-serif'] = 'FangSong'
    # # 解决保存图像是负号'-'显示为方块的问题
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.scatter(nums, List1, cmap='b')
    # plt.scatter(nums, List2, cmap='r')
    # plt.xlabel("数量/个")
    # plt.ylabel("时间/秒")
    # plt.title("带负数和不带负数列表对比")
    # plt.legend(['带负数', '不带负数'])
    # plt.show()

    """仅有负数的列表双向循环链表对比测试"""
    # # 存储List的时间
    # List = []
    # # 存储Link的时间
    # Link = []
    # # 创建一个列表存放着数据的数目
    # nums = [i**2 for i in range(300,500,10)]
    # np.random.seed(666)
    # for num in nums:
    #     # 创建一个向量
    #     matrix = np.random.randint(-20,-1,num)
    #     datas = matrix.tolist()
    #     Answers = Joseph(datas,m=2)
    #     t1 = time.time()
    #     Answers.josephDCircle()
    #     t2 = time.time()
    #     Answers.josephByList()
    #     t3 = time.time()
    #     # 把List的时间存储下来
    #     List.append(t3-t2)
    #     # 把Link的时间存储下来
    #     Link.append(t2-t1)
    # # 指定默认字体
    # plt.rcParams['font.sans-serif'] = 'FangSong'
    # # 解决保存图像是负号'-'显示为方块的问题
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.scatter(nums,List,cmap='b')
    # plt.scatter(nums,Link,cmap='r')
    # plt.xlabel("数量/个")
    # plt.ylabel("时间/秒")
    # plt.title("列表链表对比")
    # plt.legend(['列表','链表'])
    # plt.show()

   matrix = np.random.randint(1,20,10)
   answer = Joseph(matrix.tolist,2)
   answer.josephByList()

if __name__ == '__main__':
    main()

