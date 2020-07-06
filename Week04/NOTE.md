学习笔记
### 搜索 - 遍历
  * 每个节点都要访问一次
  * 每个节点仅仅要访问一次
  * 对于节点访问顺序不限
    * -深度优先：depth first search
    * -广度优先：breadth first search

### 深度优先搜索：
  * 代码：（递归）
  ``` python
  def dfs(node):
    if node in visited:
    #already visited
    return
    visited.add(node)
    #process current node
    #...logic here
    dfs(node.left)
    dfs(node.right)
  ```
  * 多叉树
  ``` python
  visited = set()
  def dfs(node,visited):
    visited.add(node)
    # process current node here
    ...
    for next_node in node.children():
      if not next_node in visited:
        dfs(next_node,visited)
  ```
  * 递归写法（用递归的公式）
  ```python
  visited = set()
  def dfs(node,visited):
    #terminator
    if node in visited:
    #already visited
    return
    visited.add(node)
    # process current node here
    ...
    for next_node in node.children():
      if not next.node in visited:
        dfs(next node,visited)
  ```
  * 非递归写法 （手动维护一个栈）
  ``` python
  def DFS(self,tree):
    if tree.root in None:
      return[]
    visited,stack =[], [tree.root]  #站
    while stack:
      node=stack.pop()
      visited.add(node)
      process(node)
      nodes=generate_related_nodes(node)
      stack.push(nodes)
    #other processig work
  ```
  
### 广度优先遍历 BFS
* 代码：
```python
  def BFS(graph,start,end): # queue
    queue = []
    queue.append([start])
    visited.add(start)
    while queue:
      node = queue.pop()
      visited.add(node)
      process(node)
      nodes=generate_related_nodes(node)
      queue.push(nodes)
    # other processing work
```
  
### 贪心算法(Greedy)
* 概念 
  * 在么一部选择中都采取在当前状态下最好的或者最有的选择，从而希望导致结果是全局最好或最优的算法
  
* 与动态规划的区别：
  * 贪心：不能回退
  * 动态规划： 保存之前的结果，有回退功能
  * 回溯： 能够回退
  
* 硬币问题： 贪心法 [20,10,5,1] 找零问题 前提是这些数据 小数可以被大叔整除

### 二分查找
* 前提：
  * 目标函数单调性（单调递增或者递减）
  * 存在上下界 (bounded)
  * 能够通过索引访问 (index accessible)
* 代码模板：
``` python
left, right=0, len(array)-1
while left <=right:
  mid =(left + right)/2
  if array[mid]==target:
    # find the target!
    break or return result
  elif array[mid] < target:
    left = mid + 1
  eles: 
    right = mid +1
```
