from sympy import symbols, diff

def uncertainty(func,variables,uncertainties):
    val = 0
    for x,u in zip(variables,uncertainties):
        val += (diff(func,x)*u)**2
    val = (val)**0.5
    return val

print("Esta é uma calculadora de incerteza. Se você possui uma variável Y que depende de outras, que possuem incertezas,\npode-se calcular a incerteza de Y a partir da fórmula da incerteza padrão combinada.")
print("Certifique-se de inserir os dados corretamente, usando sempre as mesmas unidades para cada grandeza, utilizando . como separador decimal")
print("e escrevendo a fórmula no formato Python, sempre utilizando * em uma multiplicação ou ** em exponenciação e parênteses quando necessário, por exemplo.")

variables = input("\nDigite o nome/símbolo de suas variáveis, separadas somente por espaços: ").split()
print(f"{len(variables)} variáveis inseridas: {', '.join(variables)}",end='\n\n')

values = []
uncertainties = []
for x in variables:
    values.append(float(input(f"Digite o valor de {x}: ")))
    uncertainties.append(float(input(f"Digite a incerteza de {x}: ")))
    print()

varlist = []
for x in variables:
    exec(f"{x} = symbols('{x}')")
    exec(f"varlist.append({x})")

f = input("Digite a fórmula da variável cuja incerteza se quer achar: ")
exec(f"f = {f}")

print()
print("A incerteza da variável é:",uncertainty(f,varlist,uncertainties).subs(zip(varlist,values)))

print()
input("Pressione ENTER para fechar")