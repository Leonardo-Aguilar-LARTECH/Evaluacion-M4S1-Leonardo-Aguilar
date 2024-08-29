def viajar(equipo):
    for integrante in equipo:
        print(integrante.viajar())

def concentrar(equipo):
    for integrante in equipo:
        print(integrante.concentrar())

def jugar(futbolistas):
    for jugador in futbolistas:
        print(jugador.jugarPartido())

def entrenar(futbolistas):
    for jugador in futbolistas:
        print(jugador.entrenar())

def dirigir_partido(entrenadores):
    for entrenador in entrenadores:
        print(entrenador.dirigirPartido())

def dirigir_entrenamiento(entrenadores):
    for entrenador in entrenadores:
        print(entrenador.dirigirEntrenamiento())

def masajear(masajistas):
    for masajista in masajistas:
        print(masajista.darMasaje())