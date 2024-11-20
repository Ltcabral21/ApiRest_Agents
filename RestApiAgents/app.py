import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os


# Configurações da API OpenAI e do Flask
load_dotenv()

# Recupera a chave da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


# Dicionário para armazenar agentes
agents = {}

# Função para criar um agente
def create_agent(name, personality):
    if name in agents:
        return {"error": "Agent with this name already exists."}, 400
    agents[name] = {
        "name": name,
        "personality": personality,
        "chat_history": []  # Armazena o histórico de conversas
    }
    return {"message": f"Agent '{name}' created successfully."}, 201

# Endpoint para criar um agente
@app.route('/agents', methods=['POST'])
def add_agent():
    data = request.json
    name = data.get('name')
    personality = data.get('personality', 'neutral')
    if not name:
        return {"error": "Agent name is required."}, 400
    return create_agent(name, personality)

# Endpoint para conversar com um agente
@app.route('/agents/<name>/chat', methods=['POST'])
def chat_with_agent(name):
    if name not in agents:
        return {"error": f"Agent '{name}' does not exist."}, 404

    agent = agents[name]
    user_message = request.json.get('message')
    if not user_message:
        return {"error": "Message is required."}, 400

    # Cria uma lista de mensagens com histórico
    messages = [{"role": "system", "content": f"You are a {agent['personality']} assistant."}]
    
    for entry in agent['chat_history']:
        messages.append({"role": entry['role'].lower(), "content": entry['message']})
    
    # Adiciona a nova mensagem do usuário
    messages.append({"role": "user", "content": user_message})

    try:
        # Chamada à API OpenAI com o modelo de chat
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Modelo de chat
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )
        
        assistant_reply = response['choices'][0]['message']['content'].strip()

        # Atualiza o histórico do agente
        agent['chat_history'].append({"role": "user", "message": user_message})
        agent['chat_history'].append({"role": "assistant", "message": assistant_reply})

        return {"reply": assistant_reply}, 200
    except Exception as e:
        return {"error": str(e)}, 500

# Endpoint para listar todos os agentes
@app.route('/agents', methods=['GET'])
def list_agents():
    return jsonify(list(agents.keys()))

# Endpoint para excluir um agente
@app.route('/agents/<name>', methods=['DELETE'])
def delete_agent(name):
    if name in agents:
        del agents[name]
        return {"message": f"Agent '{name}' deleted successfully."}, 200
    return {"error": f"Agent '{name}' does not exist."}, 404

# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
