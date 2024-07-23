def split_string(s, delimiter=' '):
    parts = s.split(delimiter, maxsplit=2)
    first = parts[0] if len(parts) > 0 else None
    second = parts[1] if len(parts) > 1 else None
    rest = parts[2] if len(parts) > 2 else None

    return first, second, rest

def validate_email(email):
    # rule 1 must contain username, @ , website, ., extension
    username, rest, extra = split_string(email, '@')
    if extra or not username or not rest:
        return False
    
    website, extension, extra = split_string(rest, '.')
    if extra or not website or not extension:
        return False
    
    # username can only contain letters, digits, dashes and underscores
    if not all(char.isalnum() or char in {'_','-'} for char in username):
        return False
    
    # website can only have letters and digits
    if not all(char.isalnum() for char in website):
        return False
    
    if len(extension) > 3:
        return False
    
    return True

def validation_emails():
    N = int(input())
    emails = []
    for _ in range(N):
        emails.append(str(input()))
    
    result = list(filter(validate_email, emails))
    result.sort()
    return result

if __name__ == '__main__':
    print(validation_emails())