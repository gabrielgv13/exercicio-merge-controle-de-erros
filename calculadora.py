"""
Calculadora de Preço Total de Produto
Módulo para cálculo de preço com desconto e imposto
"""


def calcular_preco_total(preco_base, quantidade):
    """
    Calcula o preço total de um produto.
    
    Args:
        preco_base (float): Preço unitário do produto
        quantidade (int): Quantidade de itens
    
    Returns:
        float: Preço total calculado
    """
    return preco_base * quantidade
