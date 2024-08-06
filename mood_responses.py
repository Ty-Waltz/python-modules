def mood_response(mood):
    mood = mood.lower()

    if mood in ["great", "good", "awesome"]:
        return "Glad to hear it!"
    elif mood in ["okay", "not bad"]:
        return "Well, I hope your day gets better!"
    elif mood in ["bad", "awful", "not good"]:
        return "I'm sorry to hear that. I hope you feel better soon!"
    else:
        return "I'm not sure how to respond to that mood. Could you tell me more?"

