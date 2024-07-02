// Función para generar un array con números aleatorios
function generarArrayAleatorio(longitud) {
    const array = [];
    for (let i = 0; i < longitud; i++) {
      array.push(Math.floor(Math.random() * 100)); // Números aleatorios entre 0 y 99
    }
    return array;
  }
  
  // Función para imprimir un array
  function imprimirArray(nombre, array) {
    console.log(`${nombre}: [${array.join(', ')}]`);
  }
  
  // Crear un array con números aleatorios
  const miArray = generarArrayAleatorio(10);
  
  // Imprimir el array antes de ordenarlo
  imprimirArray('Array original', miArray);
  
  // Ordenar el array de forma ascendente
  miArray.sort((a, b) => a - b);
  imprimirArray('Array ascendente', miArray);
  
  // Ordenar el array de forma descendente
  miArray.sort((a, b) => b - a);
  imprimirArray('Array descendente', miArray);