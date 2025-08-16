from MaterialBiblioteca import MaterialBiblioteca

class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, ejemplar, estado="disponible"):
        super().__init__(titulo, autor, codigo, estado)
        self.ejemplar=ejemplar

    def getEjemplar(self):
        return self.ejemplar
    
    def setEjemplar(self, ejemplar):
        self.ejemplar = ejemplar

    def informacion(self):
        return ("Titulo: " + str(self.getTitulo()) +
                " Autor: " + str(self.getAutor()) +
                " Codigo: " + str(self.getCodigo()) +
                " Ejemplar: " + str(self.getEjemplar()) +
                " Estado: " + str(self.getEstado()))
