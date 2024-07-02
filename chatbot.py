from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from train_chatbot import training_data
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

chatbot_name = 'M1 Motors'

# Create a new chatbot instance
chatbot = ChatBot(
    chatbot_name,
    read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    database_uri='sqlite:///db.sqlite3'
)

# Define the training file
trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Function to display chatbot options
def bot_options():
    options = [
        '1 - Qual o telefone de contato?',
        '2 - Qual o e-mail de contato?',
        '3 - Como eu acesso a politica de privacidade da empresa?',
        '4 - Qual o endereço?',
        '5 - Quem é a M1 Motors?',
        '6 - Qual o site da empresa?',
    ]

    print('Escolha uma das opções a seguir:')

    for option in options:
        print(option)

    print('\n' + 'Ou digite sua própria pergunta (digite sair para encerrar ou 0 para voltar ao menu):')

    return ''

# Function to interact with bot
def chat_with_bot():
    print('Olá, tudo bem? Como posso te ajudar?' + '\n')

    while True:
        try:
            print(bot_options())

            while True:
                try: 
                    user_input = input(Fore.BLUE + 'Você: ' + Style.RESET_ALL)

                    if user_input.lower() == 'sair':
                        return
                    if user_input == '0':
                        break

                    bot_response = chatbot.get_response(user_input)

                    print(Fore.RED + chatbot_name + ':' + Style.RESET_ALL + f' {bot_response}')
                except (KeyboardInterrupt, EOFError, SystemExit):
                    return
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == '__main__':
    chat_with_bot()
