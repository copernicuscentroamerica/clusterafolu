# Clúster Copernicus AFOLU II - Catálogo de Soluciones AFOLU-Copernicus

Este proyecto contiene un catálogo web estático, interactivo e institucional que presenta las 20 ideas de solución diseñadas en el marco del **Clúster Copernicus AFOLU II (Laboratorio de Prototipado 2026)**.

El objetivo del sitio es documentar de forma clara y accesible los prototipos técnicos propuestos para la gestión forestal, agricultura sostenible, biodiversidad, restauración y cumplimiento del reglamento EUDR en Centroamérica y el Caribe, utilizando datos de observación de la Tierra y productos Copernicus.

---

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```text
web_soluciones_cluster_afolu/
│
├── index.html                           # Catálogo general interactivo (20 soluciones)
├── README.md                            # Este archivo instructivo y de documentación
│
├── data/
│   └── solutions.json                   # Base de datos estructurada en JSON
│
├── css/
│   └── styles.css                       # Estilos CSS premium, responsivos y con identidad visual
│
├── js/
│   └── main.js                          # Control de búsqueda y filtrado dinámico en tiempo real
│
├── pages/                               # 20 Landing Pages individuales
│   ├── 01-gestion-paisaje-montecristo.html
│   ├── 02-analisis-multitemporal-cobertura-forestal.html
│   ├── ...
│   └── 20-agroeudr-miambiente.html
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
└── insumos/                             # Insumos originales (no modificados)
    ├── Fichas Word consolidadas
    └── Excel original de respuestas
```

---

## Cómo Abrir y Navegar por el Sitio Web

El sitio web está diseñado para funcionar **completamente de forma local**, sin necesidad de servidores web adicionales, conexiones a bases de datos ni conexión a internet activa (a menos que se desee descargar fuentes tipográficas de Google Fonts).

1. Navega hasta la carpeta del proyecto en tu computadora: `C:\web_antigravity\web_soluciones_cluster_afolu`
2. Haz doble clic sobre el archivo **`index.html`** para abrirlo en tu navegador de preferencia (Google Chrome, Microsoft Edge, Mozilla Firefox o Safari).
3. Utiliza la **barra de búsqueda** en tiempo real para buscar soluciones específicas por título, proponente, institución, país o palabras clave.
4. Utiliza las **pestañas de filtro** temáticas (ej: *EUDR*, *Incendios y alertas*, *Conectividad y biodiversidad*) para segmentar las soluciones según sus áreas de enfoque.
5. Haz clic en **"Ver solución"** en cualquier tarjeta para abrir la landing page de esa solución.
6. En la parte inferior de cada landing page, dispones de botones de navegación rápida ("Anterior", "Catálogo", "Siguiente") con comportamiento circular para recorrer de forma continua las 20 propuestas.

---

## Decisiones de Consolidación e Insumos

De acuerdo con las instrucciones de calidad y alcance del proyecto:
1. **Fichas Word como Fuente de Verdad**: La información fue extraída directamente de las **20 fichas de documentación técnica (archivos Word)** presentes en la carpeta `insumos/`. El archivo Excel se usó únicamente como fuente secundaria de verificación debido a que contenía registros obsoletos, duplicados o previos a las versiones finales acordadas.
2. **Campos Faltantes**: En los casos en que una ficha original no especificaba un campo en particular (como coordenadas, archivos de límites exactos, o preguntas de validación), el sistema registra explícitamente la leyenda `"No indicado en la ficha"` para preservar la integridad científica y evitar la invención de información institucional.
3. **Mapeo de las 20 Soluciones**:
   - **ID 01**: Freddy Díaz – Macizo Montecristo.
   - **ID 02**: Marlon Díaz – Cobertura Forestal Honduras.
   - **ID 03**: Willy Castañeda – Frontera Agrícola El Salvador.
   - **ID 04**: FONAFIFO – Cambios de Cobertura PSA Costa Rica.
   - **ID 05**: Florencio García – Sistema Monitoreo Satelital ANP México.
   - **ID 06**: Néstor Muñoz & Jesús Constantino – Conectividad y Hábitat Selva Maya.
   - **ID 07**: Anthony Morgan – Belize Heat Points and Burn Scar.
   - **ID 08**: Amílcar López – Cicatrices de Fuego El Salvador.
   - **ID 09**: CONAP / Alvin Mayen & Greysi González – Incendios Petén.
   - **ID 10**: Antonio Clemente – Detección Temprana Uso Suelo Panamá.
   - **ID 11**: Ana Cristina Moreno – Valle Nuevo Cobertura e Incendios.
   - **ID 12**: Manuel Morales – Paso del Puma Costa Rica.
   - **ID 13**: Oscar Barrantes – Conectividad Ecológica Gran Bosque La Amistad.
   - **ID 14**: Zamorano – Conectividad y Ganadería Río Plátano.
   - **ID 15**: MAG Costa Rica – Alerta Temprana Plagas Musáceas.
   - **ID 16**: Mauricio Vega – Monitoreo Plantaciones Forestales.
   - **ID 17**: Marco Rodríguez – Cosecha Café Guatemala.
   - **ID 18**: Nikte’ Cú Chén – Cacao Libre de Deforestación.
   - **ID 19**: Fundación NATURA – Seguimiento Territorial Cuenca del Canal.
   - **ID 20**: Roney Samaniego – AGROEUDR_MIAMBIENTE Panamá.

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

## Automatización y Regeneración del Sitio (Para Desarrolladores)

En la carpeta temporal de desarrollo se utilizaron dos scripts de Python que facilitan la generación de contenidos a partir de la fuente de datos:
1. **`parse_data_and_generate.py`**: Lee los archivos `.docx` directamente de `insumos/`, extrae su estructura clave, la limpia e inicializa los directorios del sitio, generando `data/solutions.json`.
2. **`generate_svgs.py`**: Genera dinámicamente las 20 ilustraciones conceptuales (`assets/images/`) y los 20 diagramas de flujo de proceso (`assets/diagrams/`) con la identidad cromática de cada sala de discusión.
3. **`generate_pages.py`**: Lee `data/solutions.json` y compila las plantillas para generar el archivo `index.html` y las 20 landing pages en `pages/` de manera consistente y automatizada.

Si tienes Python instalado (por ejemplo, a través de QGIS Python), puedes ejecutar estos scripts en la consola para regenerar el sitio tras cualquier modificación masiva:
```powershell
python parse_data_and_generate.py
python generate_svgs.py
python generate_pages.py
```
