from Graph import Graph
from Queue import Queue
from Stack import Stack

class Search():
    
    def __init__( self , graph ):
        self.graph = graph

    def has_not_found_exception( self ):
        if not self.wanted_node in self.graph.graph.keys():
            print( "404 Item Not Found in the Graph!" )
            return True
    
    def visit( self , node ):
        self.visited_nodes.append( node )

    def print_path( self ):
        print( self.visited_nodes )

    def is_wanted_node( self , node ):
        return node == self.wanted_node
