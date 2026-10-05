# from  turtle import Turtle,Screen

# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("black")
# timmy.forward(100) 

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon names",["pikachu","squirtle","charmnder"])
table.add_column("type of power",["electric","water","fire"])
print(table)
