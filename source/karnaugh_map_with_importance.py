from src.reducer.table_method.karnauhg_map.karnaugh_map import KarnaughMap
from src.unimportant_karnaugh_map_ceil import UnimportantKarnaughMapCeil


class KarnaughMapWithImportance(KarnaughMap):
    def is_full_of_true(self) -> bool:
        return all(all(x.value or isinstance(x, UnimportantKarnaughMapCeil) for x in row) for row in self)

    def is_full_of_false(self) -> bool:
        return all(all(not x.value or isinstance(x, UnimportantKarnaughMapCeil) for x in row) for row in self)
