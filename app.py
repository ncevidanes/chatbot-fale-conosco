from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
from flask_cors import CORS # Adicione esta linha

app = Flask(__name__)
CORS(app)  # Adicione esta linha


app = Flask(__name__)

# Definindo os pares de perguntas e respostas para o chatbot
pairs = [
    [r"oi",["Olá!", "Oi! Como posso te ajudar?", "Olá, tudo certo!"]],
    [
        r"quais os seus horários de atendimento?",
        ["Nosso horário de atendimento é de segunda a sexta, das 9h às 18h."]
    ],
    [
        r"como faço para rastrear meu pedido?",
        ["Para rastrear seu pedido, por favor, informe o número de rastreamento que enviamos para o seu e-mail."]
    ],
    [
        r"obrigado|muito obrigado",
        ["De nada! Estou aqui para ajudar.", "Fico feliz em poder ajudar!"]
    ],
    [
        r"tchau|até logo",
        ["Até logo! Tenha um ótimo dia.", "Tchau! Volte sempre."]
    ],
]

# Inicializando o chatbot
chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    # Renderiza a página HTML principal
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Recebe a mensagem do usuário via requisição POST
    user_message = request.json.get("message")
    
    # Obtém a resposta do chatbot
    response = chatbot.respond(user_message)
    
    # Se o chatbot não tiver uma resposta, fornece uma resposta padrão
    if not response:
        response = "Desculpe, não entendi sua pergunta. Por favor, tente novamente."
    
    # Retorna a resposta em formato JSON
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

# O PythonAnywhere não usa a função app.run() diretamente.
# A lógica de como a aplicação roda será configurada no painel do PythonAnywhere.
