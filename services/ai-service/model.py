def predict_intent(text):

    text = text.lower()

    if "vpn" in text:
        return "network_issue"

    if "password" in text:
        return "password_reset"

    return "general_issue"