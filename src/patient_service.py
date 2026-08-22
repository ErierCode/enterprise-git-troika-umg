"""Servicio mínimo para laboratorio Git."""

from datetime import datetime, timezone

MIN_NAME_LENGTH = 2
MIN_DOCUMENT_LENGTH = 5


def register_patient(name: str, document: str) -> dict:
    clean_name = " ".join(name.strip().split())
    clean_document = document.strip().upper()

    if len(clean_name) < MIN_NAME_LENGTH:
        raise ValueError("El nombre debe tener al menos 2 caracteres")
    if len(clean_document) < MIN_DOCUMENT_LENGTH:
        raise ValueError("El documento debe tener al menos 5 caracteres")
    if not clean_document.isalnum():
        raise ValueError("El documento solo puede contener letras y números")

    return {
        "name": clean_name,
        "document": clean_document,
        "status": "ACTIVE",
        "registered_at": datetime.now(timezone.utc).isoformat(),
    }
