// Crear un array con elementos duplicados
const arrayConDuplicados = [1, 2, 2, 3, 4, 4, 5];

// Eliminar elementos duplicados del array utilizando el método filter
const arraySinDuplicados = arrayConDuplicados.filter((valor, indice, array) => array.indexOf(valor) === indice);

// Imprimir el array sin duplicados
console.log("Array sin duplicados:", arraySinDuplicados);