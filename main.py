from Modules.classes import Futbolista, Entrenador, Masajista
# from Modules.actions import viajar, concentrar, jugar
import Modules.actions as act

delantero_vidal = Futbolista(23, "Arturo", "Vidal", 37, 23, "delantero")
arquero_bravo = Futbolista(1, "Claudio", "Bravo", "38", 1, "Portero")
director_bielsa = Entrenador(100, "Marcelo", "bielsa", 69, 5745)
masajista_perez = Masajista(200, "juan", "Perez", 35, "Fisiologo", 12)

equipo = [delantero_vidal, arquero_bravo, director_bielsa, masajista_perez]
jugadores = [delantero_vidal, arquero_bravo]
entrenadores = [director_bielsa]
masajistas = [masajista_perez]

act.concentrar(equipo)
print()
act.dirigir_entrenamiento(entrenadores)
print()
act.entrenar(jugadores)
print()
act.viajar(equipo)
print()
act.dirigir_partido(entrenadores)
print()
act.jugar(jugadores)
print()
act.masajear(masajistas)
print()
