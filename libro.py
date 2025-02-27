class Libro:
    def __init__(self, titulo, autor, genero, isbn):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn

    def info(self):
        return f"El libro '{self.titulo}' fue escrito por {self.autor}, pertenece al género {self.genero} y su ISBN es {self.isbn}."
    
    def prestar(self):
        return f"El libro '{self.titulo}' ha sido prestado."

    def devolver(self):
        return f"El libro '{self.titulo}' ha sido devuelto."

    def disponible(self):
        self.disponible = True
        return f"El libro '{self.titulo}' está disponible."