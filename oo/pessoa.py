'''
Aqui será abordado a Orientação a Objeto: Classe, Métodos, Atributos.

Classe:
* É um molde de instruções contendo um motivo central com sub-propriedades e métodos para chamadas de aplicação;
* É a base da orientação a objetos;
* Define a forma como objetos python se comportam;
* Cada propriedade e método interno podem serem chamados individualmente;
* É definido com iniciais maiúsculas e CamelCase;
* Precisa ser iniciada no método (__init__).
* Precisa ser instanciada para aplicação;
* Ela deve ser dinâmica.

Mais sobre classe:
https://www.youtube.com/embed/cV_Soy7jGns
https://www.youtube.com/embed/gtgI7PC_TJk
https://www.youtube.com/watch?v=j6B8shHXzks
https://pt.wikipedia.org/wiki/Classe_(programa%C3%A7%C3%A3o)

Atributos:
1.Métodos de instância def(self).
* Métodos de instância são funções com atributos de dados que definem a classe (objeto).
* Os métodos devem conter a palavra chave "Self" como primeiro parâmetro, sendo isolado ou não.
* O método principal deve ser iniciado com o atributo (__init__).
* Métodos também são considerados atributos.

Artigo sobre o uso do Self: http://archive.is/cX2mq

2.Atributos de Dados (self.)
* São instâncias (objetos) conectados aos parâmetros dos métodos;
* Cada atributo de dado é uma instância (objeto)
* Permitem serem utilizados individualmente;

3-Método e atributos de Classe x Métodos e atributos de instância:

Método e atributos de Classe - Métodos e atributos diretamente a classe, fora do escopo
dos métodos de instâncias 'self'.

Métodos e atributos de instância - Métodos e atributos diretamente aos métodos de instâncias
do objeto, com as palavras chave 'self'.
'''


'Criando uma classe e definindo métodos e atributos:'
# Usar Camel Case em caso de duas palavras.


# Construindo uma Classe (Objeto) que define uma Pessoa:
class Pessoa:
    # Local apenas para atributos de dados da classe.
    # São atributos globais para uso;
    # Economizam memória;
    # Podem ser tipos, containers, dicionários;
    olhos = 2

    # Métodos de instância do objeto Pessoa.
    # Inicialização a Classe Pessoa com seus atributos:
    def __init__(self, *filhos, nome="None", idade=40):
        self.idade = idade  # Atributo de dado
        self.nome = nome    # Atributo de dado
        self.filhos = list(filhos) # Atributo de dado com lista.

    def cumprimentar(self):
        return f'Olá {id(self)}'

    # Métodos atreladas apenas a Classe. Não dependentes dos métodos de instância:
    # Estático - Não necessita parâmetros.
    @staticmethod
    def metodo_estatico():
        return "Método Estático"

    # Método para manipular apenas os atributos de dados direto da Classe:
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

# Manipulando os atributos de dados dos métodos de instância da Classe:
if __name__ == '__main__':
    # Instanciando um novo objeto atribuindo a classe e iniciando para manipulação:
    jeferson = Pessoa(nome='Jeferson')
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

    # Manipulando apenas os atributos globais da Classe:
    print(f'Toda pessoa tem {Pessoa.olhos} olhos')
    print(f'O meu cachorro {pingo.nome}, tem {pingo.olhos} olhos.')
    print(f'O {jeferson.nome}, tem {jeferson.olhos} olhos.')
    print(id(jeferson.nome), id(pingo.nome))
    # Atributo da classe sempre possui o mesmo ID:
    print(id(jeferson.olhos), id(pingo.olhos))

    # Alternado atributo de classe e instanciando apenas ao método:
    pingo.olhos = 1
    print(pingo.__dict__)
    # Atributo da classe com novo ID a cada modificação:
    print(id(jeferson.olhos), id(pingo.olhos))

    # Manipulando métodos de classe.
    # @staticmethod - Manipula dados livremente, não necessita de parâmetros.
    print(Pessoa.metodo_estatico(), pingo.metodo_estatico())

    # @classmethod - Manipula atributos da classe:
    print(Pessoa.nome_e_atributos_de_classe(), pingo.nome_e_atributos_de_classe())