class restaurante:
    def __init__ (self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False 
    def __str__(self):
        
        return  f'{self.nome} | {self.categoria}'

restaurante_praca = restaurante( 'prca','gourmet')

restaurantes_pizza = restaurante('pizza','italiana')

restaurantes = [restaurantes_pizza, restaurante_praca]

print (restaurante_praca)
print (restaurantes_pizza)


