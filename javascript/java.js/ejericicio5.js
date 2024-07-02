// Crear un array con nombres de personas
const nombres = ["Juan", "María", "Carlos", "Ana", "Pedro"];

// Crear un array con las edades correspondientes
const edades = [25, 17, 35, 19, 22];

// Combinar los arrays de nombres y edades en un array de objetos
const personas = nombres.map((nombre, index) => ({ nombre, edad: edades[index] }));

// Filtrar el array de personas para obtener solo las mayores de edad
const personasMayores = personas.filter(persona => persona.edad >= 18);

// Imprimir los nombres de las personas mayores de edad
console.log("Nombres de personas mayores de edad:");
personasMayores.forEach(persona => console.log(persona.nombre));

// Usar un bucle para recorrer el array filtrado y mostrar un mensaje para cada persona
console.log("\nMensajes para cada persona mayor de edad:");
personasMayores.forEach(persona => {
  console.log(`${persona.nombre} es mayor de edad.`);
});