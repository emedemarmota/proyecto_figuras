import math
def get_area(radio:float)->float:
    if radio <0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi*radio**2

