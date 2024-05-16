import openai
from django.conf import settings
from django.http import JsonResponse
from .models import Message
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from django.http import HttpResponse


bot = ChatBot('chatbot', read_only=False,
                logic_adapters=[
                    {

                        'import_path':'chatterbot.logic.BestMatch',
                        #'default_response':'Sorry, I dont understand what do you means',
                        #'maximun_similarty_threshold':0.90,

                    }])

List_to_train = [
    
    "hi?",
    "hi, there",
    "What's your name?",
    "I'm just a chatbot",
    "What is your Favorit Team?",
    "Taraji",
    "what's your fav sport?",
    "swimming",
    "Do you have kids?",
    "No",
    "What's your fav food?",
    "Pizza",

]

chatterbostCorpusTrainer = ChatterBotCorpusTrainer(bot)

#list_trainer = ListTrainer(bot)
#list_trainer.train(List_to_train)
chatterbostCorpusTrainer.train('chatterbot.corpus.english')

def chat_view(request):
    return render(request, 'chatbot/chat.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)