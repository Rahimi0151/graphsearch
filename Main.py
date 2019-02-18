from BFS import BFS
from DFS import DFS
from Graph import Graph
from FileReader import FileReader



FILE_NAME = "Graph"

graph = Graph()
file_reader = FileReader()

file_reader.convert_to_graph( FILE_NAME , graph )
BFS = BFS( graph )
BFS.BFS( 6 )



file_reader.convert_to_graph( FILE_NAME , graph )
DFS = DFS( graph )
DFS.DFS( 4 )

