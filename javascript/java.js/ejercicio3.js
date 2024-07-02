// Crear un array con al menos 10 elementos de diferentes tipos
const miArray = [1, "dos", true, false, 5, "seis", 7, 8, "nueve", 10];

// Definir el elemento específico a buscar
const elementoABuscar = "seis";

// Usar indexOf para buscar el elemento
const indiceConIndexOf = miArray.indexOf(elementoABuscar);

if (indiceConIndexOf !== -1) {
  console.log(`Usando indexOf: El elemento '${elementoABuscar}' se encuentra en el índice ${indiceConIndexOf}.`);
} else {
  console.log(`Usando indexOf: El elemento '${elementoABuscar}' no se encuentra en el array.`);
}

// Usar findIndex para buscar el elemento
const indiceConFindIndex = miArray.findIndex(elemento => elemento === elementoABuscar);

if (indiceConFindIndex !== -1) {
  console.log(`Usando findIndex: El elemento '${elementoABuscar}' se encuentra en el índice ${indiceConFindIndex}.`);
} else {
  console.log(`Usando findIndex: El elemento '${elementoABuscar}' no se encuentra en el array.`);
}
