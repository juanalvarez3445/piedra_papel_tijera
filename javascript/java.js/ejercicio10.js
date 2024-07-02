// Crear un array con elementos de diferentes tipos
const miArray = ['a', 1, true, { nombre: 'Ejemplo' }];

// Convertir el array en un objeto utilizando reduce
const miObjeto = miArray.reduce((objeto, elemento, indice) => {
  // Utilizar el índice como clave para el objeto
  objeto['propiedad_' + indice] = elemento;
  return objeto;
}, {});

// Imprimir el objeto resultante
console.log("Objeto resultante:", miObjeto);