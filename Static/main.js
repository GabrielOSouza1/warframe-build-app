// Obtém a referência para o campo de pesquisa do Warframe
const warframeSearch = document.getElementById('warframe-search');
const warframeSearchResults = document.getElementById('warframe-results');

const primarySearch = document.getElementById('primary-search');
const primarySearchResults = document.getElementById('primary-results')

const secondarySearch = document.getElementById('secondary-search');
const secondarySearchResults = document.getElementById('secondary-results');

const meleeSearch = document.getElementById('melee-search');
const meleeSearchResults = document.getElementById('melee-results');

const companionSearch = document.getElementById('companion-search');
const companionSearchResults = document.getElementById('companion-results');



// Adiciona um "ouvinte" para o evento de digitação
warframeSearch.addEventListener('keyup', (e) => {
    const termoDaPesquisa = e.target.value;
    // Chama a função para filtrar e exibir
    const resultados = filtraItens(termoDaPesquisa, warframesData);
    mostraResultados(resultados, warframeSearchResults);
});

// Adiciona o mesmo para os outros campos
primarySearch.addEventListener('keyup', (e) => {
    const termoDaPesquisa = e.target.value;
    const resultados = filtraItens(termoDaPesquisa, armasPrimariasData);
    mostraResultados(resultados, primarySearchResults);
});

secondarySearch.addEventListener('keyup', (e) => {
    const termoDaPesquisa = e.target.value;
    const resultados = filtraItens(termoDaPesquisa, armasSecundariasData);
    mostraResultados(resultados, secondarySearchResults);
});

meleeSearch.addEventListener('keyup', (e) => {
    const termoDaPesquisa = e.target.value;
    const resultados = filtraItens(termoDaPesquisa, armasMeleeData);
    mostraResultados(resultados, meleeSearchResults);
});

companionSearch.addEventListener('keyup', (e) => {
    const termoDaPesquisa = e.target.value;
    const resultados = filtraItens(termoDaPesquisa, companheirosData);
    mostraResultados(resultados, companionSearchResults);
});

// Função para filtrar a lista com base no termo de pesquisa
function filtraItens(termoDaPesquisa, listaCompleta) {
    if (!termoDaPesquisa) {
        return [];
    }
    return listaCompleta.filter(item => 
        item.name.toLowerCase().includes(termoDaPesquisa.toLowerCase())
    );
}

// Função para exibir os resultados no HTML
function mostraResultados(resultados, elementoHTML) {
    // Limpa os resultados anteriores
    elementoHTML.innerHTML = '';
    
    // Se a lista de resultados estiver vazia, não faz nada
    if (resultados.length === 0) {
        return;
    }

    // Cria os elementos <li> para cada resultado e os adiciona à lista <ul>
    resultados.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item.name;
        elementoHTML.appendChild(li);
    });
}
