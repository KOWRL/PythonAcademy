#!/usr/bin/env python3
class Key:  # Klucze -> Klucz p³aski -> Rozmiar
    pass


class Wrench(Key):
    pass


class WrenchSize(Wrench):
    pass


class Accessory:  # Akcesoria -> Nasadki -> Rozmiar
    pass


class Cap(Accessory):
    pass


class CapSize(Cap):
    pass


class AllenKey:  # Imbusy -> Rodzaj -> Rozmiar
    pass


class TypeAllenKey(AllenKey):
    pass


class SizeAllenKey(TypeAllenKey):
    pass


class AdjustableWrench:  # Klucze nastawne -> Typ klucza -> Rozmiar
    pass


class TypeAdjustableWrench(AdjustableWrench):
    pass


class SizeAdjustableWrench(TypeAdjustableWrench):
    pass


class Toolbox:  # Zestaw narzêdzi -> Typ zestawu -> Iloœæ
    pass


class TypeToolbox(Toolbox):
    pass


class AmountToolbox(TypeToolbox):
    pass


print("Key")
wrench_size = WrenchSize()  # Klucze -> Klucz p³aski -> Rozmiar
print(isinstance(wrench_size, WrenchSize))
print(isinstance(wrench_size, Wrench))
print(isinstance(wrench_size, Key))
print(isinstance(wrench_size, object))

print("Accessory")
cap_size = CapSize()  # Akcesoria -> Nasadki -> Rozmiar
print(isinstance(cap_size, CapSize))
print(isinstance(cap_size, Cap))
print(isinstance(cap_size, Accessory))
print(isinstance(cap_size, object))

print("Allen Key")
size_allen_key = SizeAllenKey()  # Imbusy -> Rodzaj -> Rozmiar
print(isinstance(size_allen_key, SizeAllenKey))
print(isinstance(size_allen_key, TypeAllenKey))
print(isinstance(size_allen_key, AllenKey))
print(isinstance(size_allen_key, object))

print("Adjustable Wrench")
size_adjustable_wrench = SizeAdjustableWrench()  # Klucze nastawne -> Typ klucza -> Rozmiar
print(isinstance(size_adjustable_wrench, SizeAdjustableWrench))
print(isinstance(size_adjustable_wrench, TypeAdjustableWrench))
print(isinstance(size_adjustable_wrench, AdjustableWrench))
print(isinstance(size_adjustable_wrench, object))

print("Toolbox")
amount_toolbox = AmountToolbox()  # Zestaw narzêdzi -> Typ zestawu -> Iloœæ
print(isinstance(amount_toolbox, AmountToolbox))
print(isinstance(amount_toolbox, TypeToolbox))
print(isinstance(amount_toolbox, Toolbox))
print(isinstance(amount_toolbox, object))