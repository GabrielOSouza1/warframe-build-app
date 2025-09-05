// Obtém a referência para o campo de pesquisa do Warframe
const warframeSearch = document.getElementById('warframe-search');
const primarySearch = document.getElementById('primary-search');
const secondarySearch = document.getElementById('secondary-search');
const meleeSearch = document.getElementById('melee-search');
const companionSearch = document.getElementById('companion-search');




// Adiciona um "ouvinte" para o evento de digitação
warframeSearch.addEventListener('keyup', (e) => {
    // A cada tecla digitada, este código é executado
    const termoDaPesquisa = e.target.value;
    console.log(termoDaPesquisa);
});

primary-search.addEventListener('keyup', (e) => {
    // A cada tecla digitada, este código é executado
    const termoDaPesquisa = e.target.value;
    console.log(termoDaPesquisa);
});

secondary-search.addEventListener('keyup', (e) => {
    // A cada tecla digitada, este código é executado
    const termoDaPesquisa = e.target.value;
    console.log(termoDaPesquisa);
});

meleeSearch.addEventListener('keyup', (e) => {
    // A cada tecla digitada, este código é executado
    const termoDaPesquisa = e.target.value;
    console.log(termoDaPesquisa);
});     

companionSearch.addEventListener('keyup', (e) => {
    // A cada tecla digitada, este código é executado
    const termoDaPesquisa = e.target.value;
    console.log(termoDaPesquisa);
});
