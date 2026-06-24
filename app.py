from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")

# Chatbot Logic
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello"]:
        return "Hello! How can I help you?"
    elif user_input == "how are you":
        return "I am fine. Thank you!"
    elif user_input == "what is your name":
        return "I am a Rule-Based AI Chatbot."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Chat Route
@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form.get("msg", "")
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)
