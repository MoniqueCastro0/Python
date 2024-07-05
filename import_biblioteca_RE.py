import re #expressoes regulares

maiuscula = (re.search("[A-Z]", "Senha"))
print(re.search("[a-z]", "senha"))
print(re.search("[0-9]", "senha"))

print(maiuscula)

