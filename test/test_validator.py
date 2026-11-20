from validator import validate_email, validate_phone

# tests/test_validator.py
def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False

def test_validate_phone():
    assert validate_phone("+79991234567")
    assert validate_phone("7 999-123-45-67")
    assert not validate_phone("+7999123456")
    assert not validate_phone("+79991234567\n")
