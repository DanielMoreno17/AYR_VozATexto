

"""
Reglas sintacticas:
    1.- Empieza con: mover, prender, reversa, avanzar
    2.- despues de mover, deber ir: {derecha, izquierda}
    3.- despues de prender/apagar, debe ir un lugar... {cocina}
    4.- reversa/avanzar no debe tener alguna instruccion adicional
    5.- Solo puede haber una instruccion por comando!

"""

def valida_cadena(cadena):
    if not cadena.startswith(('mover', 'prender', 'reversa', 'avanzar')):
        return False

    if cadena.startswith('mover'):
        if not any(cadena.endswith(direccion) for direccion in ['derecha', 'izquierda']):
            return False

    if cadena.startswith('prender') or cadena.startswith('apagar'):
        if 'cocina' not in cadena:
            return False

    # Verifica que no haya más de dos palabras en la cadena
    if len(cadena.split()) > 2:
        return False

    return True




