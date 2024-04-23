from src.reducer.table_method.table_method_reduce_strategy import TableMethodReduceStrategy
from source.karnaugh_map_builder import KarnaughMapBuilder
import source.utils as utils

cnf_symbols = '*', '+'
dnf_symbols = '+', '*'

while True:
    form = input("Choose the form os formula:\n\t1 - CNF\n\t2 - DNF\n")
    match form:
        case '1':
            symbols = cnf_symbols
        case '2':
            symbols = dnf_symbols
        case _:
            print("Invalid input...")
            continue
    break

builder = KarnaughMapBuilder()
while True:
    string = input("Enter vector: ")
    if form == "1":
        new_str = ""
        for c in string:
            if c == '0':
                new_str += '1'
            elif c == '1':
                new_str += '0'
            else:
                new_str += c
        string = new_str
    try:
        karnaugh_map = builder.build(string)
    except ValueError as e:
        print(e)
        continue
    break

formula = TableMethodReduceStrategy.get_formula_from_karnaugh_map(karnaugh_map)
if form == "1":
    for implicant in formula:
        for var in implicant:
            implicant.add(var[0], not var[1])
            implicant.remove(var)
print(formula.print(*symbols))
