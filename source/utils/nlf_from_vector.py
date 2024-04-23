from src.formula.normal_logical_formula import NormalLogicalFormula
from src.formula.conjuent import Conjuent


def FCNF_from_vector(bits: list[bool], *args: str) -> NormalLogicalFormula:
    if len(bits) != 1 << len(args):
        raise ValueError("Invalid count of args or bits")

    formula = NormalLogicalFormula()
    for i, bit in enumerate(bits):
        if bit:
            cojuent = Conjuent()
            for j, arg in enumerate(reversed(args)):
                modular = bool(i & (1 << j))
                cojuent.add(arg, modular)
            formula.add(cojuent)
    return formula


def FDNF_from_vector(bits: list[bool], *args: str) -> NormalLogicalFormula:
    if len(bits) != 1 << len(args):
        raise ValueError("Invalid count of args or bits")

    formula = NormalLogicalFormula()
    for i, bit in enumerate(bits):
        if not bit:
            cojuent = Conjuent()
            for j, arg in enumerate(reversed(args)):
                modular = not bool(i & (1 << j))
                cojuent.add(arg, modular)
            formula.add(cojuent)
    return formula
