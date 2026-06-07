from database import init_db, DB_NAME
import sqlite3

init_db()

def get_connection():
    return sqlite3.connect(DB_NAME)

# ── FUNCIONES (copia igual que en server.py) ─────────────────────────────────

def crear_producto(nombre, categoria, cantidad, precio):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, categoria, cantidad, precio) VALUES (?, ?, ?, ?)",
        (nombre, categoria, cantidad, precio)
    )
    conn.commit()
    conn.close()
    return "Producto creado exitosamente"

def consultar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "nombre": row[1], "categoria": row[2], "cantidad": row[3], "precio": row[4]}
    return {"error": "Producto no encontrado"}

def actualizar_producto(id, cantidad):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id))
    conn.commit()
    conn.close()
    return "Producto actualizado correctamente"

def eliminar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return "Producto eliminado correctamente"

def listar_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nombre": r[1], "categoria": r[2], "cantidad": r[3], "precio": r[4]} for r in rows]

def calcular_valor_total_inventario():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(cantidad * precio) FROM productos")
    total = cursor.fetchone()[0]
    conn.close()
    return {"valor_total_inventario": total if total else 0}

def productos_agotados():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad = 0")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nombre": r[1], "categoria": r[2], "cantidad": r[3], "precio": r[4]} for r in rows]

def producto_mas_costoso():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY precio DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "nombre": row[1], "categoria": row[2], "cantidad": row[3], "precio": row[4]}
    return {"error": "No hay productos"}

def estadisticas_inventario():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*), AVG(cantidad), AVG(precio), SUM(cantidad * precio) FROM productos")
    total, prom_cant, prom_precio, valor = cursor.fetchone()
    conn.close()
    return {"total_productos": total, "promedio_cantidad": prom_cant, "promedio_precio": prom_precio, "valor_total": valor if valor else 0}

# ── PRUEBAS ───────────────────────────────────────────────────────────────────

print("=" * 50)
print("PRUEBA 1 - Crear 5 productos")
print("=" * 50)
print(crear_producto("Laptop", "Electrónica", 10, 2500000))
print(crear_producto("Mouse", "Electrónica", 50, 45000))
print(crear_producto("Silla ergonómica", "Muebles", 0, 380000))
print(crear_producto("Teclado mecánico", "Electrónica", 15, 120000))
print(crear_producto("Monitor 24\"", "Electrónica", 8, 850000))

print("\n" + "=" * 50)
print("PRUEBA 2 - Consultar producto por ID (id=1)")
print("=" * 50)
print(consultar_producto(1))

print("\n" + "=" * 50)
print("PRUEBA 3 - Actualizar cantidad del producto id=2")
print("=" * 50)
print(actualizar_producto(2, 35))

print("\n" + "=" * 50)
print("PRUEBA 4 - Eliminar producto id=5")
print("=" * 50)
print(eliminar_producto(5))

print("\n" + "=" * 50)
print("PRUEBA 5 - Listar todos los productos")
print("=" * 50)
for p in listar_productos():
    print(p)

print("\n" + "=" * 50)
print("PRUEBA 6 - Valor total del inventario")
print("=" * 50)
print(calcular_valor_total_inventario())

print("\n" + "=" * 50)
print("PRUEBA 7 - Productos agotados")
print("=" * 50)
print(productos_agotados())

print("\n" + "=" * 50)
print("PRUEBA 8 - Producto más costoso")
print("=" * 50)
print(producto_mas_costoso())

print("\n" + "=" * 50)
print("PRUEBA 9 - Estadísticas generales")
print("=" * 50)
print(estadisticas_inventario())