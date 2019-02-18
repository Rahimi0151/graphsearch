from Graph import Graph

class FileReader():

    def convert_to_graph( self , file_name , graph ):
        text = open( file_name , "r" ).read()
        splited_text = text.split( "\n" )

        for i in range( len( splited_text )-1 ) :
            from_node = int( splited_text[ i ].split( " " )[ 0 ] )
            to_node = int( splited_text[ i ].split( " " )[ 1 ] )
            graph.add_edge( from_node , to_node )
    