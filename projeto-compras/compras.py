print("Bem-vindo ao programa de compras!")
print("Este programa irá ajudá-lo a gerenciar suas compras.")

compras = ["Maçã", "Banana", "Laranja"]

def adicionar_item(item):
    compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")

print("Lista de compras atual:")
print(compras)

while True:
    novo_item = input(
        "Digite um item para adicionar "
        "(ou 'sair' para encerrar): "
    ).strip()

    if novo_item.lower() == "sair":
        break

    adicionar_item(novo_item)

print("Lista de compras final:")
print(compras)
print("Total de itens:", len(compras))