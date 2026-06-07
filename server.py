from mcp.server.fastmcp import FastMCP
from fastapi.responses import HTMLResponse
import sqlite3

# 1. Crear la instancia del servidor MCP (¡Esta es la línea que faltaba!)
server = FastMCP("Inventory Server")

# 2. El Panel de Control Visual para tu navegador web
@server.fastapi_app.get("/", response_class=HTMLResponse)
async def home_dashboard():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
    except Exception:
        products = []
    finally:
        conn.close()

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sistema de Gestión de Inventario - IBERO</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; }
            h1 { color: #2c3e50; }
            .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px; border: 1px solid #ddd; text-align: left; }
            th { background-color: #34495e; color: white; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            .badge { background-color: #27ae60; color: white; padding: 5px 10px; border-radius: 4px; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📋 Panel de Control - Inventario Inteligente (IBERO)</h1>
            <p>Estado del Servidor: <span class="badge">En Línea Activo</span></p>
            <hr>
            <h3>Productos en Base de Datos:</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre del Producto</th>
                        <th>Cantidad en Stock</th>
                        <th>Precio Unitario</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    if not products:
        html_content += "<tr><td colspan='4' style='text-align:center; padding:20px; color:#7f8c8d;'>La base de datos 'inventory.db' está conectada con éxito. Agrega registros para verlos listados aquí.</td></tr>"
    else:
        for prod in products:
            html_content += f"<tr><td>{prod[0]}</td><td>{prod[1]}</td><td>{prod[2]}</td><td>${prod[3]}</td></tr>"
            
    html_content += """
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    return html_content