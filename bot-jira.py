import requests
import json
from flask import Flask, request, Response

app = Flask(__name__)

# Configurações do Jira
JIRA_BASE_URL = "https://seu-jira.exemplo.com"
JIRA_USERNAME = "seu-usuario-jira"
JIRA_PASSWORD = "sua-senha-jira"

# Rota para receber mensagens do Microsoft Teams
@app.route("/bot", methods=["POST"])
def bot():
    data = request.get_json()

    # Verifica se a mensagem é uma atividade do tipo mensagem
    if data["type"] == "message":
        text = data["text"]
        if "criar tarefa:" in text.lower():
            task_name = text.lower().split("criar tarefa:")[1].strip()
            create_jira_task(task_name)

    return Response(status=200)

# Função para criar uma tarefa no Jira
def create_jira_task(task_name):
    url = f"{JIRA_BASE_URL}/rest/api/2/issue/"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "fields": {
            "project": {
                "key": "SEU_PROJETO_JIRA"
            },
            "summary": task_name,
            "issuetype": {
                "name": "Task"
            }
        }
    }

    response = requests.post(url, auth=(JIRA_USERNAME, JIRA_PASSWORD), headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print("Tarefa criada com sucesso no Jira!")
    else:
        print(f"Erro ao criar a tarefa no Jira. Status code: {response.status_code}")

if __name__ == "__main__":
    app.run(debug=True)
