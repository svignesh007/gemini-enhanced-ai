import random

def generate_response(user_input):
    # Simple response generation for demo purposes
    responses = [
        "That's interesting! Can you tell me more?",
        "I understand how you feel.",
        "Let's talk about something else.",
        "How does that make you feel?"
    ]
    return random.choice(responses)
