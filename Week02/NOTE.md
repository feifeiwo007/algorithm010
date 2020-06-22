# 学习笔记
### 树 Tree
* Linked List 是特殊化的Tree
* Tree 是特殊化的Graph

### 二叉树遍历
* 前序(Pre-order): 根左右
* 中序(In-order): 左根右
* 后序(Post-order): 左右根

### 二叉搜索树(Sorted Binary Tree/Ordered Binary Tree)
#### 特征
* 左子树上所有的结点的值均小于它的根结点的值
* 右子树上所有的结点的值均大于它的根结点的值
* 左右子树也分别为二叉查找树
* 中序遍历:升序排列
#### 删除
* 删除根结点：
   * 用左边紧临的最大结点顶替根结点
   * 一般使用右边紧临的最小结点 顶替根结点(Common)
* 删除子结点: 直接删掉

#### 代码
* Pre-order
```
  def preorder(self,root):
    if root:
      self.traverse_path.append(root.val)
      self.preorder(root.left)
      self.preorder(root.right)
```

* In-order
```
  def inorder(self,root):
    if root:
      self.inorder(root.left)
      self.traverse_path.append(root.val)      
      self.inorder(root.right)
```

* Post-order
```
  def postorder(self,root):
    if root:
      self.postorder(root.left)
      self.postorder(root.right)
      self.traverse_path.append(root.val)
```

### 堆 Heap
* 可以迅速找到一堆数中的最大或最小值的数据结构
* 时间复杂度
    * find-max: O(1)
    * delete-max: O(logN)
    * insret(create): O(logN) or O(1)
* 大顶堆&小顶堆
* 完全二叉堆
    * 根结点 a[0]
    * 索引为i 的左孩子索引是 (2 * i+1)
    * 索引为i 的右孩子索引是 (2 * i+2)
    * 索引为i 的父节点索引是 floor((i-1)/2)
    
### 图 Graph
* V-vertex: 点
    * 度: 入度和出度
    * 点与点之间： 联通与否
* E-edge: 边
    * 有向与无向
    * 有权与无权
