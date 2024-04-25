from src.reducer.table_method.table_method_reduce_strategy import TableMethodReduceStrategy
from source.karnaugh_map_builder import KarnaughMapBuilder
import source.utils as utils

cnf_symbols = '*', '+'
dnf_symbols = '+', '*'

builder = KarnaughMapBuilder()
while True:
    string = input("Enter vector: ")
    try:
        dnf_karnaugh_map = builder.build(string)
        cnf_string = ""
        for c in string:
            if c == '0':
                cnf_string += '1'
            elif c == '1':
                cnf_string += '0'
            else:
                cnf_string += c
        cnf_karnaugh_map = builder.build(cnf_string)
    except ValueError as e:
        print(e)
        continue
    break

dnf = TableMethodReduceStrategy.get_formula_from_karnaugh_map(dnf_karnaugh_map)
print("DNF: ", dnf.print(*dnf_symbols))

cnf = TableMethodReduceStrategy.get_formula_from_karnaugh_map(cnf_karnaugh_map)
for implicant in cnf:
    for var in implicant:
        implicant.add(var[0], not var[1])
        implicant.remove(var)
print("CNF: ", cnf.print(*cnf_symbols))
