import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "computador", "algoritmo", "jogo", "codigo"]

# Função para escolher uma palavra aleatória
def escolher_palavra():
    return random.choice(palavras)

# Função principal do jogo
def jogar():
    palavra = escolher_palavra()
    letras_acertadas = ["_"] * len(palavra)
    tentativas = 6  # Número máximo de erros permitidos
    letras_erradas = []

    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra:")

    while tentativas > 0 and "_" in letras_acertadas:
        print("Palavra:", " ".join(letras_acertadas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi tentada
        if letra in letras_acertadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Verifica se a letra está na palavra
        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_acertadas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra incorreta!")

    # Resultado do jogo
    if "_" not in letras_acertadas:
        print("Parabéns! Você acertou a palavra:", palavra)
    else:
        print("Você perdeu! A palavra era:", palavra)

# Executa o jogo
jogar()
