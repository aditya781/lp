#Name    : Aditya Sonawane
#Roll No.: 31101
#ProbStat: Create a rule based chatbot in python.

#movie ticket booking system
import random
import simple_chalk

#storing chatbot responses
name = "Bot Number 500" 
monsoon = "rainy" 
mood = "Smiley"
resp = { 
    "I want to book a movie ticket?": [
               "which movie do you want watch?"
       ] ,
    "Can you give list of today's streaming movies?":[
            "Spiderman, Batman and Uncharted these are the 3 movies that are going to stream today."
    ],
    "timing?":[
            "-----------Timings----------\n          Spiderman : 7:00, 8:00, 12:00, 15:00\n          Batman    : 18.00, 20:00\n          Uncharted : 6.00, 11:15, 14:30"
    ],
    "book spiderman movie.":[
            "completed payment. Movie has been booked!!"
    ],
    "cancel movie. ticket": [
            "Your ticket has been cancelled"
    ],
    "what's your name?": [ 
            "They call me {0}".format(name), 
            "I usually go by {0}".format(name), 
            "My name is the {0}".format(name) ],
    "what's today's weather?": [ 
            "The weather is {0}".format(monsoon), 
            "It's {0} today".format(monsoon)], 
    "how are you?": [ 
            "I am feeling {0}".format(mood), 
            "{0}! How about you?".format(mood), 
            "I am {0}! How about yourself?".format(mood) ],
    "": [ 
            "How can I help you?",
            "Hey! Are you there?", 
            "What do you mean by these?", ],
    "default": [
            "This is a default message"]
}

#user response function
def res(message):
  if message in resp: 
          bot286_message = random.choice(resp[message])
  else: 
          bot286_message = random.choice(resp["default"])
  return bot286_message

#chaking for keyword in string for better performance
def real(xtext): 
  if "name" in xtext: 
        ytext = "what's your name?"
  elif "weather" in xtext: 
          ytext = "what's today's weather?"
  elif "how are" in xtext: 
          ytext = "how are you?"
 
  elif "book" in xtext and "want" in xtext:
          ytext = "I want to book a movie ticket?"
  elif "streaming" in xtext or "stream" in xtext:
          ytext = "Can you give list of today's streaming movies?"
  elif "timing" in xtext:
          ytext = "timing?"
  elif "movie" in xtext and "book" in xtext:
          ytext = "book spiderman movie."
  elif "ticket" in xtext and "cancel" in xtext:
          ytext = "cancel movie. ticket"
  else: 
          ytext = ""
  return ytext

def send_message(message): 
  response = res(message) 
  print(simple_chalk.blue.bold("chatbot : " + str(response)))
  print()

print("chatbot : Hi there, how can i help you?")
while 1: 
  my_input = input("user    : ") 
  my_input = my_input.lower() 
  related_text = real(my_input) 
  if my_input == "exit" or my_input == "stop": 
    print(simple_chalk.green.bold("chatbot : Bye, Hope you like the support!!\n\n"))
    break
  send_message(related_text)

