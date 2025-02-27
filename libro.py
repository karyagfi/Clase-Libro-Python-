class Libro:
    def __init__(self, titulo = "Sin titulo", autor = "Sin autor", genero = "Sin genero", isbn = "Sin isbn"):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
        self.disponible = True

    def info(self):
        print(f"El libro '{self.titulo}' fue escrito por {self.autor}, pertenece al género {self.genero} y su ISBN es {self.isbn}.")
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")

    def disponible(self):
        self.disponible = True
        return f"El libro '{self.titulo}' está disponible."