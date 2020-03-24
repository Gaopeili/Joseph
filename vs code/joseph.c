#include<stdio.h>
#include<stdlib.h>
#include<time.h>

// 节点
typedef struct list{
    int index;
    int code;
    struct list* next;
}LinkList;
// 创建循环链表
LinkList* CreateList(int n,LinkList** tail);
// 打印循环链表
void Display(LinkList* head);
// 删除cur节点并令cur指向下一个
void Delete(LinkList** pre,LinkList** cur);

void Joseph_circle(LinkList* head,LinkList* tail,int n,int m);

LinkList* CreateList(int n,LinkList** tail)
{
    srand(666);
    LinkList* head = (LinkList*)malloc(sizeof(LinkList));
    LinkList* phead = head;
    for(int i=1;i<=n;i++)
    {
       LinkList* node = (LinkList*)malloc(sizeof(LinkList));
       node->index = i;
       int temp = -25+rand()%50;
       node->code = temp;
       node->next = NULL;
       phead->next = node;
       phead = node;
    }
    LinkList* temp = head;
    head = head->next;
    free(temp);
    (*tail) = phead;
    phead->next = head;
    return head;
}

void Display(LinkList* head)
{
    LinkList* phead = head ;
    printf("index:%d\tcode:%d\n",phead->index,phead->code);
    phead = phead->next;
    while(phead && phead!=head)
    {
        printf("index:%d\tcode:%d\n",phead->index,phead->code);
        phead = phead->next;
    }
}


/**
 * @brief   单向循环链表解决约瑟夫问题
 * @param   head:单向循环链表头指针
 * @param   tail:单向循环链表尾指针
 * @param   n:将要创建的个数
 * @param   m:要删除的节点位置
 * @retval  无
 */
void Joseph_circle(LinkList* head,LinkList* tail,int n,int m)
{
    // 申明pre为循环链表的tail
    LinkList* pre = tail;
    // cur为循环链表的head
    LinkList* cur = head;
    // 当单向链表长度大于1的时候
    while (n>1)
    {
        // 找到删除节点的位置
        while(--m)
        {
            pre = cur;
            cur = cur->next;
        }
        // 现在链表长度要减一
        n--;
        // 打印出我们需要的信息
        printf("%d\n",cur->index);
        // code大于0的情况
        if (cur->code>0)
        {
            m = cur->code % n;
            if(m == 0)
            {
                m = n;
            }
        }
        else if(cur->code < 0 )
        {
            // code小于0的情况
            m = cur->code % n + 1 + n;
        }
        // 删除cur节点
        Delete(&pre,&cur);
    }
    // 打印出最后一个节点
    printf("%d\t",pre->index);
    
}

/**
 * @brief 将给定单向循环链表的cur删除并且将其指向下一个位置,如果只有两个节点那么cur返回空
 * @param pre是二级指针用来修改某节点的前驱节点指向的位置
 * @param cur是二级指针用来将原节点删除并指向下一个位置
 * @retval 无返回值
 */
void Delete(LinkList** pre,LinkList** cur)
{
    // 用来记录pre原指针指向的位置
    LinkList* temp = *pre;
    // 将pre指向cur的下一个
    (*pre)->next = (*cur)->next;
    // 删除cur
    free(*cur);
    // 如果cur的下一个和原来的指针相等说明原链表只有两个节点了
    if((*pre)->next == temp)
    {
        // 只有两个节点的话就把cur复位为空
        *cur = NULL;
        (*pre)->next = NULL;
    }
    else
    {
        // 否则将cur指向pre的下一个
        *cur = (*pre)->next;
    }
    
}


