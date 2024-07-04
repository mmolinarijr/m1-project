from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from train_chatbot import training_data1, training_data2
import colorama
from colorama import Fore, Style
from flask import Flask, render_template, request, jsonify

colorama.init(autoreset=True)

# Create and define Flask routes
app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('chat.html', options=options)

@app.route('/ask', methods = ['POST'])
def ask():
    message = request.form['messageText']

    bot_response = chatbot.get_response(message)

    while True:
        try: 
            bot_response = chatbot.get_response(message)

            minimum_level_of_reliability = 0.4

            if float(bot_response.confidence) > minimum_level_of_reliability:
                bot_response = str(bot_response)
                return jsonify({'status':'OK','answer':bot_response})
            else:
                bot_response = 'Desculpe, não entendi. Tente novamente ou entre em contato conosco via WhatsApp (41) 9 92641020.'
                return jsonify({'status': 'OK', 'answer': bot_response})
        except IndexError:
            bot_response = 'Ocorreu um erro ao processar sua solicitação.'
            return jsonify({'status':'ERROR','answer':bot_response})

chatbot_name = 'M1 Motors'

# Create a new chatbot instance
chatbot = ChatBot(
    chatbot_name,
    read_only=True,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=['chatterbot.logic.BestMatch', 'chatterbot.logic.SpecificResponseAdapter'],
    database_uri='sqlite:///db.sqlite3'
)

# Define the training files
trainer = ListTrainer(chatbot)
trainer.train(training_data1)
trainer.train(training_data2)

# Define the initial options for user to choose from
options = [
    '1 - Qual o telefone de contato?',
    '2 - Qual o e-mail de contato?',
    '3 - Como eu acesso a politica de privacidade da empresa?',
    '4 - Qual o endereço?',
    '5 - Quem é a M1 Motors?',
    '6 - Qual o site da empresa?',
]

# Function to display chatbot options
def bot_options():
    print('Escolha uma das opções a seguir:\n')

    for option in options:
        print(option)

    print('\n' + 'Ou digite sua própria pergunta (a qualquer momento digite sair para encerrar ou 0 para voltar ao menu):')

    return ''

# Function to interact with bot via terminal
def chat_with_bot():
    print(f'Olá, tudo bem? Seja bem-vindo(a) a {chatbot_name}' + '\n')

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

                    minimum_level_of_reliability = 0.4

                    if float(bot_response.confidence) > minimum_level_of_reliability:
                        print(Fore.RED + chatbot_name + ':' + Style.RESET_ALL + f' {bot_response}')
                    else:
                        print(Fore.RED + chatbot_name + ':' + Style.RESET_ALL + ': Desculpa não entendi, tente novamente, ')
                        print(bot_options())
                except (KeyboardInterrupt, EOFError, SystemExit):
                    return
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Start the app either terminal or web
if __name__ == '__main__':
    chat_with_bot()
    app.run()
