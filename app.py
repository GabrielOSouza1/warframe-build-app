from flask import Flask, render_template
import requests

# Criar uma instância do aplicativo Flask
app = Flask(__name__)

# URL base da API Warframe (atualizada)
BASE_URL = "https://api.warframestat.us/warframes"

def obter_armas(idioma='pt'):
    try:
        response = requests.get("https://api.warframestat.us/weapons", params={'language': idioma})
        response.raise_for_status()  # Lança um erro para status de resposta ruins (4xx ou 5xx)
        return response.json()  # Retorna os dados em formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados: {e}")
        return None


# Função para obter dados dos Warframes
def obter_warframes(idioma='pt'):
    try:
        response = requests.get(BASE_URL, params={'language': idioma})
        response.raise_for_status()  # Lança um erro para status de resposta ruins (4xx ou 5xx)
        return response.json()  # Retorna os dados em formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados: {e}")
        return None

# Definir a rota para a página inicial
@app.route('/')
def home():
     return render_template('index.html',)
    
# Definir a rota para a página de builds
@app.route('/builds')
def builds():
    warframes = obter_warframes()
    armas = obter_armas()


    if armas and warframes:
        return render_template('builds.html', armas=armas, warframes=warframes)
    else:
        return "Erro ao carregar dados da API."
    

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)