import math

from source.unimportant_karnaugh_map_ceil import UnimportantKarnaughMapCeil
from source.karnaugh_map_with_importance import KarnaughMapWithImportance
from src.reducer.table_method.karnauhg_map.karnaugh_map_ceil import KarnaughMapCeil
import src.utils as utils


class KarnaughMapBuilder:
    def build(self, vector: str) -> KarnaughMapWithImportance:
        if not (var_count := math.log2(len(vector))).is_integer():
            raise ValueError("Vector must have length that is from powers of 2")

        var_count = int(var_count)
        row_length = 2**((var_count + 1) // 2)

        result = KarnaughMapWithImportance()
        result._column_vars = [f"x{i+1}" for i in range(var_count // 2)]
        result._row_vars = [f"x{i+1}" for i in range(var_count // 2, var_count)]
        row = []
        for i, char in enumerate(vector[utils.to_gray(i)] for i in range(len(vector))):
            match char:
                case '0':
                    ceil = KarnaughMapCeil(False)
                case '1':
                    ceil = KarnaughMapCeil(True)
                case 'x':
                    ceil = UnimportantKarnaughMapCeil()
                case _:
                    raise ValueError(f"Vector have unexpected char: {char}")
            row.append(ceil)
            if i % row_length == row_length - 1:
                if len(result) % 2 == 1:
                    row.reverse()
                result.append(row)
                row = []

        return result
