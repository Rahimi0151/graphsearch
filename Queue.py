class Queue():

    def __init__(self):
        self.__queue = []

    # Helper Functions

    def print_queue( self ):
        print( self.__queue )

    def __is_array( self , input ):
        return type([]) == type( input )

    # Main Functionality
        
    def enqueue( self , number ):
        if self.__is_array( number ):
            for i in number:
                self.enqueue(i)
        else:
            self.__queue.insert( 0 , number )

    def dequeue( self ):
        return int(self.__queue.pop())

    def is_empty( self ):
        return len( self.__queue ) == 0

    def contains( self , element ):
        return element in self.__queue