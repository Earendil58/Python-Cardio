x = "global"

def externa():
    x = "enclosing"

    def interna():
        x = "local"
        print(x)  # Busca en el namespace local.

    interna()
    print(x)  # Busca en el namespace enclosing.

externa()
print(x)  # Busca en el namespace global.
