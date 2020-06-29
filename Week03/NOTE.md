学习笔记
### 递归 (recursion)
* 递归-循环
  * 通过函数体来进行的循环
* 特点：
  * 向下进入到不同的函数，向上又回到上一层
* 代码模板
```python
def recursion(level,param1,param2,...)
   # recursion teminator (递归终结者)
   if level>MAX_LEVEL:
      process_result
      return
      
   # process logic in current level (解决这一层业务)
   process(level,data,...)
   
   # drill down (下到下一层)
   self.recursion(level+1,p1,...)
   
   # reverse current level status if needed (清理当前层)
```
* 思维要点：
 * 不要人肉进行递归
 * 找到最近最简方法，将其解析成可重复的解决问题的(重复子问题)
 * 数学归纳思维法
 
### 分治 Drivde & Conquer
* 代码模板
```python
def divide_conquer(problem,param1,param2,...):
  # recursion teminator (递归终结者)
   if problem is None:
      print_result
      return
      
   # prepare data (准备数据)
   data = prepare_data(problem)
   subproblems = spilt_problem(problem,data)
   
   # conquer subproblems (下到下一层)
   subproblem1 = self.divide_conquer(subproblems[0],p1,...)
   subproblem2 = self.divide_conquer(subproblems[1],p1,...)
   subproblem3 = self.divide_conquer(subproblems[2],p1,...)
   ...
   
   # process and generate the final result
   result = process_result(subproblem1,subproblem2,subproblem3,...)
```
### 回溯
* 二叉树遍历完之后回来: 归去来兮
