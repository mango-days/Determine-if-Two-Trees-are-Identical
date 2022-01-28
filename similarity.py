class Node :
    def __init__ ( self , data ) :
        self.left = None
        self.data = data
        self.right = None

class BinaryTree :
    def __init__ ( self ) :
        self.root = None
    
    def insert ( self , data ) :
        if self.root == None :
            self.root = Node ( data )
            return
        
        parent = self.root
        temp = self.root
        
        while temp :
            parent = temp
            
            if temp == None : 
                temp = Node ( data )
                return
        
            if temp.data == data : return # data exists
        
            if temp.data < data : 
                temp = temp.right
                if temp == None : 
                    parent.right = Node ( data )
                    return
            elif temp.data > data : 
                temp = temp.left
                if temp == None :
                    parent.left = Node ( data )
                    return
            else : print ( " something unfathomable happened! " )
        return

    def printList ( self , node ) :
        if node == None : return
        if node.data : print ( node.data ) #data exists
        if node.left : 
            print ( " --- L of" , node.data , ":")
            self.printList ( node.left )
        if node.right : 
            print ( " --- R of" , node.data )
            self.printList ( node.right )
        return
    
    def height ( self , node ) :
        if node == None : return 0
        x = y = 1
        if node.left : 
            x = x + self.height ( node.left )
        if node.right : 
            y = y + self.height ( node.right )
        return max ( x , y )
    
    def isSimilar ( self , node1 , node2 ) :
        if ( node1 and node2 and node1.left == None and node1.right == None and node2.right == None and node2.left == None ) : return True
        if node1 == None and node2 == None : return True
        elif node1 == None or node2 == None : return False
        x = False
        y = False
        if node1.left and node2.left : x = self.isSimilar ( node1.left , node2.left )
        if node1.right and node2.right : y = self.isSimilar ( node1.right , node2.right )
        if x == False or y == False : return False
        return True

Obj = BinaryTree ()
arr = [ 5 , 3 , 8 , 2 , 6 , 4 , 9 ]
for index , value in enumerate ( arr ) : Obj.insert ( value )

O = BinaryTree ()
arr = [ 5 , 8 , 3 , 2 , 6 , 4 , 9 ]
for index , value in enumerate ( arr ) : O.insert ( value )

x = Obj.isSimilar ( Obj.root , O.root )
print ("similarity =", x )
