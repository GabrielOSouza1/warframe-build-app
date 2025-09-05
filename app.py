from flask import Flask, render_template
import requests

# Criar uma instância do aplicativo Flask
app = Flask(__name__)

# URL base da API Warframe (atualizada)
BASE_URL = "https://api.warframestat.us/"

def obter_armas_e_companheiros(idioma='pt'):
   def obter_armas_e_companheiros(idioma='pt'):
    try:
        armas_response = requests.get(f"{BASE_URL}/Armas", params={'language': idioma})
        companheiros_response = requests.get(f"{BASE_URL}/Companheiros", params={'language': idioma})

        armas = armas_response.json()
        companheiros = companheiros_response.json()

        primarias = [arma for arma in armas if arma.get('category') == 'Primary']
        secundarias = [arma for arma in armas if arma.get('category') == 'Secondary']
        melees = [arma for arma in armas if arma.get('category') == 'Melee']

        return {
            'Primarias': primarias,
            'Secundarias': secundarias,
            'Melees': melees,
            'Companheiros': companheiros,
        }

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
    armas = obter_armas_e_companheiros()


    if obter_warframes and obter_armas_e_companheiros:
        return render_template(
            'builds.html',
            warframes= obter_warframes,
            primarias= obter_armas_e_companheiros['primarias'],
            secundarias= obter_armas_e_companheiros['secundarias'],
            melees= obter_armas_e_companheiros['melees'],
            companheiros= obter_armas_e_companheiros['companheiros']
        )
    else:
        return "Erro ao carregar dados da API."
    

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)