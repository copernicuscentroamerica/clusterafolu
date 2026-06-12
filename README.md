# Clúster Copernicus AFOLU II - Catálogo de Soluciones AFOLU-Copernicus

Este proyecto contiene un catálogo web que presenta 20 ideas de soluciones que están siendo diseñadas en el marco del **Clúster Copernicus AFOLU II**.

El objetivo del sitio es documentar los prototipos técnicos propuestos para la gestión forestal, agricultura sostenible, biodiversidad, restauración y cumplimiento del reglamento EUDR en Mesoamérica y República Dominicana, utilizando datos de observación de la Tierra.

---

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```text
web_soluciones_cluster_afolu/
│
├── index.html                           # Catálogo general interactivo (20 soluciones)
├── README.md                            # Este archivo instructivo y de documentación
├── generate_pages.py                    # Script de Python para regenerar las páginas HTML
├── verify_site.py                       # Script de Python para verificar enlaces e integridad del sitio
│
├── data/
│   └── solutions.json                   # Base de datos estructurada en JSON
│
├── css/
│   └── styles.css                       # Estilos CSS responsivos
│
├── js/
│   └── main.js                          # Control de búsqueda y filtrado dinámico en tiempo real
│
├── pages/                               # 20 Directorios independientes por solución
│   ├── 01-gestion-paisaje-montecristo/
│   │   └── index.html                   # Landing page e índice de la solución
│   ├── 02-analisis-multitemporal-cobertura-forestal/
│   │   └── index.html
│   ├── ...
│   └── 20-agroeudr-miambiente/
│       └── index.html
│
├── assets/                              # Recursos visuales estáticos
│   ├── images/
│   │   ├── solucion-01.svg              # Ilustración vectorial de portada para cada solución
│   │   └── ...
│   ├── diagrams/
│   │   ├── proceso-01.svg               # Diagrama conceptual del flujo de trabajo técnico
│   │   └── ...
│   └── icons/                           # Íconos auxiliares
│
└── insumos/                             # Insumos originales
    ├── Fichas Word consolidadas
    └── Excel original de respuestas del formulario de la ídea inicial las soluciones propuestas
```

---

## Cómo Abrir y Navegar por el Sitio Web

El sitio web está diseñado para funcionar **completamente de forma local**, sin necesidad de servidores web adicionales, conexiones a bases de datos ni conexión a internet activa (a menos que se desee descargar fuentes tipográficas de Google Fonts).

1. Navega hasta la carpeta del proyecto
2. Haz doble clic sobre el archivo **`index.html`** para abrirlo en tu navegador de preferencia.
3. Utiliza la **barra de búsqueda** en tiempo real para buscar soluciones específicas por título, proponente, institución, país o palabras clave.
4. Utiliza las **pestañas de filtro** temáticas (ej: *EUDR*, *Incendios y alertas*, *Conectividad y biodiversidad*) para segmentar las soluciones según sus áreas de enfoque.
5. Haz clic en **"Ver solución"** en cualquier tarjeta para abrir la landing page de esa solución.
6. En la parte inferior de cada landing page, dispones de botones de navegación rápida ("Anterior", "Catálogo", "Siguiente") con comportamiento circular para recorrer de forma continua las 20 propuestas.

---

## Decisiones de Consolidación e Insumos

De acuerdo con las instrucciones de calidad y alcance del proyecto:
1. **Fichas Word como Fuente de Verdad**: La información fue extraída directamente de las **20 fichas de documentación técnica (archivos Word)** presentes en la carpeta `insumos/`.
2. **Campos Faltantes**: En los casos en que una ficha original no especificaba un campo en particular (como coordenadas, archivos de límites exactos, o preguntas de validación), el sistema registra explícitamente la leyenda `"No indicado en la ficha"` para preservar la integridad científica y evitar la invención de información institucional.

---

## Cómo Editar y Actualizar el Sitio Web

### 1. Actualización de Datos de Soluciones
Si necesitas corregir o añadir datos en las soluciones:
1. Abre el archivo **`data/solutions.json`** en un editor de texto (como Notepad++, VS Code, o el bloc de notas).
2. Localiza el objeto correspondiente a la solución mediante su `"id"` (ej: `"01"`, `"02"`, etc.).
3. Edita los textos y guarda el archivo.
4. Para aplicar estos cambios a las landing pages y al catálogo, puedes ejecutar de nuevo los scripts de generación automáticos (ver sección de automatización más abajo), o bien editar directamente los archivos HTML individuales en `pages/` e `index.html` si se trata de cambios muy específicos.

### 2. Personalización de Diseño y Estilos
Los colores, tipografías y estructura visual se gestionan centralizadamente desde **`css/styles.css`**.
- El sitio utiliza **variables de CSS** (`:root`) para controlar la paleta de colores corporativa. Puedes cambiar fácilmente los colores primarios (azules), secundarios (verdes forestales) y de acento en una sola línea dentro del bloque `:root`.
- El diseño utiliza un sistema de rejilla flexible (Grid y Flexbox) totalmente adaptable a pantallas móviles, tablets y escritorios.

---

## Automatización y Mantenimiento del Sitio (Para Desarrolladores)

El proyecto cuenta con scripts de Python ubicados en la raíz del repositorio para facilitar la generación y validación del catálogo de soluciones:

1. **`generate_pages.py`**: Lee `data/solutions.json` y compila las plantillas para generar el archivo `index.html` y las 20 carpetas individuales con su respectivo `index.html` dentro de `pages/` de manera consistente y automatizada.
2. **`verify_site.py`**: Valida automáticamente la integridad del sitio web, asegurando que no existan enlaces rotos entre el catálogo principal, las páginas de soluciones, las imágenes y diagramas de flujo de procesos.

Si tienes Python instalado, puedes ejecutar estos scripts en la consola para regenerar y verificar el sitio tras cualquier modificación:
```powershell
python generate_pages.py
python verify_site.py
```
