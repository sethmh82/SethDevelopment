import math
'''
1 < N, Q < 1,000,000
 
EXAMPLE TREE
         1(a)
        /   \
      2(b)  3(a)
 
 n = 7
 q = 3
 s = "abaacab"
 queries = [(1,'a'),(2,'b'),(3,'a')]
 
 #ROOT = NODE(1)   
 #QUERIES = [(1,'a'),(2, 'b'),(3, 'a')]  
 #S = "abaacab" (LABELS)
 
#BUILD OUR TREE:
  root = Node(1)
  root.children.append(Node(7))
  root.children[0].children.append(Node(4))

'''
#NODES SUBTREE
class Node: 
  def __init__(self, data): 
    self.val = data #s value
    self.children = []

def count_of_nodes(root, queries, s):

  #MEMOITIZE
  dictionary = {}
  
 
  # USING RECURSION DFS
  def dfs(root, collection):
    
    #IF THERE IS NO ROOT
    if not root: return
    
    #BASE CASE
    #IF THE ROOT HAS NO CHILD THEN ADD THE VALUE TO DICTIONARY AND STOP RECURSION
    if not root.children:
      dictionary[root.val] = s[root.val - 1]
      return
      
    dictionary[root.val] = s[root.val - 1]
      
      #RECURSE THROUGH THE CHILDREN
    for children in root.children:
      dfs(children, collection)
      
      #RE-ASSIGN DICTIONARY INDEX VALUE
      #EACH TIME WE ASSIGN THE NODE TO THE NEXT CHILD VALUE
      dictionary[root.val] += dictionary[c.val]
    
  #CALL OUR DFS METHOD CONTAINING ( NODE(1), {} ) AND DICTIONARY
  dfs(root, dictionary)
  print(queries)
  
  # COLLECT OUR QUERIES INTO OUR RESULTS LIST
  for q in queries:
      res.append(dictionary[q[0]].count(q[1]))
  return res
  

  
---------------------------------------------
SECOND SOLUTION USES POST ORDER

  def postorder(result, curr, queries, s, parents):
    
    if curr is not None:
      parents.append(curr.val) 
      
      for child in curr.children:
        postorder(result, child, queries, s, parents)
        
      for i in range(len(queries)):
        qRootVal = queries[i][0]
        qChar = queries[i][1]
        
        
        if qRootVal in parents and qChar == s[curr.val-1]:
          result[i] += 1
          
      parents.pop()
      
  result = [0] * len(queries)
  postorder(result, root, queries, s, [])
  
  return result
        
    
if __name__ == "__main__":

  n,q = 3,1 
  s = "aba"
  root = Node(1) 
  root.children.append(Node(2)) 
  root.children.append(Node(3)) 
  queries = [(1, 'a'), (2,'b')]
  