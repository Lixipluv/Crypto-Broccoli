import random
import math

# Função para gerar números primos grandes usando o teste de Miller-Rabin
def gerar_primos_grandes(tamanho_bits, k=40):
    while True:
        num = random.getrandbits(tamanho_bits)
        if eh_primo_miller_rabin(num, k):
            return num

# Função para verificar se um número é primo usando o teste de Miller-Rabin
def eh_primo_miller_rabin(num, k):
    if num <= 1:
        return False
    if num <= 3:
        return True

    # Escreva n como 2^r * d + 1
    r, d = 0, num - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Execute o teste de Miller-Rabin k vezes
    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True

# Função para calcular o inverso modular
def inverso_modular(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Função para gerar chaves
def gerar_chaves(tamanho_bits):
    p = gerar_primos_grandes(tamanho_bits)
    q = gerar_primos_grandes(tamanho_bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Escolher um número e que seja coprimo com phi
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calcular o inverso modular de e
    d = inverso_modular(e, phi)

    return (n, e), (n, d)

# Função para criptografar
def criptografar(chave_publica, mensagem):
    n, e = chave_publica
    mensagem_criptografada = [pow(ord(char), e, n) for char in mensagem]
    return mensagem_criptografada

# Função para descriptografar
def descriptografar(chave_privada, mensagem_criptografada):
    n, d = chave_privada
    mensagem_descriptografada = [chr(pow(char, d, n)) for char in mensagem_criptografada]
    return ''.join(mensagem_descriptografada)

# Exemplo de uso
if __name__ == "__main__":
    chave_publica, chave_privada = gerar_chaves(128)  # Tamanho da chave em bits
    mensagem = "Crypto-Broccoli"

    mensagem_criptografada = criptografar(chave_publica, mensagem)
    print("Mensagem criptografada:", mensagem_criptografada)

    mensagem_descriptografada = descriptografar(chave_privada, mensagem_criptografada)
    print("Mensagem descriptografada:", mensagem_descriptografada)
