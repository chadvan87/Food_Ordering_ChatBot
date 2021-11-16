from django.shortcuts import render
from django.http import HttpResponse, response

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create your views here.
# Create a new instance of a ChatBot
bot = ChatBot(
    'Food Bot',
    # provide an interface that allows ChatterBot to connect to different storage
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry I dont understand!',  # default answer
            'maximum_similarity_threshold': 0.95
        }
    ]
)


response = [
    # odd numbers are user messages or questions, even numbers are bot answers
    "Hello",  # 1
    "Hi there!",  # 2
    "How are you doing?",  # 3
    "I'm doing great.",  # 4
    "That is good to hear",  # 5
    "Thank you.",
    "You're welcome.",
    "Yes",
    "Thank you for order😍.Please wait 20 minutes",
    "yes",
    "Thank you for order😍.Please wait 20 minutes",
    "No",
    "Oh😭!You can try to order something else.",
    "Nasi lemak",
    "It's 2 ringgit.Do you want buy it?",
    "Nasi goreng kampung",
    "It's be 6 ringgit.Do you want buy it?",
    "Nasi goreng tomyam",
    "It's be 6.5 ringgit.Do you want buy it?",
    "Nasi goreng ikan masin",
    "It's be 6.5 ringgit.Do you want buy it?",
    "Nasi goreng paprik",
    "It's 7 ringgit.Do you want buy it?",
    "Nasi goreng USA",
    "It's 7 ringgit.Do you want buy it?",
    "Nasi goreng pattaya",
    "It's be 7 ringgit.Do you want buy it?",
    "Nasi goreng biasa",
    "It's be 5 ringgit.Do you want buy it?",
    "Ikan goreng",
    "It's 3.5 ringgit.Do you want buy it?",
    "Ayam goreng",
    "It's 3 ringgit.Do you want buy it?",
    "Satay",
    "It's 1.2 ringgit.Do you want buy it?",
    "Kuih talam",
    "It's 0.7 ringgit.Can you come and take it?",
    "Kuih koci",
    "It's 0.4 ringgit.Can you come and take it?",
    "Roti canai",
    "It's 1.2 ringgit.Can you come and take it?",
    "Roti telur",
    "It's 2.3 ringgit.Can you come and take it?",
    "Roti cheese",
    "It's 2.5 ringgit.Can you come and take it?",
    "Roti boom",
    "It's 2.2 ringgit.Can you come and take it?",
    "Roti planta",
    "It's 2.2 ringgit.Can you come and take it?",
    "Roti susu",
    "It's 2.2 ringgit.Can you come and take it?",
    "Roti tisu",
    "It's 3.2 ringgit.Can you come and take it?",
    "Tosai",
    "It's 1.2 ringgit.Can you come and take it?",
    "Mee goreng",
    "It's 5 ringgit.Do you want buy it?",
    "Maggi goreng",
    "It's 5 ringgit.Do you want buy it?",
    "Maggi soup",
    "It's 5 ringgit.Do you want buy it?",
    "Teh tarik ais",
    "It's 2.2 ringgit.Can you come and take it?",
    "The tarik panas",
    "It's 1.8 ringgit.Can you come and take it?",
    "Milo ais",
    "It's 2.5 ringgit.Can you come and take it?",
    "Milo panas",
    "It's 2.2 ringgit.Can you come and take it?",
    "Cincau",
    "It's 2.5 ringgit.Can you come and take it?",
    "Limau ais",
    "It's 1.8 ringgit.Can you come and take it?",
    "Limau panas",
    "It's 1.5 ringgit.Can you come and take it?",
    "Teh tarik ais",
    "It's 2.2 ringgit.Can you come and take it?",
    "Bandung ais",
    "It's 2 ringgit.Can you come and take it?",
    "Apple Juice",
    "It's 5 ringgit.Can you come and take it?",
    "Orange juice",
    "It's 5 ringgit.Can you come and take it?",
    "Watermelon juice",
    "It's 5 ringgit.Can you come and take it?",
    "Pineapple juice",
    "It's 5 ringgit.Can you come and take it?",
    "Carrot juice",
    "It's 5 ringgit.Can you come and take it?",
    "Espresso",
    "It's 6 ringgit.Do you want buy it?",
    "Hot Americano",
    "It's 7 ringgit.Do you want buy it?",
    "Iced Americano",
    "It's 8 ringgit.Do you want buy it?",
    "Hot Latte",
    "It's 9 ringgit.Do you want buy it?",
    "Iced Latte",
    "It's 10 ringgit.Do you want buy it?",
    "Hot Cappuccino",
    "It's 9 ringgit.Do you want buy it?",
    "Ice Cappuccino",
    "It's 10 ringgit.Do you want buy it?",
    "Hot Mocha",
    "It's 9 ringgit.Do you want buy it?",
    "Iced Mocha",
    "It's 10 ringgit.Do you want buy it?",
    "Tteok",
    "It's 2 ringgit.Do you want buy it?",
    "Kimchi",
    "It's 4 ringgit.Do you want buy it?",
    "Gimbap",
    "It's 4.5 ringgit.Do you want buy it?",
    "Tteokbokki",
    "It's 5 ringgit.Do you want buy it?",
    "Hobakjuk",
    "It's 6 ringgit.Do you want buy it?",
    "Ramyun",
    "It's 6.5 ringgit.Do you want buy it?",
    "Kimchi Fried Rice",
    "It's 7 ringgit.Do you want buy it?",
    "Bulgogi",
    "It's 7 ringgit.Do you want buy it?",
    "Jjajangmyeon",
    "It's 7 ringgit.Do you want buy it?",
    "Kongguksu",
    "It's 7.5 ringgit.Do you want buy it?",
    "Japchae",
    "It's 8 ringgit.Do you want buy it?",
    "Bulgogi with rice",
    "It's 8 ringgit.Do you want buy it?",
    "Naengmyeon",
    "It's 8.5 ringgit.Do you want buy it?",
    "Bibimbap",
    "It's 9 ringgit.Do you want buy it?",
    "Sundubu Jjigae",
    "It's 10 ringgit.Do you want buy it?",
    "Miso Soup",
    "It's 1.5 ringgit.Do you want buy it?",
    "Chawanmushi",
    "It's 1.5 ringgit.Do you want buy it?",
    "Gyoza",
    "It's 5 ringgit.Do you want buy it?",
    "Tempura",
    "It's 5 ringgit.Do you want buy it?",
    "Tamagoyaki (Egg Roll)",
    "It's 1.5 ringgit.Do you want buy it?",
    "Teriyaki Chicken Bento",
    "It's 8 ringgit.Do you want buy it?",
    "Teriyaki Vegetable Bento",
    "It's 6.5 ringgit.Do you want buy it?",
    "Seafood Bento",
    "It's 9 ringgit.Do you want buy it?",
    "Chicken Katsu Don",
    "It's 8 ringgit.Do you want buy it?",
    "Tempura Soba",
    "It's 7 ringgit.Do you want buy it?",
    "Chicken Yaki Soba",
    "It's 7 ringgit.Do you want buy it?",
    "Zaru Soba",
    "It's 6 ringgit.Do you want buy it?",
    "Zaru Soba + Tempura",
    "It's 7 ringgit.Do you want buy it?",
    "Tempura Udon",
    "It's 7 ringgit.Do you want buy it?",
    "Chicken Yaki Udon",
    "It's 7 ringgit.Do you want buy it?",
    "Vegetable Yaki Udon",
    "It's 6 ringgit.Do you want buy it?",
    "Zaru Udon",
    "It's 6 ringgit.Do you want buy it?",
    "Zaru Udon + Tempura",
    "It's 7 ringgit.Do you want buy it?",
    "Chicken Teriyaki Lunch Set (Miso Soup)",
    "It's 10 ringgit.Do you want buy it?",
    "Tempura Lunch Set (Miso Soup)",
    "It's 9 ringgit.Do you want buy it?",
    "Vegetarian Dinner Set (Chawanmushi)",
    "It's 8 ringgit.Do you want buy it?",
]
trainer = ListTrainer(bot)
trainer.train(response)


def index(request):
    return render(request, 'bot/index.html')  # call HTML file


def specific(request):
    number = 5
    return HttpResponse(number)


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatbot_response = bot.get_response(userMessage)
    return HttpResponse(chatbot_response)