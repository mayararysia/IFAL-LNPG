/*Lista de Notas de Alunos*/

let alunos = ["Queenie", "Hermione", "Harry", "Newt", "Porpentina", "Leta", "Albus"];

let notas = [2.0, 10.0, 9.0, 5.5, 6.0, 3.0, 2.0, 2.0];

let conjunto = [["Queenie", 2.0],["Hermione", 10.0],["Harry", 9.0],["Newt", 5.5],["Porpentina", 6.0], ["Leta", 3.0], ["Albus", 2.0]];

//Listas Puras
console.log('------- x -------------- x ---------------- x------\n');
console.log('Listas Puras: \n');
console.log("Alunos: "+alunos);
console.log("Notas: "+notas+"\n");
console.log("\tAluno, Nota: \n");
console.log(conjunto);
console.log('\n------- x -------------- x ---------------- x------\n');

const nomeAluno = elemento => elemento[0];
const notaAluno = elemento => elemento[1];
const alunoAprovado = elemento => elemento[1] > 6;
const alunoReprovado = elemento => elemento[1] <= 6;


let arrayAprovados = conjunto.filter(alunoAprovado);
let arrayReprovados = conjunto.filter(alunoReprovado);

console.log('APROVADOS: '+arrayAprovados.map(nomeAluno));
console.log('\nREPROVADOS: '+arrayReprovados.map(nomeAluno));


const soma = array => array.reduce((acumulador, valorAtual) => acumulador + valorAtual);
const mediaDoArray = array => soma(array) / array.length;
const mediaDasNotas = mediaDoArray(notas);
const mediaDasNotasAprovados = mediaDoArray(arrayAprovados.map(notaAluno));
const mediaDasNotasReprovados = mediaDoArray(arrayReprovados.map(notaAluno));
const maiorValor = array => array.reduce((acumulador, valorAtual) => Math.max(acumulador, valorAtual));
const menorValor = array => array.reduce((acumulador, valorAtual) => Math.min(acumulador, valorAtual));
const potenciaDois= base => Math.pow(base, 2);


console.log('\nMÉDIA GERAL: '+mediaDasNotas);
console.log('\nMÉDIA GERAL DOS APROVADOS: '+mediaDasNotasAprovados);
console.log('\nMÉDIA GERAL DOS REPROVADOS: '+mediaDasNotasReprovados);
console.log('\nMAIOR NOTA: '+ maiorValor(conjunto.map(notaAluno)));
console.log('\nMENOR NOTA: '+ menorValor(conjunto.map(notaAluno)));
console.log('\nNOTAS DUPLICADAS: \n' + notas.map(potenciaDois));

console.log('\n\n ------- x -------------- x ---------------- x------\n');
console.log('\n\nManipulando Entrada: \n');

let entrada = "2.0, 10.0, 9.0, 5.5, 6.0, 3.0, 2.0, 65.0";
let lista = entrada.split(" ").map(valor => parseInt(valor));
let hexa = lista.map(valor => '0x'+valor.toString(16));

console.log("Lista:", lista);
console.log("Hexa:", hexa);

entrada = [2.0 <= 6.0, 10.0 == null, '', 9.0>6.0, 5.5, 6.0, 3.0, 2.0, 2.0, null];
lista = entrada.filter(valor => !!valor);
console.log("\nentrada = [2.0 <= 6.0, 10.0 == null, '', 9.0>6.0, 5.5, 6.0, 3.0, 2.0, 2.0, null]\n")
console.log(lista);