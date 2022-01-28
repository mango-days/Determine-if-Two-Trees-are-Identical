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
        
Obj = BinaryTree ()
arr = [ 5 , 3 , 8 , 2 , 6 , 4 , 9 ]
for index , value in enumerate ( arr ) : Obj.insert ( value )
Obj.printList ( Obj.root )
print ( "height =", Obj.height ( Obj.root ) )
