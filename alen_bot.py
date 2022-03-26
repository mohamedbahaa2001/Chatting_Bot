from gtts import gTTS #Import Google Text to Speech
from IPython.display import Audio #Import Audio method from IPython's Display Class
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def say(text):
  tts = gTTS(str(text)) #Provide the string to convert to speech
  tts.save('1.wav') #save the string converted to speech as a .wav file
  sound_file = '1.wav'
  Audio(sound_file, autoplay=True) 
  return Audio(sound_file,autoplay=True)



chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")


while(True):
  request = input('You: ')
  response = chatbot.get_response(request)
  print('Alen: ', response)