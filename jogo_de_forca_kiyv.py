from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "computador", "unicep", "faculdade", "saulo"]

class ForcaApp(MDApp):
    def build(self):
        # Carrega o arquivo KV para a interface
        return Builder.load_file("forca.kv")
    
    def on_start(self):
        # Inicializa o jogo
        self.nova_palavra()

    def nova_palavra(self):
        # Seleciona uma nova palavra
        self.palavra = random.choice(palavras)
        self.letras_acertadas = ["_"] * len(self.palavra)
        self.tentativas = 6
        self.letras_erradas = []

        # Atualiza a interface
        self.root.ids.palavra_label.text = " ".join(self.letras_acertadas)
        self.root.ids.tentativas_label.text = f"Tentativas restantes: {self.tentativas}"
        self.root.ids.letras_erradas_label.text = "Letras erradas: "
    
    def verificar_letra(self, letra):
        letra = letra.lower()

        # Verifica se a letra já foi tentada
        if letra in self.letras_acertadas or letra in self.letras_erradas:
            self.root.ids.mensagem_label.text = "Você já tentou essa letra."
            return

        # Verifica se a letra está na palavra
        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.letras_acertadas[i] = letra
            self.root.ids.palavra_label.text = " ".join(self.letras_acertadas)
            self.root.ids.mensagem_label.text = "Boa! Você acertou uma letra."
        else:
            self.letras_erradas.append(letra)
            self.tentativas -= 1
            self.root.ids.letras_erradas_label.text = f"Letras erradas: {', '.join(self.letras_erradas)}"
            self.root.ids.tentativas_label.text = f"Tentativas restantes: {self.tentativas}"
            self.root.ids.mensagem_label.text = "Letra incorreta!"

        # Verifica se o jogo terminou
        if "_" not in self.letras_acertadas:
            self.root.ids.mensagem_label.text = "Parabéns! Você venceu!"
        elif self.tentativas == 0:
            self.root.ids.mensagem_label.text = f"Você perdeu! A palavra era: {self.palavra}"

# Executa o aplicativo
ForcaApp().run()
