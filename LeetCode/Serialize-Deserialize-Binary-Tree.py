# O(n) time and space complexity for both serialization and 
# deserialization
# Definition for a binary tree node.


from collections import deque 

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # if we see a None
        if not root:
            return "-1001"
        # Otherwise we serialize root, roo.left and root.right 
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # from preorder list to tree
        def helper(dq): 
            # using the dq we deserialize one by one
            value = dq.popleft()
            # if we see -1, means we need to form null node
            if value == -1001:
                return None
            # form the actual node
            node = TreeNode(value)
            # form node's left
            node.left = helper(dq)
            # form node's right
            node.right = helper(dq)
            
            return node
        
        # at first get the node integer vals from the serial of 
        # the tree 
        print(data)
        data = map(int,data.split(","))

        dq = deque(data)

        return helper(dq)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == "__main__":
    
    root = TreeNode([2,4,6])
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    #ans = ser.serialize(root)
    #de = deser.deserialize(ans)
    print("SER: ", ans)
    #print("DE: ", de)