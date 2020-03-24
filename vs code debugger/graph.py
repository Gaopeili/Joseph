from json import dumps
from random import randint
# 创建一个可视化数据结构
graph = {
    "kind": {"graph": True},
    "nodes": [

    ],
    "edges": []
}
# 为了方便演示并且检验算法的正确性,人为将num设置的小一些
num = 25
# 创建一个循环链表
for i in range(1,num):
    j = randint(-20,20)
    # 加入新的节点
    graph['nodes'].append({'id':str(i),'code':j})
    # 加入连接关系
    graph['edges'].append({'from':str(i),'to':str(i+1),'label':str(j)})
    # 输出为json格式方便可视化
    json_graph = dumps(graph)
# 手动将最后一个元素和起始元素连接起来
graph['edges'][num-2]['to'] = '1'
# 显示最终结果
json_graph = dumps(graph)

# 开始正式的约瑟夫环
# 以下代码移植上面的JosephByList方法,只添加了一些可视化tips

# 随便设置一个初始索引
index = 5
while len(graph['nodes']) > 0:
    # 该节点的前一个节点指向下一个
    graph['edges'][(index-1)%len(graph['nodes'])]['to'] = graph['edges'][index]['to']
    # 可视化
    json_graph = dumps(graph)
    # 删除节点
    subdict = graph['nodes'].pop(index)
    # 删除连接关系
    graph['edges'].pop(index)
    # 可视化
    json_graph = dumps(graph)
    
    # 打印出我们需要的信息
    print(subdict['id'])

    # 接下来寻找下一个需要弹出的对象
    # 这个是为了避免除数为0的情况
    if len(graph['nodes']) > 0:
        if subdict['code']>0:
            # 如果code的值大于0那么新的下标即为在原来的基础上加对应的code减去一(因为该元素已经被删除掉了)除以总长度
            index = (index + subdict['code']-1)%len(graph['nodes'])
        else:
            # 如果code的值小于0那么相当于从前往后数，但是从前往后数的时候这个节点对下标没有影响所以不需要减一
            index = (index+subdict['code'])%len(graph['nodes'])
    else:
        index = 0

graph['edges'].pop(0)
graph['nodes'].pop(0)
print("Finished")


