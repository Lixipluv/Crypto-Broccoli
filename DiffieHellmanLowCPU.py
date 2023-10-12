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

a = 7  # Chave privada de Alice
b = 3  # Chave privada de Bob

# Cálculo das chaves públicas
A = mod_exp(g, a, p)  # Chave pública de Alice
B = mod_exp(g, b, p)  # Chave pública de Bob

# Troca de chaves públicas (em uma comunicação real, isso seria feito por meio de um canal seguro)
# Supondo que Alice recebe a chave pública de Bob e vice-versa

# Cálculo das chaves compartilhadas
shared_key_alice = mod_exp(B, a, p)  # Chave compartilhada de Alice
shared_key_bob = mod_exp(A, b, p)  # Chave compartilhada de Bob

# Verificação de que ambas as partes calcularam a mesma chave compartilhada
assert shared_key_alice == shared_key_bob

print("Chave compartilhada (Alice):", shared_key_alice)
print("Chave compartilhada (Bob):", shared_key_bob)
