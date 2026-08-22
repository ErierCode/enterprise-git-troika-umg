"""Servicio mínimo para laboratorio Git."""


def register_patient(name: str, document: str) -> dict:
    if not name.strip():
        raise ValueError("El nombre es obligatorio")
    if not document.strip():
        raise ValueError("El documento es obligatorio")
    return {"name": name.strip(), "document": document.strip(), "status": "ACTIVE"}
