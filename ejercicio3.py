from fastapi import FastAPI


app = FastAPI()


# Creacion de clase videojuego
class VideoJuego:
    titulo = ''
    genero = ''
    lanzamiento = ''
    
    def __init__(self, titulo, genero, lanzamiento) :
        self.titulo = titulo
        self.genero = genero
        self.lanzamiento = lanzamiento
        print('Se creo el juego: ', self.titulo)

    # Se modifica el metodo string
    def __str__(self):
        return '{} ({})'.format(self.titulo ,self.lanzamiento)

# Creacion de clase catalogo.
class Catalogo:
    videoJuegos = []


    def __init__ (self, videoJuegos=[]):
        self.videoJuegos = videoJuegos


    # Metodo para agregar videojuegos a la lista.
    def agregar(self, vj):
        self.videoJuegos.append(vj)

    # Metodo para mostrar esos videojuegos.
    def mostrar(self):
        for vj in self.videoJuegos:
            print(vj)



vj = VideoJuego("Halo", "Shooter", "01-01-99")
c = Catalogo([vj])

c.agregar(VideoJuego("Half Life", "Shooter", "01-01-99"))
c.agregar(VideoJuego("League of legends", "Shooter", "05-10-09"))
c.agregar(VideoJuego("Dota", "Shooter", "17-11-12"))
c.agregar(VideoJuego("Counter-Strike", "Shooter", "30-01-99"))


c.mostrar()