
############################
# Tipos de atributos:
#    - Atributo de método - Escopo: Método;
#    - Atributo de instância - Escopo: Apenas o objeto instânciado;
#    - Atributo de classe - Escopo: Todos os objetos da classe.
############################


class MinhaClasse():
    # Declaração de um atributo de CLASSE
    # Sem uso do 'self' e FORA de qualquer método.
    #
    # O atributo de classe existe:
    #       (escopo) - dentro da classe em que foi declarado e
    #       (tempo de vida) - enquanto a classe estiver declarada/importada.
    #
    # Não é necessário instânciar o objeto para acessar o atributo.
    atributo_de_classe = 'atributo_de_classe'

    def __init__(self):
        # Declaração de um atributo de INSTÂNCIA
        # Repare no uso do 'self.'.
        # O self é uma referência ao próprio objeto.
        #
        # O atributo de instância só existe:
        #       (escopo) - dentro do objeto em que foi declarado e
        #       (tempo de vida) - enquanto o objeto estiver instânciado.
        self.atributo_de_instancia = 'atributo_de_instancia'

    def print_attr(self):
        print('Imprimindo atributos:')
        # Declaração de atributo de MÉTODO
        # Sem uso do 'self.' e DENTRO de algum método.
        #
        # O atributo de método só existe:
        #       (escopo) - dentro do método em que foi declarado e
        #       (tempo de vida) - enquanto o método estiver sendo executado.
        atributo_de_metodo = 'atributo_de_metodo'

        # Acessando atributo de Classe
        # Repare no uso do 'self.' para acessar o atributo.
        #
        # Os atributos de classe são compartilhados
        # entre todos os objetos deste tipo.
        print('\t', self.atributo_de_classe)

        # Acessando atributo de Instância
        # Repare no uso do 'self.' para acessar o atributo.
        print('\t', self.atributo_de_instancia)
        # Acessando atributos de Método
        # Sem uso do 'self.'.
        print('\t', atributo_de_metodo)


# Não é necessário instânciar objetos para acessar atributos de Classe.
print('\nImprimindo atributos de Classe:\n')
print(MinhaClasse.atributo_de_classe)
# Não é possível acessar atributos de instância ou método
# sem instânciar objetos.
# print(MinhaClasse.atributo_de_instancia)

# Instânciado objetos.
MC1 = MinhaClasse()
MC2 = MinhaClasse()

# Executando métodos que acessam os atributos de classe, instância e método.
print('\nImprimindo objetos:\n')
MC1.print_attr()
MC2.print_attr()

# Acessando externamente atributos de classe.
#
# Notar que: esta operação irá alterar todos os objetos do tipo da classe.
#
# Usando um objeto.
MC1.__class__.atributo_de_classe = 'Olá '
# Usando a classe.
MinhaClasse.atributo_de_classe += 'Mundo!'

# Acessando externamente atributos de Instância.
#
# Notar que: esta operação irá alterar somente o objeto referenciado.
MC1.atributo_de_instancia = 'atributo_de_instancia_ALTERADO'

# Executando métodos que acessam os atributos de classe, instância e método.
print('\nImprimindo atributos:\n')
MC1.print_attr()
MC2.print_attr()

print('\nImprimindo Dicionários:\n')

print(MinhaClasse.__dict__)
print(MC1.__class__.__dict__)
print(MC2.__class__.__dict__)
print(MC1.__dict__)
print(MC2.__dict__)
