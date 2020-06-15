# 学习笔记
### 原理
* 再复杂的问题都离不开以下三步
	* 循环 for loop
	* 判断 if else
	* 递归 recursion
* 空间复杂度换时间复杂度， 升维
### 数组 Array
* 在python 种的表达 <br>
	`list = []`
	
* 在python 中的操作 <br>
	```
	array_full=['aaa','bbb','ccc']
	#append
	array_full.append('ddd')
	#insert
	array_full.insert(0,'ddd')
	#remove
	array_full.remove(0,'ddd')	```

* 操作的时间复杂度 <br>
	Manuplate|O
	-------- | -------
	Insert| O(n)
	Append| O(1)
	Remove| O(n)
	
	
### 链表 Linked List
* 在python 中定义一Node <br>
	```
	class Node(object):
   		def __init__(self,data):
       			self.data = data
			self.next = None
	```
	
* 在python 中的操作 <br>
	```
	class LinkList(object):
   		def __init__(self):
       		self.head = Node(None)

   	#判断链表是否为空
   	def IsEmpty(self):
       		p = self.head #头指针
       		if p.next == None:
           		print("List is Empty")、
			return True
		return False
   	#打印链表
   	def PrintList(self):
       		if self.IsEmpty():
           		return False
       		p = self.head
       		while p:
           		print(p.data,end=' ')
           		p = p.next
	```
* 操作的时间复杂度 <br>
	Manuplate|O
	-------- | -------
	Create empty linked list| O(1)
	Create linked list| O(n)
	Insert head| O(1)
	Insert tail| O(1)
	Remove head| O(1)
	Remove tail| O(1)
	common remove and insert| O(n)
	search| O(n)


### 双链表 Double Linked List
* 在python 中定义一Node <br>
	```
	class Node(object):
   		def __init__(self,data):
       			self.data = data
			self.next = None
			self.prev = None
	```

* 操作的时间复杂度 <br>
	Manuplate|O
	-------- | -------
	prepend| O(1)
	append | O(1)
	lookup | O(n)
	inster | O(1)
	delete | O(1)
	
### 跳表 Skip List
* 定义 <br>
	 * 只能用于元素有序的情况
	 * 对标的是平衡树(AVL tree) 和二分查找树
	 * 项目中的应用 Redis LevelDB

* 操作的时间复杂度 <br>
	Manuplate|O
	-------- | -------
	insert | O(log n)
	delete | O(log n)
	lookup | O(log n)

* 跳表的空间复杂度 <br>
	* O(n)

* 给有序链表加速 <br>
	increase dimentions and increase first/second level index
	
	
	
