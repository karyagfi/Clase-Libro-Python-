from libro import Libro

libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", "978-8478884452")
libro2 = Libro("La sombra del viento", "Carlos Ruiz Zafón", "Misterio", "978-8408079545")
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "978-8478887200")
libro4 = Libro("Fahrenheit 451", "Ray Bradbury", "Ciencia ficción", "978-1451673319")
libro5 = Libro("Crimen y castigo", "Fiódor Dostoyevski", "Novela psicológica", "978-8420664206")

print(libro1.info())
print(libro1.prestar())
print(libro1.devolver())
print(libro1.disponible())

print(libro2.info())
print(libro2.prestar())
print(libro2.devolver())
print(libro2.disponible())

print(libro3.info())
print(libro3.prestar())
print(libro3.devolver())
print(libro3.disponible())

print(libro4.info())
print(libro4.prestar())
print(libro4.devolver())
print(libro4.disponible())

print(libro5.info())
print(libro5.prestar())
print(libro5.devolver())
print(libro5.disponible())