import unittest
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class TestCompanyBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize chatbot for testing
        cls.chatbot = ChatBot(
            'TestCompanyBot',                  
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///test_db.sqlite3'
        )

        # Train the chatbot
        training_data = [
            'Qual o telefone de contato?',
            'O telefone de contato é (41) 3014-9646 e WhatsApp é (41) 9 9264-1020',
            'Qual o e-mail de contato?',
            'O e-mail de contato é contato@m1motorscwb.com.br',
            'Como eu acesso a politica de privacidade da empresa?',
            'Acesse através deste link: https://m1motors.com.br/politica-de-privacidade',
            'Qual o endereço?',
            'O endereço de todas as lojas está disponível neste link: https://m1motors.com.br/localizacao',
            'Quem é a M1 Motors?',
            'Fundada em 2020 por um visionário com ampla experiência no mercado automotivo, a M1 Motors é uma empresa do ramo automotivo que se destaca pela inovação. Sua localização estratégica em Shopping Centers proporciona aos clientes maior conforto e segurança durante todo o processo de compra e venda de veículos.',
            'Qual o site da empresa?',
            'Nosso site é: https://m1motors.com.br/'
        ]
        trainer = ListTrainer(cls.chatbot)
        trainer.train(training_data)

    # Execute tests
    def test_chatbot_phone_number(self):
        response = self.chatbot.get_response('Qual o telefone de contato?')
        self.assertIn('O telefone de contato é (41) 3014-9646 e WhatsApp é (41) 9 9264-1020', response.text)

    def test_chatbot_email(self):
        response = self.chatbot.get_response('Qual o e-mail de contato?')
        self.assertIn('O e-mail de contato é contato@m1motorscwb.com.br', response.text)

    def test_chatbot_privacy_policy(self):
        response = self.chatbot.get_response('Como eu acesso a politica de privacidade da empresa?')
        self.assertIn('Acesse através deste link: https://m1motors.com.br/politica-de-privacidade', response.text)

    def test_chatbot_address(self):
        response = self.chatbot.get_response('Qual o endereço?')
        self.assertIn('O endereço de todas as lojas está disponível neste link: https://m1motors.com.br/localizacao', response.text)

    def test_chatbot_who_is(self):
        response = self.chatbot.get_response('Quem é a M1 Motors?')
        self.assertIn('Fundada em 2020 por um visionário com ampla experiência no mercado automotivo, a M1 Motors é uma empresa do ramo automotivo que se destaca pela inovação. Sua localização estratégica em Shopping Centers proporciona aos clientes maior conforto e segurança durante todo o processo de compra e venda de veículos.', response.text)

    def test_chatbot_company_website(self):
        response = self.chatbot.get_response('Qual o site da empresa?')
        self.assertIn('Nosso site é: https://m1motors.com.br/', response.text)

if __name__ == '__main__':
    unittest.main()
