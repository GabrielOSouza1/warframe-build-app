from flask import Flask, render_template
import requests

app = Flask(__name__)
BASE_URL = "https://api.warframestat.us"

def obter_armas_e_companheiros():
    try:
        armas = requests.get(f"{BASE_URL}/weapons").json()
        companheiros = requests.get(f"{BASE_URL}/companions").json()

        primarias = [a for a in armas if a.get('category') == 'Primary']
        secundarias = [a for a in armas if a.get('category') == 'Secondary']
        melees = [a for a in armas if a.get('category') == 'Melee']

        return {
            'primarias': primarias,
            'secundarias': secundarias,
            'melees': melees,
            'companheiros': companheiros
        }

    except Exception as e:
        print("Erro ao obter armas e companheiros:", e)
        return None

def obter_warframes():
    try:
        return requests.get(f"{BASE_URL}/warframes").json()
    except Exception as e:
        print("Erro ao obter warframes:", e)
        return None

@app.route('/builds')
def builds():
    warframes = obter_warframes()
    armas = obter_armas_e_companheiros()

    if warframes and armas:
        return render_template(
            'builds.html',
            warframes=warframes,
            primarias=armas['primarias'],
            secundarias=armas['secundarias'],
            melees=armas['melees'],
            companheiros=armas['companheiros']
        )
    else:
        return "Erro ao carregar dados da API."

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
