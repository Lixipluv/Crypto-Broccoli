import random
import math

# Função para calcular o módulo exponencial de forma eficiente (a^b mod m)
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base ** 2) % modulus
        exponent //= 2
    return result

# Geração de números primos grandes (p) - idealmente, isso deve ser feito de forma mais segura
def generate_large_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if all(p % n != 0 for n in range(2, int(math.sqrt(p)) + 1)):  # Verifica se p não é divisível por primos até a raiz quadrada de p
            return p

# Função para gerar uma chave privada aleatória
def generate_private_key(p):
    return random.randint(2, p - 2)

# Geração de chaves privadas aleatórias para Alice e Bob
bits = 256  # Tamanho do número primo, quanto maior, mais seguro
p = generate_large_prime(bits)
g = random.randint(2, p - 2)  # 2 <= g <= p-2

a = generate_private_key(p)  # Chave privada de Alice
b = generate_private_key(p)  # Chave privada de Bob

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


