nomeProdutos = ["Amaciante", "Detergente", "Desinfetante", "Sabão"]
precoProdutos = [14, 3, 5, 20]
qtdProduto = [5, 8, 3, 10]


def imprimirProduto(indice):
    print("VISUALIZAÇÃO DO PRODUTO:"
        "\nProduto - ",nomeProdutos[indice],
        " Preço - ", precoProdutos[indice],
        " Quantidade - ", qtdProduto[indice])

def removerProdutoEspecifico(indice):
    nomeProdutos.pop(indice)
    precoProdutos.pop(indice)
    qtdProduto.pop(indice)
    print("PRODUTO REMOVIDO:"
        "\nPRODUTOS: ", nomeProdutos,
        "\nPREÇOS: ", precoProdutos,
        "\nQUANTIDADE: ", qtdProduto)

posProd = 2
removProd = 0

imprimirProduto(posProd)
removerProdutoEspecifico(removProd)