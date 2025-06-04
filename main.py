import string, random

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range (comprimento))
    return senha

passsword = gerar_senha(20)
print(passsword)