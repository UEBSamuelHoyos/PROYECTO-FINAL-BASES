from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

# Configura la URI correcta de MongoDB Atlas
app.config["MONGO_URI"] = "mongodb+srv://Hoyos:7712@ferreterialogs.i9tps73.mongodb.net/ferreteria?retryWrites=true&w=majority&appName=FerreteriaLogs"

mongo = PyMongo(app)
CORS(app)  # Permite llamadas desde frontend en otro origen

def fix_id(document):
    document['_id'] = str(document['_id'])
    return document

# --- CRUD Categorias ---
@app.route('/api/categorias', methods=['GET'])
def get_categorias():
    categorias = list(mongo.db.categorias.find())
    categorias = [fix_id(c) for c in categorias]
    return jsonify(categorias)

@app.route('/api/categorias', methods=['POST'])
def create_categoria():
    data = request.get_json()
    nuevo = {'nombre_categoria': data['nombre_categoria']}
    result = mongo.db.categorias.insert_one(nuevo)
    return jsonify({'message': 'Categoría creada', 'id': str(result.inserted_id)}), 201

@app.route('/api/categorias/<id>', methods=['PUT'])
def update_categoria(id):
    data = request.get_json()
    mongo.db.categorias.update_one({'_id': ObjectId(id)}, {'$set': {'nombre_categoria': data['nombre_categoria']}})
    return jsonify({'message': 'Categoría actualizada'})

@app.route('/api/categorias/<id>', methods=['DELETE'])
def delete_categoria(id):
    mongo.db.categorias.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Categoría eliminada'})

# --- CRUD Productos ---
@app.route('/api/productos', methods=['GET'])
def get_productos():
    productos = list(mongo.db.productos.find())
    productos = [fix_id(p) for p in productos]
    return jsonify(productos)

@app.route('/api/productos', methods=['POST'])
def create_producto():
    data = request.get_json()
    nuevo = {
        'nombre': data['nombre'],
        'descripcion': data.get('descripcion', ''),
        'stock': data.get('stock', 0),
        'precio': data.get('precio', 0),
        'id_categoria': data['id_categoria']
    }
    result = mongo.db.productos.insert_one(nuevo)
    return jsonify({'message': 'Producto creado', 'id': str(result.inserted_id)}), 201

@app.route('/api/productos/<id>', methods=['PUT'])
def update_producto(id):
    data = request.get_json()
    mongo.db.productos.update_one({'_id': ObjectId(id)}, {'$set': {
        'nombre': data['nombre'],
        'descripcion': data.get('descripcion', ''),
        'stock': data.get('stock', 0),
        'precio': data.get('precio', 0),
        'id_categoria': data['id_categoria']
    }})
    return jsonify({'message': 'Producto actualizado'})

@app.route('/api/productos/<id>', methods=['DELETE'])
def delete_producto(id):
    mongo.db.productos.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Producto eliminado'})

# --- CRUD Tipos Clientes ---
@app.route('/api/tipos-clientes', methods=['GET'])
def get_tipos_clientes():
    tipos = list(mongo.db.tipos_clientes.find())
    tipos = [fix_id(t) for t in tipos]
    return jsonify(tipos)

@app.route('/api/tipos-clientes', methods=['POST'])
def create_tipo_cliente():
    data = request.get_json()
    nuevo = {'descripcion': data['descripcion']}
    result = mongo.db.tipos_clientes.insert_one(nuevo)
    return jsonify({'message': 'Tipo cliente creado', 'id': str(result.inserted_id)}), 201

@app.route('/api/tipos-clientes/<id>', methods=['PUT'])
def update_tipo_cliente(id):
    data = request.get_json()
    mongo.db.tipos_clientes.update_one({'_id': ObjectId(id)}, {'$set': {'descripcion': data['descripcion']}})
    return jsonify({'message': 'Tipo cliente actualizado'})

@app.route('/api/tipos-clientes/<id>', methods=['DELETE'])
def delete_tipo_cliente(id):
    mongo.db.tipos_clientes.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Tipo cliente eliminado'})

# --- CRUD Clientes ---
@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    clientes = list(mongo.db.clientes.find())
    clientes = [fix_id(c) for c in clientes]
    return jsonify(clientes)

@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    nuevo = {
        'nombre_completo': data['nombre_completo'],
        'telefono': data.get('telefono', ''),
        'email': data.get('email', ''),
        'direccion': data.get('direccion', ''),
        'documento': data.get('documento', ''),
        'tipo_cliente_id': data['tipo_cliente_id']
    }
    result = mongo.db.clientes.insert_one(nuevo)
    return jsonify({'message': 'Cliente creado', 'id': str(result.inserted_id)}), 201

@app.route('/api/clientes/<id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()
    mongo.db.clientes.update_one({'_id': ObjectId(id)}, {'$set': {
        'nombre_completo': data['nombre_completo'],
        'telefono': data.get('telefono', ''),
        'email': data.get('email', ''),
        'direccion': data.get('direccion', ''),
        'documento': data.get('documento', ''),
        'tipo_cliente_id': data['tipo_cliente_id']
    }})
    return jsonify({'message': 'Cliente actualizado'})

@app.route('/api/clientes/<id>', methods=['DELETE'])
def delete_cliente(id):
    mongo.db.clientes.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Cliente eliminado'})

# --- CRUD Estados Factura ---
@app.route('/api/estados-facturas', methods=['GET'])
def get_estados_facturas():
    estados = list(mongo.db.estados_facturas.find())
    estados = [fix_id(e) for e in estados]
    return jsonify(estados)

@app.route('/api/estados-facturas', methods=['POST'])
def create_estado_factura():
    data = request.get_json()
    nuevo = {'descripcion': data['descripcion']}
    result = mongo.db.estados_facturas.insert_one(nuevo)
    return jsonify({'message': 'Estado factura creado', 'id': str(result.inserted_id)}), 201

@app.route('/api/estados-facturas/<id>', methods=['PUT'])
def update_estado_factura(id):
    data = request.get_json()
    mongo.db.estados_facturas.update_one({'_id': ObjectId(id)}, {'$set': {'descripcion': data['descripcion']}})
    return jsonify({'message': 'Estado factura actualizado'})

@app.route('/api/estados-facturas/<id>', methods=['DELETE'])
def delete_estado_factura(id):
    mongo.db.estados_facturas.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Estado factura eliminado'})

# --- CRUD Facturas ---
@app.route('/api/facturas', methods=['GET'])
def get_facturas():
    facturas = list(mongo.db.facturas.find())
    for f in facturas:
        f['_id'] = str(f['_id'])
        if 'fecha_factura' in f and f['fecha_factura'] is not None:
            f['fecha_factura'] = f['fecha_factura'].strftime('%Y-%m-%d') if hasattr(f['fecha_factura'], 'strftime') else str(f['fecha_factura'])
    return jsonify(facturas)

@app.route('/api/facturas', methods=['POST'])
def create_factura():
    data = request.get_json()
    fecha = data.get('fecha_factura')
    if fecha:
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        except:
            fecha = datetime.utcnow()
    else:
        fecha = datetime.utcnow()

    nuevo = {
        'id_cliente': data['id_cliente'],
        'fecha_factura': fecha,
        'metodo_pago': data.get('metodo_pago', ''),
        'id_estado': data['id_estado'],
        'total_facturas': data.get('total_facturas', 0)
    }
    result = mongo.db.facturas.insert_one(nuevo)
    return jsonify({'message': 'Factura creada', 'id': str(result.inserted_id)}), 201

@app.route('/api/facturas/<id>', methods=['PUT'])
def update_factura(id):
    data = request.get_json()
    fecha = data.get('fecha_factura')
    if fecha:
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        except:
            fecha = datetime.utcnow()
    else:
        fecha = datetime.utcnow()

    mongo.db.facturas.update_one({'_id': ObjectId(id)}, {'$set': {
        'id_cliente': data['id_cliente'],
        'fecha_factura': fecha,
        'metodo_pago': data.get('metodo_pago', ''),
        'id_estado': data['id_estado'],
        'total_facturas': data.get('total_facturas', 0)
    }})
    return jsonify({'message': 'Factura actualizada'})

@app.route('/api/facturas/<id>', methods=['DELETE'])
def delete_factura(id):
    mongo.db.facturas.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Factura eliminada'})

# --- CRUD Detalles Factura ---
@app.route('/api/detalles-factura', methods=['GET'])
def get_detalles_factura():
    detalles = list(mongo.db.detalles_factura.find())
    detalles = [fix_id(d) for d in detalles]
    return jsonify(detalles)

@app.route('/api/detalles-factura', methods=['POST'])
def create_detalle_factura():
    data = request.get_json()
    nuevo = {
        'id_factura': data['id_factura'],
        'id_producto': data['id_producto'],
        'cantidad': data.get('cantidad', 1),
        'precio_unitario': data.get('precio_unitario', 0)
    }
    result = mongo.db.detalles_factura.insert_one(nuevo)
    return jsonify({'message': 'Detalle factura creado', 'id': str(result.inserted_id)}), 201

@app.route('/api/detalles-factura/<id>', methods=['PUT'])
def update_detalle_factura(id):
    data = request.get_json()
    mongo.db.detalles_factura.update_one({'_id': ObjectId(id)}, {'$set': {
        'id_factura': data['id_factura'],
        'id_producto': data['id_producto'],
        'cantidad': data.get('cantidad', 1),
        'precio_unitario': data.get('precio_unitario', 0)
    }})
    return jsonify({'message': 'Detalle factura actualizado'})

@app.route('/api/detalles-factura/<id>', methods=['DELETE'])
def delete_detalle_factura(id):
    mongo.db.detalles_factura.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Detalle factura eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
