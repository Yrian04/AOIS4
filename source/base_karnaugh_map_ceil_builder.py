from abc import ABC, abstractmethod

from src.reducer.table_method.karnauhg_map.karnaugh_map import KarnaughMap


class BaseKarnaughMapBuilder:
    @abstractmethod
    def build(self, vector: str) -> KarnaughMap: pass

