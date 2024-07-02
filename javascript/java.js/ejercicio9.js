// Crear un array con objetos que tienen una propiedad en común
const objetos = [
    { nombre: 'Objeto1', color: 'rojo' },
    { nombre: 'Objeto2', color: 'azul' },
    { nombre: 'Objeto3', color: 'verde' },
    { nombre: 'Objeto4', color: 'rojo' },
    { nombre: 'Objeto5', color: 'azul' },
  ];
  
  // Agrupar los elementos del array por el valor de la propiedad común
  const grupos = objetos.reduce((acumulador, objeto) => {
    // Obtener el valor de la propiedad común
    const valorPropiedadComun = objeto.color; // Cambia "color" por la propiedad que quieras agrupar
  
    // Verificar si ya existe un grupo con ese valor de la propiedad común
    if (!acumulador[valorPropiedadComun]) {
      // Si no existe, crear un nuevo grupo con ese valor de la propiedad común
      acumulador[valorPropiedadComun] = [];
    }
  
    // Agregar el objeto al grupo correspondiente
    acumulador[valorPropiedadComun].push(objeto);
  
    // Devolver el acumulador actualizado
    return acumulador;
  }, {});
  
  // Imprimir los grupos
  console.log("Grupos de objetos por la propiedad común:");
  console.log(grupos);