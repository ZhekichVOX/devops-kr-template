# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Валидация номера телефона."""
    import re
    cleaned = phone.replace('-', '').replace(' ', '')
    return re.fullmatch(r'\+?7[0-9]{10}', cleaned) is not None
