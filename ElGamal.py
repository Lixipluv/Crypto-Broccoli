import random

# Função para verificar se um número é primo usando o teste de Miller-Rabin
def eh_primo_miller_rabin(num, k=5):
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

# Função para gerar um número primo aleatório usando Miller-Rabin
def gerar_primo_miller_rabin(tamanho_bits, k=5):
    while True:
        num = random.getrandbits(tamanho_bits)
        # Certifique-se de que o número seja ímpar
        num |= 1
        if eh_primo_miller_rabin(num, k):
            return num

# Função para encontrar um gerador módulo p
def encontrar_gerador(p):
    for g in range(2, p):
        if pow(g, 2, p) != 1 and pow(g, (p - 1) // 2, p) != 1:
            return g
    return None

# Geração das chaves ElGamal com números primos p e g gerados por Miller-Rabin
def gerar_chaves(tamanho_bits):
    p = gerar_primo_miller_rabin(tamanho_bits)
    g = encontrar_gerador(p)

    if g is None:
        raise ValueError("Não foi possível encontrar um gerador válido.")

    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return (p, g, y), (p, x)

# Função para criptografar uma mensagem
def criptografar(chave_publica, mensagem):
    p, g, y = chave_publica
    k = random.randint(2, p - 2)
    a = pow(g, k, p)
    b = (pow(y, k, p) * mensagem) % p
    return a, b

# Função para descriptografar uma mensagem
def descriptografar(chave_privada, a, b):
    p, x = chave_privada
    mensagem = (b * pow(pow(a, x, p), -1, p)) % p
    return mensagem

# Função para recifrar uma mensagem cifrada
def recifrar(chave_publica, a, b, novo_k):
    p, g, y = chave_publica
    a_novo = pow(g, novo_k, p)
    b_novo = (b * pow(a, novo_k, p)) % p
    return a_novo, b_novo

# Exemplo de uso
if __name__ == "__main__":
    chave_publica, chave_privada = gerar_chaves(256)
    mensagem = "Crypto Broccoli"  # Mensagem a ser cifrada

    # Converte a mensagem em um número para evitar Tracbeack do python
    mensagem_numero = int.from_bytes(mensagem.encode(), 'big')

    a, b = criptografar(chave_publica, mensagem_numero)
    print("Mensagem criptografada (a, b):", (a, b))

    mensagem_descriptografada_numero = descriptografar(chave_privada, a, b)
    print("Mensagem descriptografada:", mensagem_descriptografada_numero)

    novo_k = random.randint(2, chave_publica[0] - 2)
    a_novo, b_novo = recifrar(chave_publica, a, b, novo_k)
    print("Mensagem recifrada (a_novo, b_novo):", (a_novo, b_novo))

    mensagem_recifrada_descriptografada_numero = descriptografar(chave_privada, a_novo, b_novo)
    print("Mensagem recifrada e descriptografada:", mensagem_recifrada_descriptografada_numero)
