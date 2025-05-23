// 1. Crear colecciones y datos iniciales para ferretería

// === Categorías ===
db.createCollection("categorias");

const catHerramientas = db.categorias.insertOne({ nombre_categoria: "Herramientas" }).insertedId;
const catConstruccion = db.categorias.insertOne({ nombre_categoria: "Construcción" }).insertedId;
const catElectricidad = db.categorias.insertOne({ nombre_categoria: "Electricidad" }).insertedId;

// === Tipos de Clientes ===
db.createCollection("tipos_clientes");

const tipoMinorista = db.tipos_clientes.insertOne({ descripcion: "Cliente minorista" }).insertedId;
const tipoMayorista = db.tipos_clientes.insertOne({ descripcion: "Cliente mayorista" }).insertedId;
const tipoEmpresa = db.tipos_clientes.insertOne({ descripcion: "Empresa" }).insertedId;

// === Estados de Facturas ===
db.createCollection("estados_facturas");

const estadoPendiente = db.estados_facturas.insertOne({ descripcion: "Pendiente" }).insertedId;
const estadoPagada = db.estados_facturas.insertOne({ descripcion: "Pagada" }).insertedId;
const estadoCancelada = db.estados_facturas.insertOne({ descripcion: "Cancelada" }).insertedId;

// === Productos ===
db.createCollection("productos");

const prodMartillo = db.productos.insertOne({
  nombre: "Martillo",
  descripcion: "Martillo de acero con mango de goma",
  stock: 30,
  precio: 24000,
  id_categoria: catHerramientas
}).insertedId;

const prodCemento = db.productos.insertOne({
  nombre: "Cemento Gris 50kg",
  descripcion: "Bolsa de cemento",
  stock: 100,
  precio: 28000,
  id_categoria: catConstruccion
}).insertedId;

// === Clientes ===
db.createCollection("clientes");

const clienteCarlos = db.clientes.insertOne({
  nombre_completo: "Carlos Ramírez",
  telefono: "3110000000",
  email: "carlos@correo.com",
  direccion: "Calle 123 #45-67",
  documento: "123456789",
  tipo_cliente_id: tipoMinorista
}).insertedId;

// === Facturas ===
db.createCollection("facturas");

const factura1 = db.facturas.insertOne({
  id_cliente: clienteCarlos,
  fecha_factura: new Date("2025-05-23"),
  metodo_pago: "Efectivo",
  id_estado: estadoPendiente,
  total_facturas: 48000
}).insertedId;

// === Detalles de Factura ===
db.createCollection("detalles_factura");

db.detalles_factura.insertMany([
  {
    id_factura: factura1,
    id_producto: prodMartillo,
    cantidad: 2,
    precio_unitario: 24000
  }
]);
