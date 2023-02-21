class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "org", "net"]

while True:
    email = input().split("@")
    if len(email) < 2:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    data = email[1].split(".")
    domain = data[1]
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
