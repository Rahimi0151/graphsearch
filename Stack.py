class Stack():

    def __init__(self):
        self.__stack = []

    # Helper Functions

    def print_stack( self ):
        print( self.__stack )

    def __is_array( self , input ):
        return type([]) == type( input )

    # Main Functionality
        
    def push( self , number ):
        if self.__is_array( number ):
            for i in number.reverse():
                self.push(i)
        else:
            self.__stack.append( number )

    def pop( self ):
        return int(self.__stack.pop())

    def is_empty( self ):
        return len( self.__stack ) == 0

    def contains( self , element ):
        return element in self.__stack