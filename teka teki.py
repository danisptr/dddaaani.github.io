class MiniGameLangInterpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('SHOW'):
                self.show(line[5:-1].strip('"'))
            elif line.startswith('INPUT'):
                prompt = line[6:-1].strip('"')
                self.input(prompt)
            elif line.startswith('IF'):
                condition = line.split('THEN')[0].strip()[3:]
                command = line.split('THEN')[1].strip()
                self.if_condition(condition, command)
            elif line.startswith('WHILE'):
                # For simplicity, while loops are not implemented in this example
                pass

    def show(self, message):
        print(message)

    def input(self, prompt):
        user_input = input(prompt + ' ')
        self.variables['last_input'] = user_input
        print(f"You entered: {user_input}")

    def if_condition(self, condition, command):
        # Simplified condition checking
        if condition == 'last_input == "dani"':
            if self.variables.get('last_input') == 'dani':
                self.execute(command)
        elif condition == 'last_input != "dani"':
            if self.variables.get('last_input') != 'dani':
                self.execute(command)

# Sample code for MiniGameLang
mini_game_code = """
SHOW "Selamat datang di kuis sederhana!"
INPUT "Apa nama Anda? "
SHOW "Halo, [nama]. Siap untuk pertanyaan pertama?"
SHOW "jengenku sopo?"
INPUT "Jawaban Anda: "
IF last_input == "dani" THEN SHOW "Benar! Selamat!"
IF last_input != "dani" THEN SHOW "Salah. Coba lagi lain kali!"
"""

interpreter = MiniGameLangInterpreter()
interpreter.execute(mini_game_code)
