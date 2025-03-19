# sintacticoConLed.py

def valida_cadena(cadena):
    if not cadena.startswith(('mover', 'prender', 'reversa', 'avanzar', 'apagar')):
        return False

    if cadena.startswith('mover'):
        if not any(cadena.endswith(direccion) for direccion in ['derecha', 'izquierda']):
            return False

    if cadena.startswith('prender') or cadena.startswith('apagar'):
        if 'cocina' not in cadena:
            return False

    # Se verifica que no haya más de dos palabras en la cadena
    if len(cadena.split()) > 2:
        return False

    return True
