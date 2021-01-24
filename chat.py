import random

affirmitive = ['Indeed.', 'Wonderful.', 'What would you like to talk about?', 'Excellent.', 'Is that a good thing?', 'Awesome!', "That's very nice.", 'All right!', 'Cool, tell me more.']

question = ['Why?','How do you feel?', 'Take a deep breath. It will all be okay.', 'Are you satisfied?', 'Are you living your best life?', 'Do you have aspirations?', 'Are you having fun?', 'What are you grateful for?', 'Who are you grateful for?', 'Do you feel focused today?', 'Are you feeling confident today?', 'Are you feeling energized?', 'Tell me about yourself.', "Let's talk. You can start.", 'Why is that?', 'How come?', 'Do you know why?', "Let's talk about you.", 'I would like to hear some more about you.', 'Tell me more.', "Oh, that's interesting.", 'Is that so?', 'I see.', 'Who is?', 'Do you need advice?', 'Do you need help?', 'How can I help you?', 'What do you need?', 'Can I help you with something?', "What's on your mind?", 'How are you feeling today?', 'Do you feel loved today?', 'What is your highlight of the day?']

insights = ["Walk as if you are kissing the Earth with your feet", "No one saves us but ourselves. No one can and no one may. We ourselves must walk the path.", "Man suffers only because he takes seriously what the gods made for fun.", "You only lose what you cling to.", "Teach this triple truth to all: A generous heart, kind speech, and a life of service and compassion are the things which renew humanity.", "Avoid evil deeds as a man who loves life avoids poison.", "What you think, you become. What you feel, you attract. What you imagine, you create.", 'Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.', 'Three things cannot be long hidden: the sun, the moon, and the truth.', 'Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared.', 'You can search throughout the entire universe for someone who is more deserving of your love and affection than you are yourself, and that person is not to be found anywhere. You yourself, as much as anybody in the entire universe deserve your love and affection.', 'Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship.', 'Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned.', 'To keep the body in good health is a duty... otherwise we shall not be able to keep our mind strong and clear.']

bot = ['Yes.', 'No.']

message = input('You: ')

def getReply(message):
  if 'hello' in message:
    reply = "Hi there! I'm WiseBot. It's a pleasure to speak with you today."
    print('WiseBot: ' + reply)
  elif 'Hello' in message:
    reply = "Hi there! I'm WiseBot. It's a pleasure to speak with you today."
    print('WiseBot: ' + reply)
  elif 'hi' in message:
    reply = "Hi there! I'm WiseBot. It's a pleasure to speak with you today."
    print('WiseBot: ' + reply)
  elif 'Hi' in message:
    reply = "Hi there! I'm WiseBot. It's a pleasure to speak with you today."
    print('WiseBot: ' + reply)
  elif 'hey' in message: 
    reply = "Hi there! I'm WiseBot. It's a pleasure to speak with you today."
    print('WiseBot: ' + reply)
  elif 'Hey' in message:
    reply = "Hi there! I'm WiseBot. It's a pleasure to speak with you today."
    print('WiseBot: ' + reply)
  elif 'Good' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'good' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'Great' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'great' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'Okay' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'okay' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'Fine' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'fine' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'Ok' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'ok' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'what' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'who' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'where' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'why' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'how' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'when' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'can' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'tell' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'should' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'could' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'would' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'cool' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'nice' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'sweet' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'lol' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'ugh' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'life' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'Life' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'Feelings' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'feelings' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'My' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'my' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'nothing' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'Nothing' in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif 'Help' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'help' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'no' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'No' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'yes' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'Yes' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'Thanks' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'thanks' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'Thank you' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'thank you' in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif "I don't know" in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif "i don't know" in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif 'I' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif 'i' in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "Will" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "will" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "cat" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "dog" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "job" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "work" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "coworker" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "world" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "politics" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "religion" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "advice" in message: 
    reply = random.choice(insights)
    print('WiseBot: ' + reply)
  elif "food" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "money" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "Me" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "I'm" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "im" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "me" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "You" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "you" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "Us" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "us" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "We" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "we" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "You" in message: 
    reply = random.choice(bot)
    print('WiseBot: ' + reply)
  elif "you" in message: 
    reply = random.choice(bot)
    print('WiseBot: ' + reply)
  elif "hungry" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "sad" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "bad" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "happy" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "upset" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "excited" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "confused" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "anxious" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "content" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "wonderful" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "Tired" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "tired" in message: 
    reply = random.choice(affirmitive)
    print('WiseBot: ' + reply)
  elif "are" in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif "but" in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif "quote" in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  elif "story" in message: 
    reply = random.choice(question)
    print('WiseBot: ' + reply)
  else: 
    print("WiseBot: Huh? Sorry. I'm not sure I understand.")

while ('bye' not in message):
  message = input('You: ')
  getReply(message)