def juros_simples(juros, capital, tempo):
    '''Calcula o montante final utilizando juros simples. Onde: M (montante final), C (capital inicial), i (taxa de juros) e t (tempo).'''
    montante = capital + (capital * juros * tempo)
    return montante

def juros_compostos( juros, capital, tempo):
    '''Calcula o montante final utilizando juros compostos. Onde: M (montante final), C (capital inicial), i (taxa de juros) e t (tempo).'''
    montante = capital * (1 + juros) ** tempo
    return montante

def desconto(valor_inicial, percentual_desconto):
    '''Calcula o valor final de um produto após aplicar um desconto percentual. Onde: Vf (valor final), Vi (valor inicial) e d (percentual de desconto).'''
    valor_final = valor_inicial - (valor_inicial * percentual_desconto / 100)
    return valor_final

def aumento(valor_inicial, percentual_aumento):
    '''Calcula o valor final após aplicar um aumento percentual. Onde: Vf (valor final), Vi (valor inicial) e a (percentual de aumento).'''
    valor_final = valor_inicial + (valor_inicial * percentual_aumento / 100)
    return valor_final

def parcela(valor_total, numero_parcelas):
    '''Calcula o valor de cada parcela de um financiamento simples. Onde: P (valor da parcela), V (valor total financiado) e n (número de parcelas).'''
    valor_parcela = valor_total / numero_parcelas
    return valor_parcela