from src.patient_service import register_patient

def test_register_patient():
    patient = register_patient("Ana López", "123456")
    assert patient["status"] == "ACTIVE"
