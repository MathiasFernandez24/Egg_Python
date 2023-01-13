from typing import Optional


def usuario(nombre: str, actividad: Optional[bool] = None) -> str:
    mensaje: str = f"{nombre.upper()}: {actividad}"
    return mensaje


situacion = usuario("administrador")
print(situacion)
