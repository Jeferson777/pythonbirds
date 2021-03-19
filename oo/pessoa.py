'''
Aqui será abordado a Orientação a Objeto: Classe, Métodos, Atributos.

Classe:
*É um molde de instruções contendo um motivo central com sub-propriedades e métodos para chamadas de aplicação;
*É a base da orientação a objetos;
*Define a forma como objetos python se comportam;
*Cada propriedade e método interno podem serem chamados individualmente;
*É definido com iniciais maiúsculas e CamelCase;
*Precisa ser iniciada no método (__init__).
*Precisa ser instanciada para aplicação;
*Ela deve ser dinâmica.

Mais sobre classe:
https://www.youtube.com/embed/cV_Soy7jGns
https://www.youtube.com/embed/gtgI7PC_TJk
https://www.youtube.com/watch?v=j6B8shHXzks
https://pt.wikipedia.org/wiki/Classe_(programa%C3%A7%C3%A3o)

Atributo - Métodos:
*Métodos são funções construidas e pertencentes a uma classe.
*Cada função ou método contém suas próprias funcionalidade.
*Os métodos devem conter a palavra chave "Self" como primeiro parâmetro, sendo isolado ou não.
*Instanciamentos e objetos, se definem apenas ao método iniciado (__init__).
*Métodos também são atributos.


Artigo sobre o uso do Self: http://archive.is/cX2mq

Atributo de Dados:
*São instânciamentos individuais de parâmetros nos métodos;
*Podem receberem valores e serem chamados individualmente;
*São considerados objetos.
'''


'Criando uma classe e definindo métodos e atributos:'
# Usar Camel Case em caso de duas palavras.


# Construindo uma Classe (Objeto):
class Pessoa:
    # Criando um método iniciando a classe:
    def __init__(self, *filhos, nome="None", idade=40):
        self.idade = idade  # Atributo de dado
        self.nome = nome    # Atributo de dado
        self.filhos = list(filhos) # Atributo de dado com lista.

    # Construindo um Método
    def cumprimentar(self):
        return f'Olá {id(self)}'


# Aplicando orientação a objeto:
if __name__ == '__main__':
    jeferson = Pessoa(nome='Jeferson') # Atribuindo o objeto, passando um dado de parâmetro. Aqui ele é iniciado.
    print(jeferson.nome)
    pingo = Pessoa(jeferson, nome='Pingo')
    print(id(pingo))
    print(pingo.cumprimentar()) # Modo correto.
    print(pingo.nome) # Imprimindo o atributo nome da classe Pessoa.
    print(pingo.idade)

    for filho in pingo.filhos:
        print(filho.nome)

    # Criando Atributos dinamicamente em tempo de execução.
    # Aconselhável apenas para momentos isolados, pois o ideal é instanciar em um método na classe.
    pingo.sobrenome = 'P. Pingous'
    print(pingo.sobrenome)
    # Removendo o atributo dinamicamente:
    del pingo.sobrenome
    # Atributo especial __dict__, permite verificar todos os atributos de instância na classe:
    print(jeferson.__dict__)
    print(pingo.__dict__)