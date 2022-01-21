from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text)

    if user_message in ("hello", "hi"):
        return "Hey, how are you doing?"
    if "time" in user_message:
        return str(datetime.now())
    
    return "I dont understand"
    