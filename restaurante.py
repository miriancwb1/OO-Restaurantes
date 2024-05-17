class Restaurante:
    restaurantes = []


    def __init__ (self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False 
        Restaurante.restaurantes.append(self)


    def __str__(self):
        
        return  f'{self.nome} | {self.categoria}'
    
    
    def listar_restaurante():
        print(f'{'nome do restaurante'.just(25)} | {"categoria". ijust (25)} | {"status"}
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(24)} |{restaurante.categoria} | {restaurante.ativo}')
    @property
    def ativo (self):
        return '⌧' if self._ativo else '☐' 
    
    

restaurante_praca = Restaurante( 'prca','gourmet')

restaurantes_pizza = Restaurante('pizza','italiana')


Restaurante.listar_restaurante()


