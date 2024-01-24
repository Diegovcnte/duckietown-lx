from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    res[shape[0]//2:, :] = 1
    
    # :, = indica que queremos todos los elementos de la parte Y de la matriz
    # shape[1] = indica que queremos todas las columnas de la tupla pasada
    # //2 = el cociente de la mitad de todas las columnas será la mitad de la matriz y además será redondeado
    # shape[1]//2: = indica que queremos todos las columnas desde shape[1]//2 hasta el final o sea la parte derecha de la matriz

    #SI DETECTO ALGO EN EL LADO DERECHO INFLUIRÉ EN MI MOTOR IZQUIERDO

    """ 
    Enfoque anterior para que no se olvide:
    
    res[100:150, 100:150] = 1

    o

    res[100:150, 100:300] = -1

    En este enfoque nos limitabamos a secciones específicas dentro de una matriz. Se cambió por un enfoque
    que tomara en cuenta el tamaño total de la matriz dinámicamente


    """

    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    res[:,:shape[1]//2] = 0
    res[100:250, 100:400] = -1
    # :, = indica que queremos todos los elementos de la parte Y de la matriz
    # shape[1] = indica que queremos todas las columnas de la tupla pasada
    # //2 = el cociente de la mitad de todas las columnas será la mitad de la matriz y además será redondeado
    # :shape[1]//2 = indica que queremos todos las columnas desde el inicio hasta antes de shape[1]//2 o sea parte izquierda de la matriz

    #SI DETECTO ALGO EN EL LADO DERECHO INFLUIRÉ EN MI MOTOR DERECHO


    return res


"""

 la matriz de peso es un indicador, como en el motor izquierdo agregue peso al lado derecho, 
 este motor izquierdo actuará si se cumple ese peso en el lado derecho de la imagen 

 """
