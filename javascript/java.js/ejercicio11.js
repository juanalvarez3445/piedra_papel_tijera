// Definir un array vacío para almacenar los productos
let inventario = [];

// Función para agregar un nuevo producto al inventario
function agregarProducto(nombre, descripcion, precio, cantidad, categoria) {
  inventario.push({
    nombre: nombre,
    descripcion: descripcion,
    precio: precio,
    cantidad: cantidad,
    categoria: categoria
  });
  console.log("Producto agregado exitosamente.");
}

// Función para listar todos los productos
function listarProductos() {
  console.log("Lista de productos:");
  inventario.forEach(producto => {
    console.log("Nombre:", producto.nombre);
    console.log("Descripción:", producto.descripcion);
    console.log("Precio:", producto.precio);
    console.log("Cantidad en stock:", producto.cantidad);
    console.log("Categoría:", producto.categoria);
    console.log("--------------------");
  });
}

// Función para buscar un producto por nombre
function buscarProductoPorNombre(nombre) {
  const productoEncontrado = inventario.find(producto => producto.nombre === nombre);
  if (productoEncontrado) {
    console.log("Producto encontrado:");
    console.log("Nombre:", productoEncontrado.nombre);
    console.log("Descripción:", productoEncontrado.descripcion);
    console.log("Precio:", productoEncontrado.precio);
    console.log("Cantidad en stock:", productoEncontrado.cantidad);
    console.log("Categoría:", productoEncontrado.categoria);
  } else {
    console.log("No se encontró ningún producto con ese nombre.");
  }
}

// Función para eliminar un producto por nombre
function eliminarProducto(nombre) {
  inventario = inventario.filter(producto => producto.nombre !== nombre);
  console.log("Producto eliminado exitosamente.");
}

// Función para actualizar la cantidad en stock de un producto por nombre
function actualizarStock(nombre, nuevaCantidad) {
  const producto = inventario.find(producto => producto.nombre === nombre);
  if (producto) {
    producto.cantidad = nuevaCantidad;
    console.log("Cantidad en stock actualizada exitosamente.");
  } else {
    console.log("No se encontró ningún producto con ese nombre.");
  }
}

// Ejemplos de uso:
agregarProducto("Camiseta", "Camiseta de algodón", 20, 50, "Ropa");
agregarProducto("Zapatillas", "Zapatillas deportivas", 50, 30, "Calzado");
listarProductos();
buscarProductoPorNombre("Camiseta");
eliminarProducto("Zapatillas");
actualizarStock("Camiseta", 40);
listarProductos();