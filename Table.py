from prettytable import PrettyTable

table = PrettyTable() #we have a table object

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
