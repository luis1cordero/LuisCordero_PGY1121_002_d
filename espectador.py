class espectador:
    rut = 0
    nombre = ''
    apellido = ''
    edad = 0
    valor=0

    def __init__(self):
        self.rut = 11111111
        self.nombre = 'Luis'
        self.apellido = 'Cordero'
        self.edad = 20
        self.valor=50000
    def setRut(self,rut):
        if not rut.isnumeric():
            print("el rut sin punto,guion ni digito verificador, solo numeros")
            return False
        if len(rut) < 7 and len(rut)> 8:
            print("la longitud no es correcta")
            return False