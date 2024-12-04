import random
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

# KV Language para o layout
KV = '''
ScreenManager:
    MenuScreen:
    GameScreen:

<MenuScreen>:
    name: "menu"
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text: "Bem-vindo ao Jogo de Forca"
            halign: "center"
            font_style: "H4"

        MDRaisedButton:
            text: "Iniciar Jogo"
            pos_hint: {"center_x": 0.5}
            on_release: app.start_game()

<GameScreen>:
    name: "game"
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            id: word_label
            text: app.displayed_word
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: letter_input
            hint_text: "Digite uma letra"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Tentar"
            pos_hint: {"center_x": 0.5}
            on_release: app.guess_letter(letter_input.text)

        MDLabel:
            id: attempts_label
            text: f"Tentativas restantes: {app.remaining_attempts}"
            halign: "center"
            theme_text_color: "Error"

        MDRaisedButton:
            text: "Voltar ao Menu"
            pos_hint: {"center_x": 0.5}
            on_release: app.go_to_menu()
'''

# Lógica do Jogo de Forca
class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class ForcaApp(MDApp):
    def build(self):
        self.word_list = ["PYTHON", "KIVY", "DESENVOLVEDOR", "SAULO", "PROGRAMACAO"]
        self.displayed_word = "_ " * len(self.word_list)  # Palavra mascarada
        self.remaining_attempts = 6  # Tentativas permitidas
        self.guessed_letters = []  # Letras já tentadas

        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name="menu"))
        self.sm.add_widget(GameScreen(name="game"))
        return Builder.load_string(KV)

    def start_game(self):
        # Reiniciar o estado do jogo
        self.word = random.choice(self.word_list).upper()
        self.displayed_word = "_ " * len(self.word)
        self.remaining_attempts = 6
        self.guessed_letters = []
        self.root.current = "game"
        self.update_game_screen()

    def guess_letter(self, letter):
        if not letter or len(letter) != 1 or not letter.isalpha():
            return  # Entrada inválida

        letter = letter.upper()
        if letter in self.guessed_letters:
            return  # Letra já tentada

        self.guessed_letters.append(letter)

        if letter in self.word:
            # Atualizar palavra mascarada
            self.displayed_word = " ".join(
                [char if char in self.guessed_letters else "_" for char in self.word]
            )
            if "_" not in self.displayed_word:
                self.end_game(won=True)
        else:
            # Diminuir tentativas
            self.remaining_attempts -= 1
            if self.remaining_attempts <= 0:
                self.end_game(won=False)

        self.update_game_screen()

    def update_game_screen(self):
        # Atualizar os elementos da tela do jogo
        game_screen = self.root.get_screen("game")
        game_screen.ids.word_label.text = self.displayed_word
        game_screen.ids.attempts_label.text = f"Tentativas restantes: {self.remaining_attempts}"

    def end_game(self, won):
        message = "Você venceu!" if won else f"Você perdeu! A palavra era {self.word}."
        game_screen = self.root.get_screen("game")
        game_screen.ids.word_label.text = message

    def go_to_menu(self):
        self.root.current = "menu"

# Rodar o aplicativo
if __name__ == "__main__":
    ForcaApp().run()
