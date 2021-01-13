def printDecimal(num):
    print("{}".format(num), end="       ")

def printOctal(num):
    print("{}".format(oct(num)), end="       ")

def printHexadecimal(num):
    print("{}".format(hex(num)), end="       ")

def printBinario(num):
    print("{}".format(bin(num)), end="       ")

def imprimirTabela():
    cont = 0
    while cont < 225:
        printDecimal(cont),
        printOctal(cont),
        printHexadecimal(cont),
        printBinario(cont)
        print("\n")
        cont += 1
        print("Decimal   Octal   Hexadecimal     Binario")
        print('-------   -----     --------     ---------')
imprimirTabela()