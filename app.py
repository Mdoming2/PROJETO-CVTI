import random, json

try: 
    with open("perguntas.json", encoding="UTF-8") as file:
        perguntas=json.load(file)
except:
    perguntas = ""

class ShowDoMilhao:
    global perguntas
    def __init__(self):
        self.questions = perguntas
        self.prize_levels = [1000, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 1000000]
        self.score = 0
        self.correct_answers = 0
        self.used_help = False
        self.used_questions = []  # Lista para controlar perguntas usadas

    def start_game(self):
        print("Bem-vindo ao Show do Milhão!")
        while self.correct_answers < 10:
            self.display_options()
            self.display_question()
            self.get_user_answer()
        print("Parabéns! Você ganhou 1 milhão de reais!")

    def display_options(self):
        if not self.used_help:
            print("(1) Pedir Ajuda")
        print("(2) Eliminar duas opções incorretas")
        print("(3) Trocar de pergunta")
        print("(4) Perguntar ao professor ou colega do curso")
        print()

    def display_question(self):
        # Seleciona uma pergunta que não tenha sido usada ainda
        while True:
            question_index = random.randint(0, len(self.questions) - 1)
            if question_index not in self.used_questions:
                self.current_question_index = question_index
                self.used_questions.append(question_index)
                break
        
        question = self.questions[self.current_question_index]
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
    
    def get_user_answer(self):
        while True:
            user_answer = input("Digite a letra correspondente à sua resposta: ").lower()
            if user_answer in ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4']:
                break
            else:
                print("Resposta inválida. Por favor, escolha uma das opções (a, b, c, d, e, 1, 2, 3 ou 4).")
        
        if user_answer == '1':
            if not self.used_help:
                self.get_help()
                self.used_help = True
            else:
                print("Você já usou a ajuda. Por favor, escolha uma das opções de resposta.")
        elif user_answer == '2':
            if not self.used_help:
                self.eliminate_options()
                self.used_help = True
            else:
                print("Você já usou a ajuda. Por favor, escolha uma das opções de resposta.")
        elif user_answer == '3':
            if not self.used_help:
                self.change_question()
                self.used_help = True
            else:
                print("Você já usou a ajuda. Por favor, escolha uma das opções de resposta.")
        elif user_answer == '4':
            if not self.used_help:
                self.ask_friend()
                self.used_help = True
            else:
                print("Você já usou a ajuda. Por favor, escolha uma das opções de resposta.")
        elif user_answer == self.questions[self.current_question_index]["answer"]:
            self.score += self.prize_levels[self.correct_answers]
            self.correct_answers += 1
            print("Resposta correta! Você ganhou R${}.".format(self.prize_levels[self.correct_answers - 1]))
            if self.correct_answers < 10:
                self.current_question_index = None  # Reseta para escolher uma nova pergunta
        else:
            print(f"Resposta incorreta! Infelizmente você perdeu o jogo. Sua pontuação final é: R${self.prize_levels[self.correct_answers]}")
            exit()

    def get_help(self):
        print("Você pediu ajuda.")
        correct_answer = self.questions[self.current_question_index]["answer"]
        options = random.sample(self.questions[self.current_question_index]["options"], 2)
        print("Estou em dúvida entre", correct_answer, "e", ', '.join(options))

    def eliminate_options(self):
        print("Você escolheu eliminar duas opções incorretas.")
        correct_answer = self.questions[self.current_question_index]["answer"]
        options = self.questions[self.current_question_index]["options"]
        incorrect_options = [opt for opt in options if not opt.startswith(correct_answer)]
        options_to_keep = random.sample(incorrect_options, 2)
        options_to_keep.append(correct_answer)
        options_to_keep.sort()
        for option in options:
            if option not in options_to_keep:
                print(f"Eliminando: {option}")

    def change_question(self):
        print("Você escolheu trocar de pergunta.")
        self.current_question_index = None  # Reseta para escolher uma nova pergunta

    def ask_friend(self):
        print("Você escolheu perguntar ao professor ou colega do curso.")
        correct_answer = self.questions[self.current_question_index]["answer"]
        while True:
            friend_answer = input("Digite a letra correspondente à resposta que você acha correta: ").lower()
            if friend_answer in ['a', 'b', 'c', 'd', 'e']:
                break
            else:
                print("Resposta inválida. Por favor, digite uma das opções (a, b, c, d ou e).")
        
        if friend_answer == correct_answer:
            print("Parabéns! Sua resposta está correta.")
        else:
            print(f"Resposta incorreta! Infelizmente você perdeu o jogo. Sua pontuação final é: R${self.prize_levels[self.correct_answers]}")
            exit()

if __name__ == "__main__":
    jogo = ShowDoMilhao()
    jogo.start_game()





