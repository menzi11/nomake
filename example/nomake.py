
import nomake

set_solution_name( "TestSolution" )

my_projects = [ "Main" , "UnitTest" ]

add_project( my_projects )

add_cpp( "Main" , "src/" )
add_cpp( "UnitTest" , "tests/test.cpp" )

add_headers( my_projects , "src/somelib.h" )