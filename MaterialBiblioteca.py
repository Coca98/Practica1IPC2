from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor, codigo, estado):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.estado = estado

    def getTitulo(self):
        return self.titulo
    def setTitulo(self, titulo):
        self.titulo = titulo
    def getAutor(self):
        return self.autor
    def setAutor(self, autor):
        self.autor = autor
    def getCodigo(self):
        return self.codigo
    def setCodigo(self, codigo):
        self.codigo = codigo
    def getEstado(self):
        return self.estado
    def setEstado(self, estado):
        self.estado = estado

    @abstractmethod
    def informacion(self):
        pass