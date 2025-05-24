

db.users.insertMany([
  {
    nombre: "Laura Martínez",
    empresa: "Tornillos S.A.",
    cargo: "Gerente de Compras",
    telefono: "3101234567",
    correo: "laura@tornillossa.com",
    contrasena: "clave123",
    verificacion: 1
  },
  {
    nombre: "Carlos Pérez",
    empresa: "Construmax",
    cargo: "Encargado de Inventario",
    telefono: "3127654321",
    correo: "carlos@construmax.com",
    contrasena: "seguro456",
    verificacion: 1
  }
]);


db.user_products.insertMany([
  {
    nombre_producto: "Taladro Inalámbrico",
    max_venta_diario: 10,
    min_venta_diario: 2,
    tiempo_provedor_despacho_dias: 3,
    inventario_total: 50,
    id_to_user: ObjectId("ID_DEL_USUARIO")
  },
  {
    nombre_producto: "Caja de Tornillos 100 unid",
    max_venta_diario: 20,
    min_venta_diario: 5,
    tiempo_provedor_despacho_dias: 2,
    inventario_total: 200,
    id_to_user: ObjectId("ID_DEL_USUARIO")
  }
]);
