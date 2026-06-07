# Sistema Cognitivo de Gestión de Inventarios (MCP)

Este proyecto implementa un servidor basado en **Model Context Protocol (MCP)** utilizando Python y FastMCP. Permite a los Modelos de Lenguaje (LLMs) interactuar directamente con una base de datos SQLite para realizar operaciones CRUD y análisis estadísticos en tiempo real sobre un inventario.

## Estructura del Proyecto
- `server.py`: Servidor MCP principal con las herramientas expuestas.
- `database.py`: Inicialización y configuración de la base de datos SQLite3.
- `requirements.txt`: Librerías necesarias.
- `inventory.db`: Base de datos relacional local (generada automáticamente).

## Requisitos e Instalación
1. Asegúrese de tener Python 3.8 o superior instalado.
2. Instale las dependencias mediante la terminal:
   ```bash
   pip install -r requirements.txt