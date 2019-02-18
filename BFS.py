from Graph import Graph
from Queue import Queue
from Stack import Stack
from Search import Search

class BFS( Search ):

    def __initialize_BFS( self , wanted_node ):
        self.__queue = Queue()
        self.visited_nodes = []
        self.wanted_node = wanted_node

    def __is_new_node( self , node ):
        return not node in self.visited_nodes and not self.__queue.contains( node )

    def __add_children( self , node ):
        for node in self.graph.graph[ node ]:
            if self.__is_new_node( node ):
                self.__queue.enqueue( node )

    def __call_recursive_BFS( self , node ):
        self.visit( node )
        if self.is_wanted_node( node ):
            return
        self.__add_children( node )      
        self.__call_recursive_BFS( self.__queue.dequeue() )

    def BFS( self , wanted_node , starting_node = 1 ):
        self.__initialize_BFS( wanted_node )
        if self.has_not_found_exception():
            return
        self.__call_recursive_BFS( starting_node )
        return self.print_path()
