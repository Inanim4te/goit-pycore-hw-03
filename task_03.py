import re

def normalize_phone(phone_number):
    normalized_number = re.sub(r'[^\d+]', '', phone_number)

    if not normalized_number.startswith('+38'):
        if normalized_number.startswith('38'):
            normalized_number = '+' + normalized_number
        else:
            normalized_number = '+38' + normalized_number

    return normalized_number