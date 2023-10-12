# Função para calcular o módulo exponencial de forma eficiente (a^b mod m)
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus  # Reduzimos a precisão aqui
        exponent //= 2
    return result

# Geração de chaves privadas aleatórias para Alice e Bob
p = 23  # Um número primo menor para reduzir o uso de CPU
g = 5

# O "homem do meio" intercepta as chaves públicas de Alice e Bob
a = 7  # Chave privada de Alice
b = 3  # Chave privada de Bob
A = mod_exp(g, a, p)  # Chave pública de Alice

# "Homem do meio" intercepta a chave pública de Alice e envia sua própria chave pública falsa
fake_A = 999  # Chave pública falsa do "homem do meio"

# Bob recebe a chave pública falsa do "homem do meio"
B = mod_exp(g, b, p)  # Chave pública de Bob

# "Homem do meio" intercepta a chave pública de Bob e envia sua própria chave pública falsa
fake_B = 888  # Chave pública falsa do "homem do meio"

# Alice recebe a chave pública falsa do "homem do meio"

# Cálculo das chaves compartilhadas
shared_key_alice = mod_exp(fake_B, a, p)  # Chave compartilhada de Alice (calculada usando a chave pública falsa do "homem do meio")
shared_key_bob = mod_exp(fake_A, b, p)  # Chave compartilhada de Bob (calculada usando a chave pública falsa do "homem do meio")

# "Homem do meio" tem acesso às chaves compartilhadas

# O "homem do meio" pode agora interceptar e decifrar todas as comunicações entre Alice e Bob

print("Chave compartilhada (Alice):", shared_key_alice)
print("Chave compartilhada (Bob):", shared_key_bob)
