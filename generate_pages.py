import json
import os
import re
import math

# Mathematically exact EU flag SVG path generator
def get_eu_flag_svg(width=24, height=16):
    cx, cy = 405, 270
    radius = 135
    star_R = 15
    star_r = 5.7
    
    stars_paths = []
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        scx = cx + radius * math.cos(angle)
        scy = cy + radius * math.sin(angle)
        
        points = []
        for k in range(10):
            r_k = star_R if k % 2 == 0 else star_r
            phi = math.radians(k * 36 - 90)
            px = scx + r_k * math.cos(phi)
            py = scy + r_k * math.sin(phi)
            points.append(f"{px:.1f},{py:.1f}")
        
        stars_paths.append(f'<polygon points="{" ".join(points)}" fill="#ffcc00" />')
        
    svg = f'''<svg class="eu-flag-svg" viewBox="0 0 810 540" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="810" height="540" fill="#003399"/>
  {"".join(stars_paths)}
</svg>'''
    return svg

# Load data
json_path = r"C:\web_antigravity\web_soluciones_cluster_afolu\data\solutions.json"
with open(json_path, 'r', encoding='utf-8') as f:
    solutions = json.load(f)

# Define thematic filters mapping for each solution based on ID and content
def get_thematic_tags(sol):
    tags = []
    id_str = sol["id"]
    sala = sol["sala"]
    
    # 1. Cobertura y deforestación
    if sala == 1 or id_str in ["10", "11", "12", "13", "14", "18", "20"]:
        tags.append("cobertura")
        
    # 2. Incendios y alertas
    if sala == 2 or id_str in ["01", "02", "04", "05", "11", "15", "19"]:
        tags.append("incendios")
        
    # 3. Conectividad y biodiversidad
    if sala == 3 or id_str in ["01", "05", "06", "19"]:
        tags.append("conectividad")
        
    # 4. Agricultura y cadenas productivas
    if id_str in ["03", "14", "15", "17", "18", "20"]:
        tags.append("agricultura")
        
    # 5. EUDR
    if id_str in ["18", "20"]:
        tags.append("eudr")
        
    # 6. Carbono y biomasa
    if id_str in ["01", "11", "16", "19"]:
        tags.append("carbono")
        
    # 7. Plataformas y despliegue digital
    if id_str in ["02", "04", "05", "10", "16", "19", "20"]:
        tags.append("plataformas")
        
    return tags

# Update solutions data in-memory with thematic filter tags
for sol in solutions:
    sol["temas_filtro"] = get_thematic_tags(sol)

# Theme display names mapping
THEMES = {
    "all": "Todos",
    "cobertura": "Cobertura y deforestación",
    "incendios": "Incendios y alertas",
    "conectividad": "Conectividad y biodiversidad",
    "agricultura": "Agricultura y cadenas productivas",
    "eudr": "EUDR",
    "carbono": "Carbono y biomasa",
    "plataformas": "Plataformas y despliegue digital"
}

# Helper to escape HTML text
def esc(txt):
    return txt.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

# Helper to render table for Datos e Insumos
def make_data_table(sol):
    di = sol["datos_insumos"]
    
    doc_rel = di["documento_relacionado"]
    url_doc = di["url_documento"]
    if url_doc and url_doc != "No indicado en la ficha":
        doc_html = f'<a href="{esc(url_doc)}" target="_blank" style="color:var(--primary-color);text-decoration:underline;font-weight:600;">{esc(doc_rel)}</a>'
    else:
        doc_html = esc(doc_rel)
        
    ext_html = esc(di["enlace_externo"])
    if ext_html.startswith("http"):
        ext_html = f'<a href="{ext_html}" target="_blank" style="color:var(--primary-color);text-decoration:underline;font-weight:600;">Enlace externo</a>'

    rows = [
        ("Datos Satelitales / Fuentes Copernicus", di["satelitales_fuentes"]),
        ("Datos Locales Disponibles", di["disponibles"]),
        ("Datos Requeridos / Faltantes", di["faltantes"]),
        ("Documento Relacionado", doc_html),
        ("Enlaces Externos / Observaciones", ext_html)
    ]
    
    html = '<table class="data-table"><thead><tr><th>Insumo / Variable</th><th>Detalle en la Ficha</th></tr></thead><tbody>'
    for label, val in rows:
        html += f'<tr><td><strong>{label}</strong></td><td>{val}</td></tr>'
    html += '</tbody></table>'
    return html

# Helper to render tools badges
def make_tools_badges(sol):
    indices_str = sol["metodo_flujo"]["indices_algoritmos"].lower()
    tools = []
    if "google earth engine" in indices_str or "gee" in indices_str:
        tools.append("Google Earth Engine")
    if "qgis" in indices_str:
        tools.append("QGIS")
    if "arcgis" in indices_str:
        tools.append("ArcGIS Pro")
    if "python" in indices_str:
        tools.append("Python")
    if "r" in indices_str:
        tools.append("R")
    if "kobo" in indices_str:
        tools.append("KoboToolbox")
    if "github" in indices_str:
        tools.append("GitHub")
    
    if not tools:
        tools = ["Google Earth Engine", "QGIS", "Python"]
        
    badges_html = ""
    for t in tools:
        badges_html += f'<span class="tool-badge">{t}</span> '
    return badges_html


# Generate index.html (updated from Salas to Grupos)
def generate_index_html():
    cards_html = ""
    for sol in solutions:
        id_str = sol["id"]
        slug = sol["slug"]
        sala = sol["sala"]
        paises_str = ", ".join(sol["paises"])
        tags_str = ", ".join(sol["areas_tematicas"][:4])
        search_payload = f"{sol['titulo']} {sol['proponentes']} {sol['institucion']} {paises_str} {tags_str} Grupo {sala}"
        temas_list = ",".join(sol["temas_filtro"])
        
        cards_html += f'''
      <!-- Card {id_str} -->
      <div class="solution-card" data-sala="{sala}" data-temas="{temas_list}" data-search="{esc(search_payload)}">
        <div class="card-img-wrapper">
          <img src="assets/images/solucion-{id_str}.svg" alt="Ilustración {esc(sol['titulo'])}">
        </div>
        <div class="card-content">
          <span class="card-sala-tag">Grupo {sala}</span>
          <h3 class="card-title">{esc(sol['titulo'])}</h3>
          <div class="card-meta">
            <p><strong>Proponente:</strong> {esc(sol['proponentes'])}</p>
            <p><strong>Institución:</strong> {esc(sol['institucion'])}</p>
            <p><strong>País:</strong> {esc(paises_str)}</p>
          </div>
          <div class="card-tags">
        '''
        for tag in sol["areas_tematicas"][:3]:
            cards_html += f'<span class="card-tag">{esc(tag)}</span>'
            
        cards_html += f'''
          </div>
          <div class="card-action">
             <a href="pages/{slug}/index.html" class="btn-solution">Ver solución</a>
          </div>
        </div>
      </div>
        '''
        
    # Count stats
    total_solutions = len(solutions)
    paises_set = set()
    for s in solutions:
        paises_set.update(s["paises"])
    total_countries = len(paises_set)
    
    filter_tabs_html = ""
    for filter_key, filter_label in THEMES.items():
        active_class = "active" if filter_key == "all" else ""
        filter_tabs_html += f'<button class="filter-btn {active_class}" data-filter="{filter_key}">{filter_label}</button>\n'

    index_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Catálogo de Soluciones AFOLU-Copernicus - Clúster Copernicus AFOLU II</title>
  <link rel="stylesheet" href="css/styles.css">
  <meta name="description" content="Catálogo regional de soluciones e ideas de prototipado basadas en observación de la Tierra y Copernicus para el sector AFOLU en Mesoamérica y el Caribe.">
</head>
<body>

  <!-- EU Top Bar -->
  <div class="eu-top-bar">
    <div class="eu-top-bar-container">
      <div class="eu-brand-left">
        {get_eu_flag_svg(24, 16)}
        <span>Unión Europea</span>
      </div>
      <div class="eu-brand-divider"></div>
      <div class="eu-brand-right">
        <img src="assets/images/GG_logo-BLUE.svg" alt="Global Gateway" class="gg-logo-img">
      </div>
    </div>
  </div>

  <!-- Header Section -->
  <header class="main-header">
    <div class="container">
      <h1>Clúster Copernicus AFOLU II</h1>
      <p class="intro-text">Catálogo de Soluciones AFOLU-Copernicus</p>
      <p style="color: var(--accent-light); opacity: 0.8; max-width: 650px; margin: 0 auto; font-size: 0.95rem;">
        Plataforma del Laboratorio de Prototipado para la gestión forestal, agricultura sostenible, biodiversidad, monitoreo de incendios y uso del suelo en Centroamérica y el Caribe.
      </p>
      <div style="margin-top: 1.5rem;">
        <button id="btn-about" class="btn-about-gg">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle; margin-right:4px;">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="16" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12.01" y2="8"></line>
          </svg>
          Acerca de AFOLU II
        </button>
      </div>
    </div>
  </header>

  <!-- Stats Banner (updated "Salas de Trabajo" -> "Grupos de Soluciones") -->
  <div class="stats-banner">
    <div class="stat-item">
      <div class="stat-number">{total_solutions}</div>
      <div class="stat-label">Soluciones</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">{total_countries}</div>
      <div class="stat-label">Países</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">4</div>
      <div class="stat-label">Grupos de Soluciones</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">2026</div>
      <div class="stat-label">Año de Prototipado</div>
    </div>
  </div>

  <!-- Main Catalog Container -->
  <main class="catalog-container">
    
    <!-- Toolbar with Search and Filters -->
    <div class="toolbar">
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input type="text" id="search-input" placeholder="Buscar por título, proponente, institución, país o temas clave...">
      </div>
      
      <div class="filter-tabs">
        {filter_tabs_html}
      </div>
    </div>

    <!-- Grid of Solutions -->
    <div class="solutions-grid" id="solutions-grid">
      {cards_html}
      
      <!-- No Results State -->
      <div class="no-results" id="no-results" style="display: none;">
        <h3>No se encontraron soluciones</h3>
        <p>Prueba ajustando los filtros o el término de búsqueda.</p>
      </div>
    </div>

  </main>

  <!-- Footer -->
  <footer class="main-footer">
    <div class="container">
      <div class="footer-logo-wrapper">
        <img src="assets/images/GG_logo-WHITE.svg" alt="Global Gateway" class="gg-footer-logo">
      </div>
      <p class="copernicus-tag">Clúster Copernicus AFOLU II</p>
      <p>Laboratorio de Prototipado 2026</p>
      <p class="attribution">Una iniciativa para fortalecer la observación de la Tierra y la conservación regional en Mesoamérica y el Caribe.</p>
    </div>
  </footer>

  <!-- About Modal (Concept Note Context) -->
  <div id="about-modal" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Acerca del Clúster AFOLU II</h3>
        <button id="modal-close" class="modal-close">&times;</button>
      </div>
      <div class="modal-body">
        
        <div class="modal-section">
          <h4>1. Justificación y Contexto</h4>
          <p>En el marco de la estrategia <strong>Global Gateway</strong> de la Unión Europea y el Programa Indicativo Multianual (MIP 2021-2027), la transformación digital es una prioridad clave. La "ventana centroamericana" de la Digital Alliance integra tecnologías satelitales (Copernicus y Galileo) como pilares para la transición ecológica regional en el sector <strong>AFOLU</strong> (Agricultura, Silvicultura y Otros Usos del Suelo).</p>
          <p>El Clúster AFOLU II representa la consolidación técnica del Laboratorio de Prototipado, transitando de la formación teórica general hacia la creación de capacidades técnico-institucionales concretas, implementando soluciones operativas bajo el enfoque de <em>"aprender haciendo"</em> y <em>"Quick Wins"</em>.</p>
        </div>

        <div class="modal-section">
          <h4>2. Fases de la Iniciativa</h4>
          <div class="modal-timeline">
            <div class="timeline-item">
              <div class="timeline-meta">Fase I: Formación Virtual (Mayo - Junio 2026)</div>
              <div class="timeline-title">Capacitación y exploración</div>
              <div class="timeline-desc">7 seminarios virtuales de alta especialización para un grupo estable de 35 a 45 expertos regionales de los ministerios y organizaciones territoriales vinculadas a la CCAD, CAC y el Programa Grandes Bosques de Mesoamérica (PGBM).</div>
            </div>
            <div class="timeline-item">
              <div class="timeline-meta">Fase II: Desarrollo de Soluciones (Junio - Diciembre 2026)</div>
              <div class="timeline-title">Taller presencial y acompañamiento tutelado</div>
              <div class="timeline-desc">Taller presencial de 3 días intensivos utilizando metodologías ágiles (SCRUM) para consolidar los prototipos, dando inicio a un acompañamiento y tutoría técnica de 6 meses para integrar y estabilizar las soluciones dentro de las rutinas de trabajo institucionales.</div>
            </div>
          </div>
        </div>

        <div class="modal-section">
          <h4>3. Cronograma de Sesiones Virtuales</h4>
          <ul class="steps-list" style="margin-top:0.75rem;">
            <li><strong>Sesión 1 (21 Mayo):</strong> Presentación del PGBM y reforzamiento del ecosistema de productos y servicios Copernicus. <em>(Ricardo Montero, Roberto Matellanes)</em></li>
            <li><strong>Sesión 2 (26 Mayo):</strong> Servicios de incendios forestales de CopernicusLAC Panamá (prevención, alertas y post-incendio). <em>(INDRA, GIZ)</em></li>
            <li><strong>Sesión 3 (28 Mayo):</strong> Presentación del mapa panregional de cobertura y usos del suelo (LULC) de CopernicusLAC Chile. <em>(CopernicusLAC Chile)</em></li>
            <li><strong>Sesión 4 (2 Junio):</strong> Ejercicios y aplicaciones prácticas en el contexto de Mesoamérica. <em>(Christian Aguilar, Ariel Russell)</em></li>
            <li><strong>Sesión 5 (5 Junio):</strong> Métricas de paisaje, conectividad ecológica y carbono forestal. <em>(Lenin Corrales, GIZ)</em></li>
            <li><strong>Sesiones 6 y 7 (9 y 11 Junio):</strong> Talleres virtuales exploratorios para cociseño de prototipos de soluciones. <em>(Ariel Russell, GIZ)</em></li>
            <li><strong>Sesión 8 (24-26 Junio):</strong> Taller práctico presencial (SCRUM) para inicio del desarrollo del prototipo. <em>(GIZ, AECID, UCR, EUreCA)</em></li>
          </ul>
        </div>

        <div class="modal-section">
          <h4>4. Entidades y Socios Impulsores</h4>
          <div class="partner-grid">
            <div class="partner-card">
              <div class="partner-name">EUreCA</div>
              <div class="partner-role">Coordinación general de la facilidad, supervisión y soporte técnico.</div>
            </div>
            <div class="partner-card">
              <div class="partner-name">GIZ</div>
              <div class="partner-role">Diseño pedagógico, contenidos y apoyo en formación técnica de prototipado.</div>
            </div>
            <div class="partner-card">
              <div class="partner-name">PGBM</div>
              <div class="partner-role">Programa Grandes Bosques de Mesoamérica, soporte y financiamiento regional.</div>
            </div>
            <div class="partner-card">
              <div class="partner-name">Academia y UCR</div>
              <div class="partner-role">Escuela de Geografía de la UCR, UTP (Panamá), UVG (Guatemala) y UNA (Costa Rica) mediante AECID.</div>
            </div>
            <div class="partner-card">
              <div class="partner-name">CopernicusLAC</div>
              <div class="partner-role">Centros regionales de Chile y Panamá, aportando infraestructura de cómputo y expertos.</div>
            </div>
            <div class="partner-card">
              <div class="partner-name">CCAD y CAC</div>
              <div class="partner-role">Comisión Centroamericana de Ambiente y Desarrollo, Comité de Bosques e instancias del SICA.</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <script src="js/main.js"></script>
</body>
</html>
'''
    with open(r"C:\web_antigravity\web_soluciones_cluster_afolu\index.html", 'w', encoding='utf-8') as f:
      f.write(index_content)
    print("Generated index.html successfully with updated text.")

# Generate 20 landing HTML pages (updated "Sala" -> "Grupo")
def generate_landing_pages():
    for idx, sol in enumerate(solutions):
        id_str = sol["id"]
        slug = sol["slug"]
        
        prev_idx = (idx - 1) % len(solutions)
        next_idx = (idx + 1) % len(solutions)
        prev_sol = solutions[prev_idx]
        next_sol = solutions[next_idx]
        
        paises_str = ", ".join(sol["paises"])
        
        # Lat/lon details for Territory section
        lat = sol["territorio"]["latitud"]
        lon = sol["territorio"]["longitud"]
        punto = sol["territorio"]["punto_aproximado"]
        coords_html = ""
        if lat != "No indicado en la ficha" and lon != "No indicado en la ficha":
            coords_html = f'''
            <p><strong>Punto aproximado (Coordenadas):</strong> {esc(lat)}, {esc(lon)}</p>
            <p><strong>Ubicación de referencia:</strong> {esc(punto)}</p>
            '''
        elif punto != "No indicado en la ficha":
            coords_html = f'<p><strong>Punto aproximado:</strong> {esc(punto)}</p>'
            
        poligono = sol["territorio"]["poligono_aproximado"]
        poligono_html = ""
        if poligono != "No indicado en la ficha":
            poligono_html = f'<p><strong>Polígono aproximado:</strong> <span style="font-size:0.85rem; word-break:break-all; font-family:monospace; color:var(--text-secondary);">{esc(poligono[:120]) + ("..." if len(poligono) > 120 else "")}</span></p>'
            
        limites_str = sol["territorio"]["cuenta_limites"]
        archivo_lim = sol["territorio"]["archivo_limites"]
        url_lim = sol["territorio"]["url_limites"]
        limites_html = f"<p><strong>Cuenta con límites geoespaciales:</strong> {esc(limites_str)}</p>"
        if archivo_lim != "No indicado en la ficha":
            if url_lim != "No indicado en la ficha":
                limites_html += f'<p><strong>Archivo de límites:</strong> <a href="{esc(url_lim)}" target="_blank" style="color:var(--primary-color);text-decoration:underline;font-weight:600;">{esc(archivo_lim)}</a></p>'
            else:
                limites_html += f'<p><strong>Archivo de límites:</strong> {esc(archivo_lim)}</p>'
                
        req_act = sol["producto"]["requiere_actualizacion"]
        desc_act = sol["producto"]["descripcion_actualizacion"]
        act_html = f"<p><strong>Requiere actualización:</strong> {esc(req_act)}</p>"
        if desc_act != "No indicado en la ficha":
            act_html += f"<p><strong>Frecuencia / Método de actualización:</strong> {esc(desc_act)}</p>"
            
        data_table_html = make_data_table(sol)
        tools_html = make_tools_badges(sol)
        
        # Build HTML content (updated labels from Sala -> Grupo)
        page_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(sol['titulo'])} - Clúster Copernicus AFOLU II</title>
  <link rel="stylesheet" href="../../css/styles.css">
  <meta name="description" content="{esc(sol['titulo'])}. Idea de solución del Clúster Copernicus AFOLU II de {esc(sol['proponentes'])}.">
</head>
<body>

  <!-- EU Top Bar -->
  <div class="eu-top-bar">
    <div class="eu-top-bar-container">
      <div class="eu-brand-left">
        {get_eu_flag_svg(24, 16)}
        <span>Unión Europea</span>
      </div>
      <div class="eu-brand-divider"></div>
      <div class="eu-brand-right">
        <img src="../../assets/images/GG_logo-BLUE.svg" alt="Global Gateway" class="gg-logo-img">
      </div>
    </div>
  </div>

  <!-- Hero Section -->
  <section class="landing-hero">
    <div class="landing-hero-container">
      <div class="landing-hero-content">
        <a href="../../index.html" class="btn-back">
          <svg viewBox="0 0 24 24"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg>
          Volver al catálogo
        </a>
        <h2 style="margin-top: 1.5rem;">{esc(sol['titulo'])}</h2>
        
        <div class="landing-hero-meta">
          <div class="hero-meta-item">
            <span class="hero-meta-label">Proponente(s)</span>
            <span class="hero-meta-val">{esc(sol['proponentes'])}</span>
          </div>
          <div class="hero-meta-item">
            <span class="hero-meta-label">Institución</span>
            <span class="hero-meta-val">{esc(sol['institucion'])}</span>
          </div>
          <div class="hero-meta-item">
            <span class="hero-meta-label">País(es)</span>
            <span class="hero-meta-val">{esc(paises_str)}</span>
          </div>
          <div class="hero-meta-item">
            <span class="hero-meta-label">Grupo</span>
            <span class="hero-meta-val">Grupo {sol['sala']} - {esc(sol['grupo_trabajo'])}</span>
          </div>
        </div>
      </div>
      <div class="landing-hero-img">
        <img src="../../assets/images/solucion-{id_str}.svg" alt="Ilustración principal de la solución">
      </div>
    </div>
  </section>

  <!-- Main Content Layout -->
  <main class="landing-main">
    
    <!-- Body Content (Left Side) -->
    <div class="landing-body">
      
      <!-- Sección 2: Problema -->
      <section class="landing-section">
        <h3 class="landing-section-title">1. Problema que busca atender</h3>
        <p>{esc(sol['problema'])}</p>
      </section>

      <!-- Sección 3: Relevancia -->
      <section class="landing-section">
        <h3 class="landing-section-title">2. Relevancia del problema</h3>
        <p>{esc(sol['relevancia'])}</p>
      </section>

      <!-- Sección 6: Producto esperado -->
      <section class="landing-section">
        <h3 class="landing-section-title">3. Producto esperado</h3>
        <p><strong>Tipo de entregable:</strong> {esc(sol['producto']['tipo'])}</p>
        <p><strong>Descripción del producto:</strong> {esc(sol['producto']['descripcion'])}</p>
        <p><strong>Componentes de despliegue sugeridos:</strong> {esc(sol['producto']['componentes_despliegue'])}</p>
        <p><strong>Nivel de acceso previsto:</strong> {esc(sol['producto']['nivel_acceso'])}</p>
        <p><strong>Forma de uso institucional:</strong> {esc(sol['producto']['forma_uso'])}</p>
        {act_html}
      </section>

      <!-- Sección 7: Flujo de trabajo preliminar -->
      <section class="landing-section">
        <h3 class="landing-section-title">4. Flujo de trabajo preliminar</h3>
        <p>El siguiente diagrama conceptualiza el procesamiento de datos y flujo técnico sugerido para la solución:</p>
        
        <div class="diagram-container">
          <img src="../../assets/diagrams/proceso-{id_str}.svg" alt="Diagrama de flujo de proceso para {esc(sol['titulo'])}">
        </div>
        
        <p><strong>Descripción del flujo metodológico imaginado:</strong></p>
        <p>{esc(sol['metodo_flujo']['flujo_imaginado'])}</p>
        <p><strong>Algoritmos o índices clave:</strong> {esc(sol['metodo_flujo']['indices_algoritmos'])}</p>
      </section>

      <!-- Sección 8: Datos e insumos -->
      <section class="landing-section">
        <h3 class="landing-section-title">5. Datos e insumos identificados</h3>
        <p>Insumos satelitales y capas locales necesarias para el despliegue del prototipo:</p>
        <div class="data-table-wrapper">
          {data_table_html}
        </div>
      </section>

    </div>

    <!-- Sidebar Widget Columns (Right Side) -->
    <div class="landing-sidebar">
      
      <!-- Sección 4: Territorio -->
      <div class="sidebar-widget">
        <h4 class="sidebar-widget-title">Territorio de aplicación</h4>
        <p><strong>Referencia territorial:</strong> {esc(sol['territorio']['referencia'])}</p>
        {coords_html}
        {poligono_html}
        {limites_html}
      </div>

      <!-- Sección 5: Usuarios y Decisiones -->
      <div class="sidebar-widget">
        <h4 class="sidebar-widget-title">Usuarios y Decisiones</h4>
        <p><strong>Tipo de usuario:</strong> {esc(sol['usuarios_finales']['tipo'])}</p>
        <p><strong>Usuario final:</strong> {esc(sol['usuarios_finales']['descripcion'])}</p>
        <p style="margin-top:0.75rem;"><strong>Decisiones a apoyar:</strong></p>
        <p style="font-size:0.875rem; color:var(--text-secondary);">{esc(sol['usuarios_finales']['decision_apoyo'])}</p>
      </div>

      <!-- Sección 9: Herramientas sugeridas -->
      <div class="sidebar-widget">
        <h4 class="sidebar-widget-title">Herramientas sugeridas</h4>
        <div class="tools-list">
          {tools_html}
        </div>
        <p style="font-size:0.8rem; color:var(--text-light); margin-top:0.75rem;">
          Se sugieren estas herramientas por su madurez tecnológica y compatibilidad con Copernicus.
        </p>
      </div>

      <!-- Sección 10: Actividades preliminares -->
      <div class="sidebar-widget">
        <h4 class="sidebar-widget-title">Actividades preliminares</h4>
        <ul class="steps-list">
          <li>Organizar datos</li>
          <li>Definir AOI de referencia</li>
          <li>Preparar script inicial</li>
          <li>Generar indicadores básicos</li>
          <li>Validar resultados</li>
          <li>Preparar visualización</li>
          <li>Documentar flujo</li>
          <li>Definir ruta de despliegue</li>
        </ul>
      </div>

      <!-- Sección 11: Ruta de continuidad -->
      <div class="sidebar-widget">
        <h4 class="sidebar-widget-title">Ruta de continuidad</h4>
        <p><strong>Durante la jornada presencial:</strong></p>
        <p style="font-size:0.875rem; color:var(--text-secondary); margin-bottom:1rem;">{esc(sol['producto']['avance_presencial'])}</p>
        <p><strong>Acompañamiento posterior y despliegue:</strong></p>
        <p style="font-size:0.875rem; color:var(--text-secondary);">{esc(sol['metodo_flujo']['frecuencia_actualizacion'])} - Actualización requerida para dar continuidad técnica al prototipo.</p>
      </div>

      <!-- Asesoría Sesión 6 -->
      <div class="sidebar-widget" style="background-color: var(--accent-light); border-color: var(--accent-color);">
        <h4 class="sidebar-widget-title" style="color: var(--primary-color);">Pregunta para la Asesoría</h4>
        <p style="font-size:0.9rem; font-weight:600; color:var(--primary-color);">{esc(sol['preguntas_asesoria']['pregunta_principal'])}</p>
        <p style="font-size:0.8rem; color:var(--text-secondary); margin-top:0.5rem;"><strong>Áreas solicitadas:</strong> {esc(sol['preguntas_asesoria']['areas_asesoria'])}</p>
      </div>

    </div>

  </main>

  <!-- Footer Pagination & Navigation -->
  <section class="landing-pagination">
    <a href="../{prev_sol['slug']}/index.html" class="btn-nav">
      <svg viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
      Anterior: {esc(prev_sol['titulo'][:30])}...
    </a>
    
    <a href="../../index.html" class="btn-nav">
      Catálogo
    </a>
    
    <a href="../{next_sol['slug']}/index.html" class="btn-nav">
      Siguiente: {esc(next_sol['titulo'][:30])}...
      <svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
    </a>
  </section>

  <!-- Footer -->
  <footer class="main-footer">
    <div class="container">
      <div class="footer-logo-wrapper">
        <img src="../../assets/images/GG_logo-WHITE.svg" alt="Global Gateway" class="gg-footer-logo">
      </div>
      <p class="copernicus-tag">Clúster Copernicus AFOLU II</p>
      <p>Laboratorio de Prototipado 2026</p>
    </div>
  </footer>

</body>
</html>
'''
        page_dir = os.path.join(r"C:\web_antigravity\web_soluciones_cluster_afolu\pages", slug)
        os.makedirs(page_dir, exist_ok=True)
        page_path = os.path.join(page_dir, "index.html")
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
            
    print(f"Generated {len(solutions)} landing pages successfully (updated with Grupo text).")

# Execute generations
generate_index_html()
generate_landing_pages()
print("All HTML pages generated with the new terminology (Grupo / Grupos de Soluciones)!")
