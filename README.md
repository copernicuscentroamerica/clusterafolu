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

1. Navega hasta la carpeta donde clonaste o descargaste el proyecto en tu computadora (por ejemplo: `C:\ruta\al\proyecto\clusterafolu`) y haz doble clic sobre el archivo **`index.html`** para abrirlo en tu navegador de preferencia.
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

---

## 🛠️ Guía de Contribución para los Equipos de Solución

Para mantener el repositorio ordenado y permitir que cada uno de los 20 equipos enriquezca su solución de forma independiente, se debe seguir un flujo de trabajo lógico y ordenado. 

> [!IMPORTANT]
> **Permisos de Escritura (Acceso a GitHub):**
> Cualquier persona puede clonar el repositorio de forma pública y trabajar localmente en su computadora. Sin embargo, para poder subir tus cambios de vuelta al repositorio central en GitHub (`git push`), **necesitas ser miembro del proyecto**.
> 
> **Cómo solicitar acceso:**
> Envía un correo electrónico a **copernicuscentroamerica@gmail.com** (o escribe a través del canal oficial del Clúster) indicando:
> 1. Tu **nombre completo** e **institución**.
> 2. El **nombre o número de tu solución** (ej: *Solución 01 - Gestión del Paisaje Montecristo*).
> 3. Tu **nombre de usuario de GitHub** (ej: *mi-usuario-github*).
> 
> *Nota: Una vez que el administrador te agregue, recibirás un correo de invitación de GitHub. También puedes aceptar la invitación directamente visitando [https://github.com/copernicuscentroamerica/clusterafolu/invitations](https://github.com/copernicuscentroamerica/clusterafolu/invitations).*

A continuación, haz clic en cada sección desplegable para ver las instrucciones en orden cronológico:

<details>
<summary><b>📥 1. Cómo Clonar y Sincronizar el Repositorio (Primer Paso Obligatorio)</b></summary>

Para descargar el proyecto a tu computadora y comenzar a trabajar de forma local sincronizada:

1. **Clonar por primera vez**:
   * Abre tu terminal (PowerShell, Git Bash o CMD) en tu computadora.
   * Navega a la carpeta de tu preferencia donde deseas guardar el proyecto (por ejemplo, `C:\proyectos` o `Documents`):
     ```powershell
     cd C:\ruta\a\tu\carpeta\de\preferencia
     ```
   * Clona el repositorio oficial ejecutando el siguiente comando:
     ```powershell
     git clone https://github.com/copernicuscentroamerica/clusterafolu.git
     ```
   * Entra a la carpeta del proyecto recién clonado:
     ```powershell
     cd clusterafolu
     ```

2. **Trabajo diario - Sincronizar cambios**:
   Antes de empezar a añadir o modificar archivos en tu solución local, **siempre** debes descargarte las últimas modificaciones hechas por otros equipos para evitar conflictos de fusión (merge conflicts). Ejecuta en la terminal:
   ```powershell
   git pull origin main
   ```
</details>

<details>
<summary><b>📂 2. Cómo Organizar los Datos y Documentos de tu Solución</b></summary>

Una vez que tengas el repositorio clonado localmente, busca la carpeta asignada a tu solución dentro de la carpeta `pages/` (por ejemplo, `pages/01-gestion-paisaje-montecristo/`).

Cada equipo debe estructurar su espacio local creando las siguientes subcarpetas dentro del directorio de su solución:
*   `datos/`: Para guardar archivos de datos locales (CSV, GeoJSON, Shapefiles, KML, etc.).
*   `documentos/`: Para subir manuales de usuario, reportes en PDF, fichas complementarias y metodologías detalladas.

*Ejemplo de estructura de archivos esperada:*
```text
pages/01-gestion-paisaje-montecristo/
├── index.html (la landing page principal de la solución)
├── datos/
│   └── limites_montecristo.geojson
└── documentos/
    └── manual_usuario_v1.pdf
```
</details>

<details>
<summary><b>💻 3. Cómo Subir y Documentar Scripts (Python / R)</b></summary>

Si tu solución incluye código de procesamiento (ej. Google Earth Engine, scripts de Python, R, o Notebooks de Jupyter):
1. Crea una carpeta llamada `scripts/` dentro del directorio de tu solución (ej. `pages/01-gestion-paisaje-montecristo/scripts/`).
2. Guarda allí tus archivos de código (ej. `analisis.py`, `procesamiento.R`, `gee_code.js`).
3. Añade un archivo de texto simple `README.md` **dentro de esa carpeta de scripts** detallando las librerías necesarias y cómo ejecutar el código.
</details>

<details>
<summary><b>🚀 4. Cómo Guardar y Subir tus Cambios a GitHub (Comandos Git)</b></summary>

Para registrar localmente tus avances y subirlos de forma segura al repositorio remoto en GitHub:

1. Abre tu terminal y colócate en la raíz de tu repositorio local clonado:
   ```powershell
   cd C:\ruta\local\donde\clonaste\el\proyecto\clusterafolu
   ```
2. Añade los nuevos archivos y carpetas que hayas creado en el directorio de tu solución (por ejemplo, tus carpetas de `datos/`, `documentos/` o `scripts/`):
   ```powershell
   git add pages/nombre-de-tu-solucion/
   ```
3. Guarda el registro de tus cambios localmente creando un commit descriptivo:
   ```powershell
   git commit -m "Add: scripts y datos para la solucion XX"
   ```
4. Sube tus cambios al repositorio remoto en GitHub para compartirlos con el equipo:
   ```powershell
   git push origin main
   ```
   *(Nota: Si no tienes permisos de colaborador, este comando fallará pidiéndote autenticación. Asegúrate de haber solicitado acceso de escritura previamente).*
</details>

<details>
<summary><b>🔑 5. Para Administradores: Cómo gestionar accesos y proteger carpetas específicas</b></summary>

En Git y GitHub no existe un control de permisos de lectura/escritura a nivel de carpetas individuales por defecto (cualquier colaborador invitado al repositorio tiene permisos de escritura en todo el proyecto). 

Para poder asociar equipos de trabajo a soluciones específicas y evitar que un equipo modifique accidentalmente la carpeta de otra solución, los administradores deben seguir estos pasos:

1. **Añadir Colaboradores al Repositorio**:
   * Ve al repositorio en GitHub y haz clic en **Settings** (Configuración) > **Collaborators** (Colaboradores).
   * Presiona **Add people** (Añadir personas), ingresa el usuario o correo de GitHub del miembro del equipo y envíale la invitación con rol de **Write** (Escritura).

2. **Configurar Propietarios de Carpeta (CODEOWNERS)**:
   * Ya hemos pre-creado el archivo **`.github/CODEOWNERS`** en la raíz del repositorio con la estructura para las 20 soluciones.
   * Abre y edita este archivo para reemplazar los marcadores `@usuario-equipo-X` con los nombres de usuario reales de GitHub de los responsables de cada carpeta.
   * Por ejemplo:
     ```text
     # Ruta de la carpeta de solución                  # Usuario(s) responsable(s)
     /pages/01-gestion-paisaje-montecristo/            @maria-trifinio
     /pages/02-analisis-multitemporal-cobertura-forestal/ @juan-icf @marlon-diaz
     ```
   * Haz commit y sube los cambios del archivo editado a la rama principal (`main`).

3. **Activar las Reglas de Protección de Ramas**:
   * En la configuración del repositorio en GitHub, ve a **Settings** > **Branches** (Ramas).
   * En *Branch protection rules*, presiona **Add branch protection rule** (Añadir regla de protección de rama).
   * Escribe `main` en *Branch name pattern*.
   * Marca las siguientes casillas:
     * **"Require a pull request before merging"** (Requerir Pull Request antes de fusionar).
     * **"Require review from Code Owners"** (Requerir revisión de los Propietarios de Código).
   * Con esta configuración, cualquier cambio en la carpeta de una solución protegida en `pages/` requerirá obligatoriamente la revisión y aprobación del propietario o miembros asignados a esa carpeta en el archivo `CODEOWNERS` antes de poder integrarse a `main`.
</details>
