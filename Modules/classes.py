class Persona:
    def __init__(self, id: int, nombre: str, apellidos:str, edad:int):
        self._id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    @property #permite transformar funcion en propiedad, para restingir acceso y modificacion
    def id(self):
        return str(self._id).zfill(3)
    
    @id.setter
    def id(self, id):
        return ""
    
    def concentrar(self):
        return f"{self.nombre} {self.apellidos}, ha ingresado al complejo deportivo para iniciar la concentracion previa al partido"
    
    def viajar(self):
        return f"{self.nombre} {self.apellidos}, se encuentra viajando al recinto del proximo partido"

class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion
        
    def jugarPartido(self):
        return f"el {self.demarcacion} {self.nombre} {self.apellidos}, esta jugando el partido con la camieta {self.dorsal}"
    
    def entrenar(self):
        return f"el {self.demarcacion} {self.nombre} {self.apellidos}, inicia su entrenamiento"

class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)
        self.idFederacion = idFederacion
    
    def dirigirPartido(self):
        return f"el entrenador {self.id} {self.nombre} {self.apellidos}, está dirigiendo el partido del equipo"
    
    def dirigirEntrenamiento(self):
        return f"el entrenador {self.nombre} {self.apellidos}, está dirigiendo el entrenamiento, en la concentracion del equipo"

class Masajista(Persona):
    def __init__(self, id, nombre, apellidos, edad, titulacion, annosDeExperiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annosDeExperiencia = annosDeExperiencia
        
    def darMasaje(self):
        return f"el masajista {self.nombre} {self.apellidos}, se encuentra dando masajes"