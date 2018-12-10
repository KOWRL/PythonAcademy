#!/usr/bin/env python3

def conversion():
    var = input("Podaj liczbe: ")
    int_var = int(var)
    print("Liczba: ", int_var, "Typ liczby: ", type(int_var).__name__)

conversion()