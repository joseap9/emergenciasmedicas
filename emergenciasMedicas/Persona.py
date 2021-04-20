class Persona:

    def __init__(self,n,e,s,d):
        self.nombre = n
        self.edad = e
        self.sexo = s
        self.direccion = d

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        self.sexo = sexo

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getSexo(self):
        return self.sexo

    def getDireccion(self):
        return self.direccion

    def __str__(self):
        return self.nombre + "\n" + str(self.edad) + "\n" + self.sexo + "\n" + self.direccion