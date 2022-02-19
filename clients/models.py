from uuid import uuid4 #Nos permite generar uuid únicos. uuid4 es el estandar de la industria


class Client:

    def __init__(self, name, company, email, position, id=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.id = id or uuid4() #si no nos dan un id entonces usamos un uuid4

    def to_dict(self):
        #vars revisa lo que regresa __dict__ y accede a una representación como dict de nuestro objeto
        return vars(self) #

    @staticmethod #nos permite declarar un método estático dentro de la clase
    #un método estático se puede ejecutar sin necesidad de una instacia de clase
    def schema():
        return ['name', 'company', 'email', 'position', 'id']
        #se retorna la representación columnar de nuestro objeto
        