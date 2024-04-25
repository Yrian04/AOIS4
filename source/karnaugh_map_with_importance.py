from src.reducer.table_method.karnauhg_map.karnaugh_map import KarnaughMap
from source.unimportant_karnaugh_map_ceil import UnimportantKarnaughMapCeil


class KarnaughMapWithImportance(KarnaughMap):
    def is_full_of_true(self) -> bool:
        return all(all(x.value or isinstance(x, UnimportantKarnaughMapCeil) for x in row) for row in self)

    def is_full_of_false(self) -> bool:
        return all(all(not x.value or isinstance(x, UnimportantKarnaughMapCeil) for x in row) for row in self)

    @staticmethod
    def _remove_useless_edges(edges: list[KarnaughMap]):
        useful_edges = []
        useless_edges = []
        for x in edges:
            for row in x:
                for ceil in row:
                    if isinstance(ceil, UnimportantKarnaughMapCeil):
                        continue
                    for y in (e for e in edges if e not in useless_edges and e is not x):
                        if ceil in y:
                            break
                    else:
                        useful_edges.append(x)
                        break
            if x not in useful_edges:
                useless_edges.append(x)
        return useful_edges
