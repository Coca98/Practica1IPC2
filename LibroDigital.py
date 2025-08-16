from MaterialBiblioteca import MaterialBiblioteca

class LibroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, tamano, estado="disponible"):
        super().__init__(titulo, autor, codigo, estado)
        self.tamano=tamano

    def getTamano(self):
        return self.tamano
    
    def setTamano(self, tamano):
        self.tamano = tamano

    def informacion(self):
        return ("TTitulo:" + str(self.getTitulo()) +
                "\nAutor: " + str(self.getAutor()) +
                "\nCodigo: " + str(self.getCodigo()) +
                "\nTamano: " + str(self.getTamano()) +
                "\nEstado: " + str(self.getEstado()))