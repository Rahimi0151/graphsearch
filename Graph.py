class Graph():

    def __init__(self):
        self.graph = {}
    
    # Helper Functions

    def print_graph( self ):
        print( self.graph )

    # Main Functionality

    def add_edge( self , from_node , to_node ):
        if from_node in self.graph:
            self.graph[from_node].append(to_node)
        else:
            self.graph[from_node] = [to_node]

    def add_2way_edge( self , first_node , second_node ):
        self.add_edge( first_node , second_node )
        self.add_edge( second_node , first_node )
