# Auditoría SEO rápida · SERRA-S Immobiliàries (serra-s.com)

**Fecha:** 7 de septiembre de 2026 · **Preparado por:** Sultox · **Para:** Serra-S Immobiliàries, Santa Susanna

> Método: comprobación directa de la web (títulos, descripciones, redirecciones, hreflang, robots, sitemap, plataforma) el 7 de septiembre de 2026, análisis de lo que Google tiene indexado de serra-s.com y serra-s.es, presencia en portales (idealista, habitaclia) y comparación con la competencia local.

---

## Resumen en 3 líneas

1. La web corporativa está bien montada por dentro (WordPress, redirecciones, sitemap, caché), pero **Google no sabe qué es ni dónde está**: la portada se titula "Inici", ninguna página tiene descripción y Yoast SEO está instalado sin configurar.
2. **Los inmuebles no están en la web.** Viven en serra-s.es, la web de Inmovilla del cliente, donde el listado tiene el mismo título que la portada y cada ficha se titula con el titular comercial del agente, sin marca ni "en venta". De más de 100 inmuebles, en nuestras búsquedas Google solo muestra uno, y ya retirado. Las fichas antiguas de serra-s.com dan 404.
3. Lo primero se arregla en **una semana sin tocar el diseño**. Lo segundo tiene solución conocida: plantilla actual de Inmovilla o conector Inmovilla → WordPress.

---

## Hallazgos por prioridad

### 1. CRÍTICO · Los títulos no dicen a qué os dedicáis ni dónde, y no hay descripciones

| Página | `<title>` real | Meta description |
|---|---|---|
| `www.serra-s.com/` | Inici | Ninguna |
| `/es/serra-s-inmobiliaries-compraventa-de-inmuebles/` | Inicio | Ninguna |
| `/contacte/` | Contacte - SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquiler | Ninguna |
| `/es/noticias/` | Noticias - SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquiler | Google lo corta |
| `www.serra-s.es/` (y todas sus páginas) | SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquil... | "servicio de Broker hipotecario, Renta vitalicia, Certificados Energéticos, Cédulas de habitabilidad, seguros de impago y seguros de hogar" |

Ni "inmobiliaria" ni "Santa Susanna" en ningún título. Google reescribe la portada a veces como "SERRA-S inmobiliàries". En serra-s.es el título ya viene cortado con "..." en el propio HTML.

Para comparar: la página de inmuebles en venta de VirtuaHome (`inmuebles.virtuahome.es/venta.php`) sale como "La Mejor Inmobiliaria de Santa Susana | VirtuaHome.es". Su portada, en cambio, se titula "INICIO - VIRTUA HOME": la mayoría de agencias de la zona tienen el mismo problema, y quien lo arregle primero se lleva las búsquedas. En Santa Susanna hay 47 agencias en idealista.

**Títulos propuestos**

| Página | Título propuesto (CA) | Título propuesto (ES) |
|---|---|---|
| Portada | Immobiliària a Santa Susanna · Compra, venda i lloguer al Maresme \| SERRA-S | Inmobiliaria en Santa Susanna · Compra, venta y alquiler en el Maresme \| SERRA-S |
| Comprar | Pisos i cases en venda a Santa Susanna i l'Alt Maresme \| SERRA-S | Pisos y casas en venta en Santa Susanna y el Alt Maresme \| SERRA-S |
| Alquilar | Pisos de lloguer a Santa Susanna, Malgrat i Pineda \| SERRA-S | Pisos de alquiler en Santa Susanna, Malgrat y Pineda \| SERRA-S |
| Vender | Vols vendre el teu pis al Maresme? Valoració gratuïta \| SERRA-S | ¿Quieres vender tu piso en el Maresme? Valoración gratuita \| SERRA-S |
| Ficha inmueble (automático) | {Tipo} en venda a {Municipi} · {m²} m² · {Preu} € \| SERRA-S | {Tipo} en venta en {Municipio} · {m²} m² · {Precio} € \| SERRA-S |
| Noticias | Notícies del mercat immobiliari al Maresme \| SERRA-S | Noticias del mercado inmobiliario en el Maresme \| SERRA-S |

Cada página necesita además una **meta description** de 140 a 155 caracteres con el teléfono y la zona.

**Solución:** Yoast SEO está instalado y activo (robots y sitemap los genera él). Solo hay que rellenar títulos y descripciones por página en CA y ES. Configuración, no programación.

### 2. CRÍTICO · Los inmuebles viven fuera de la web y Google no los ve

- `www.serra-s.com` (WordPress, tema Enfold, WPML, Yoast, W3 Total Cache) tiene **15 páginas** y ninguna ficha de inmueble ni página de comprar/vender/alquilar. El menú enlaza a `serra-s.es/venta.php` y `serra-s.es/alertas.php?idio=1`.
- `www.serra-s.es` es la **web de Inmovilla** del cliente (`apiweb.inmovilla.com/apiweb/config/12449_...`, código de cliente 12449). Portada y listado (`venta.php`, canonical `/venta/es`) comparten `<title>` (cortado con "..." en el código) y description (lista de servicios).
- Las fichas vivas tienen URL legible (`/ficha/bungalow/palafolls/sant-genis-de-palafolls/12449/30025147/es/`), canonical propio y title propio, **pero el title es el titular comercial del agente** ("VIVE DE VACACIONES TODO EL AÑO: PARCELA con DOS módulos..."), en mayúsculas, cortado a ~60 caracteres, sin "en venta", precio ni marca. Description = primeras líneas del texto del anuncio. H1 de la ficha: "Encuentra la casa de tus sueños" y "Suscríbete", no el inmueble.
- Las URLs antiguas de ficha (`/ficha/index.php?codigo=12449_23982185`, las que Google conoce) devuelven la portada con 200 (soft 404) en vez de redirigir a la URL nueva o dar "no disponible".
- Portada de serra-s.es: 15 H1, 7 de 16 imágenes sin alt.
- Resultado: 85 inmuebles en idealista y 111 en habitaclia; en nuestras búsquedas Google solo muestra una ficha, y retirada.

**Solución:** título automático estructurado por ficha ({Tipo} en venta en {Municipio}, {Zona} · {m²} m² · {Precio} € | SERRA-S) delante del titular comercial; inmueble como H1; listado con title/description propios; 301 de las URLs antiguas; `RealEstateListing`/`Offer`; páginas de comprar/vender/alquilar en la web corporativa enlazando a las fichas. Las plantillas las gestiona Inmovilla (se piden a través de ellos); alternativa: conector Inmovilla → WordPress para tener todo bajo www.serra-s.com.

### 3. ALTO · Las fichas antiguas de serra-s.com dan 404

Google todavía muestra `/es/compra/terrenos/barcelona/premia-de-dalt/528` (terreno en Premià de Dalt, ref. PD270720T, 660.000 €). Hoy responde "Page not found" con `noindex`. También indexa `serra-s.com/es` con título "SERRA-S" y snippet "Tu portal inmobiliario de confianza": es el fantasma del buscador anterior, que vivía en serra-s.com/es y ahora está en serra-s.es. Se cambió de plataforma sin redirigir.

**Solución:** 301 de todas las URLs antiguas del buscador (`/es/compra/...`, `/es/content/...`; `serra-s.com/es/content/certif-energetico` también redirige a www y muere) a su equivalente o a la página de compra. Retirada en Search Console.

### 4. MEDIO · Google recibe páginas que no debería ver

`page-sitemap.xml` incluye páginas de plantilla del tema Enfold que no son para el público: `/qality/`, `/es/qality-esp/`, `/excellence/`, `/es/excellence-2/`, `/es/footer-esp/`. `category-sitemap.xml` incluye los 19 archivos de categoría (CA + ES). Google además tiene indexado `/es/category/sense-categoria-es/` ("Sense categoria Archives"). Solución: `noindex` en páginas de plantilla y archivos de categoría, etiqueta, autor y adjuntos, y fuera del sitemap (Yoast).

### 5. MEDIO · Señalización de idiomas incompleta

hreflang existe (WPML): la portada CA declara `ca`, `es` y `en`; la portada ES solo `ca` y `es`; contacto `ca` y `es`. **`/en/` responde 200 pero está vacía** (H1 "Nothing Found", title = tagline del sitio) y es indexable (`index, follow`); no está en el sitemap y Google no la indexa. Páginas en catalán con coletilla en castellano; la portada de noticias en catalán tiene slug castellano (`/noticias/`), y hay posts con slug cruzado (`/es/quotes-hipotecaries-...-es-translation/`, `/cuotas-hipotecarias-mas-bajas-que-los-alquileres/` en CA).

**Solución:** hreflang coherente, coletilla por idioma, y con el inglés una de dos: versión EN real (portada, comprar, contacto) en el sitemap, o `noindex` en `/en/` y quitarla del hreflang.

### 6. MEDIO · La marca está escrita de tres maneras

"SERRA-S **inmobiliàries**" (títulos de la web y de serra-s.es), "SERRA-S **immobiliàries**" (idealista, logo), "SERRA-S **Gestions Immobiliàries**" (habitaclia, firma de correo). Elegir una y usarla en web, portales, Google Business, Facebook y firma.

### 7. MEDIO · Portada en castellano con URL larga y tres saltos

`serra-s.com/es` → 301 → `www.serra-s.com/es` → 301 → `/es/inicio/` → 301 → `/es/serra-s-inmobiliaries-compraventa-de-inmuebles/` (la que Google indexa como "Inicio"). Solución: portada ES en `/es/` y un solo salto desde las demás.

### 8. MEDIO · Datos de contacto inconsistentes fuera de la web

Portales: "Carretera N-II km 673, Centro Comercial Carrefour" y "N-2, 11, 08398 Santa Susanna". Unificar NAP en web, Google Business, idealista, habitaclia y Facebook. Horario: L-S 10:00-13:30 y 17:00-20:30 · domingos y festivos 10:00-13:00. Teléfonos: 93 102 84 44 y 675 142 221. Email: info@serra-s.com.

### 9. MEDIO · Mucho blog, nada local

45 posts en CA y ES (90 URLs), todos noticias genéricas del sector (euríbor, IBI, decoración, ascensores...), probablemente contenido sindicado. Solo uno habla del Maresme; ninguno menciona Santa Susanna, Malgrat, Pineda, Calella ni Canet. Solución: 5 páginas de zona + 1 artículo local al mes.

---

## Lo que ya está bien (comprobado)

- Redirecciones http → https y sin www → www: 301 correctas.
- `robots.txt` (Yoast, sin bloqueos) y `sitemap_index.xml` correctos.
- Canonical en cada página.
- Todas las imágenes de la web corporativa con alt (18/18 portada CA, 15/15 portada ES, 11/11 contacto).
- Un solo H1 por página en WordPress.
- `lang="ca"` / `lang="es-ES"` declarado.
- W3 Total Cache con Redis activo.
- JSON-LD presente (el genérico de Yoast; falta `RealEstateAgent`).
- Blog activo: 45 artículos en dos idiomas.

## Comprobaciones técnicas que entran en la Fase 1

- Velocidad y Core Web Vitals (PageSpeed móvil y escritorio) ⚠️ pendiente
- Datos estructurados `RealEstateAgent`
- Google Business Profile ⚠️ pendiente
- Search Console configurado y sitemap enviado
- Alt en fotos de serra-s.es
- Versión móvil y botones de llamada / WhatsApp

---

## Plan de acción y precios cerrados

| Fase | Qué incluye | Plazo | Precio cerrado |
|---|---|---|---|
| **Fase 1 · Base** | Títulos y descripciones de todas las páginas en CA/ES (Yoast), 301 de las URLs antiguas del buscador, noindex de páginas plantilla y archivos + fuera del sitemap, hreflang coherente y `/en/` visible, portada ES en `/es/` con un salto, marca unificada, Google Business Profile, Search Console, `RealEstateAgent`, propuesta cerrada para inmuebles (plantilla Inmovilla vs conector) | 1 semana | **450 €** |
| **Fase 2 · Inmuebles y zona** | Título, descripción y datos estructurados automáticos en todas las fichas, URLs legibles, página de "vendido", páginas de comprar/vender/alquilar en la web corporativa, 5 páginas de zona (Santa Susanna, Malgrat, Pineda, Calella, Canet), versión EN mínima, mejora de velocidad | 2 semanas | **890 €** |
| Fase 1 + 2 juntas | Todo lo anterior | 3 semanas | **1.190 €** |

Si para los inmuebles se opta por el conector Inmovilla → WordPress, la licencia del conector se paga aparte al proveedor, a su precio, sin recargo. Sin cuotas mensuales.

---

## Qué esperar

- Semanas 1-2: Google reindexa títulos nuevos. Empezáis a aparecer por "inmobiliaria Santa Susanna" y variantes.
- Mes 1-2: las fichas empiezan a recibir visitas directas desde Google sin pasar por idealista.
- Mes 3: con las páginas de zona, presencia en los 5 municipios del Alt Maresme donde tenéis cartera.

---

## Fuentes consultadas

- Comprobación directa el 7 sep 2026 con `auditorias/comprobar-serra-s.sh` (salida en el Escritorio de Nacho, `serra-s-check.txt`)
- [Portada indexada de serra-s.com](https://www.serra-s.com/)
- [Ficha fantasma de Premià de Dalt (404)](https://www.serra-s.com/es/compra/terrenos/barcelona/premia-de-dalt/528)
- [Portada ES "Inicio"](https://www.serra-s.com/es/serra-s-inmobiliaries-compraventa-de-inmuebles/)
- [Archivo "Sense categoria"](https://www.serra-s.com/es/category/sense-categoria-es/)
- [Noticias](https://www.serra-s.com/es/noticias/) · [Contacte](https://www.serra-s.com/contacte/)
- [Plataforma de fichas serra-s.es](https://www.serra-s.es/) · [ficha Canet](https://www.serra-s.es/ficha/index.php?codigo=12449_23982185)
- [SERRA-S en idealista (85 inmuebles)](https://www.idealista.com/pro/serra-s-immobiliaries/)
- [SERRA-S en habitaclia](https://english.habitaclia.com/real_estate-serra_s_gestions_immobiliaries_50274_1/)
- [Agencias en Santa Susanna, idealista](https://www.idealista.com/en/agencias-inmobiliarias/santa-susanna-barcelona/inmobiliarias)
- [VirtuaHome venta](https://www.inmuebles.virtuahome.es/venta.php) · [VirtuaHome portada](https://www.virtuahome.es/?idio=8)

---
---

# NOTAS INTERNAS (no enviar al cliente)

## Estado de verificación (7 sep 2026)

Tres pasadas: (1) búsquedas en Google desde el entorno remoto, (2) workflow de 12 verificadores + escépticos (9 escépticos, 5 de descubrimiento y el crítico cayeron por límite de uso), (3) script `comprobar-serra-s.sh` ejecutado desde el Mac de Nacho contra la web real.

| Afirmación original | Estado final | Qué se hizo |
|---|---|---|
| `<title>` de la portada = "Inici" | **Confirmado** (HTML real) | Google lo reescribe a veces como "SERRA-S inmobiliàries". |
| Sin meta description | **Confirmado** en portada CA, portada ES y contacto | Yoast instalado (5 referencias) sin rellenar. |
| Sin www indexado como sitio aparte | **Refutado** | `serra-s.com` → 301 → `www`. Lo indexado en `serra-s.com/es` es un fantasma del buscador anterior. Hallazgo eliminado. |
| Buscador de inmuebles en `serra-s.com/es` | **Refutado / cambiado** | Ya no existe: `/es/compra/.../528` da 404 con noindex. El buscador vive en serra-s.es. Nuevo hallazgo 3 (404s sin redirigir). |
| serra-s.es = web antigua abandonada | **Refutado** | Es la plataforma de fichas activa (assets 2026-07-29). No llamarla "antigua" delante del cliente. |
| Dos portadas en español duplicadas | **Refutado** | `/es/` → `/es/inicio/` → canonical al slug largo. Es cadena de redirecciones, no duplicado. Hallazgo 7. |
| Fichas invisibles (1 indexada) | **Confirmado y agravado** | La web corporativa no tiene fichas; en serra-s.es solo 1 indexada. |
| hreflang ⚠️ | **Comprobado**: existe pero inconsistente | CA declara `en` → `/en/`; ES no. `/en/` sin indexar ⚠️. |
| Versión inglesa | `/en/` responde 200 pero está vacía ("Nothing Found"), indexable | Hallazgo 5. |
| Todas las fichas de serra-s.es canonicalizan a la portada | **Refutado para fichas vivas** (3ª pasada) | Las fichas activas tienen URL amigable, title y canonical propios. Lo compartido es portada + listado + URLs antiguas. Hallazgo 2 reescrito: el problema es el title (titular comercial) y el H1. |
| WordPress + WPML + Yoast | **Confirmado** | Tema Enfold, W3 Total Cache + Redis. |
| Alt en imágenes | **Refutado para WP** (0 sin alt); **confirmado para serra-s.es** (7/16) | Movido a "lo que ya está bien" / comprobaciones. |
| Marca en tres grafías | Confirmado | |
| Sense categoria indexado | Confirmado + está en `category-sitemap.xml` | |
| 85 / 111 / 47 | Confirmado en títulos de Google (7 sep) | |
| Título VirtuaHome | Corregido: es de `inmuebles.virtuahome.es/venta.php`; portada "INICIO - VIRTUA HOME" | |
| NAP doble | Visto en snippets; comprobar en Maps ⚠️ | |

## Segunda pasada desde el Mac (hecha, 15:22)

- `/en/` → 200. `/es/inicio/` → 301 al slug largo (tres saltos en total). `/es/compra/.../528` → 404. `serra-s.es/es`, `/ca`, `/en` → 200.
- `page-sitemap.xml`: 15 URLs (home, qality ×2, excellence ×2, footer-esp, contacte/contacto, empresa ×2, home ES, noticias ×2, serveis/servicios). `post-sitemap.xml`: 90 URLs (45 posts × 2 idiomas). `category-sitemap.xml`: 19 archivos.
- serra-s.es en castellano: mismo title/description; canonical `/es`. Ficha de Canet: devuelve la portada (soft 404).
- Enlaces de www.serra-s.com hacia serra-s.es: `venta.php` y `alertas.php?idio=1`.
- Proveedor: **Inmovilla** (`apiweb.inmovilla.com/apiweb/config/12449_...`, CSS `inmovilla-1.css`, texto "inmovilla diseño web"). Facebook: `facebook.com/.../61570973482792/`.

## Pendiente

1. **PageSpeed** móvil y escritorio de `https://www.serra-s.com/` en pagespeed.web.dev. Enfold + jquery-migrate + html5shiv: espera 40-60 en móvil. Si baja de 50, subir velocidad a hallazgo ALTO.
2. **Google Maps**: nota, nº de reseñas y dirección de "SERRA-S immobiliàries" y de "Virtua Home Santa Susanna". Añadir al hallazgo 8.
3. ~~Tercer script~~: hecho (15:28). Fichas vivas con URL/title/canonical propios; `/en/` vacía.
4. **Recuento real de fichas indexadas**: en tu Google, `site:serra-s.es` y `site:serra-s.es/ficha`. Anota el número. Si son más de 5, cambia "solo muestra una ficha, y retirada" por el número real. El argumento se mantiene mientras sea una fracción pequeña de los 100+.
5. Opcional: `curl -s https://www.serra-s.es/robots.txt` y `curl -s https://www.serra-s.es/sitemap.xml | head -30` para saber si Inmovilla publica sitemap de fichas.

## Riesgos y decisiones

- **Plataforma = Inmovilla, plantilla antigua.** Dos vías para la Fase 2: (a) el cliente pide a Inmovilla el cambio a plantilla actual (Inmovilla lo hace; el SEO por inmueble y las URLs amigables van en sus plantillas nuevas; tú configuras textos y estructura); (b) conector Inmovilla → WordPress (hay plugins de terceros tipo plugininmovilla.com / propertify.es, con licencia anual). **Antes de cerrar la Fase 2, pide precio de la licencia del conector y confirma con el cliente qué contrato tienen con Inmovilla.** La vía (b) es la buena a largo plazo: todo bajo www.serra-s.com. Estimación extra si (b): 8-12 h de integración y plantillas.
- **Plantillas de Inmovilla:** el title de ficha lo compone Inmovilla a partir del titular del anuncio. Cambiar a un patrón estructurado se pide a Inmovilla (soporte/diseño web); confirma con el cliente si tienen ese servicio contratado y cuánto tarda. Si Inmovilla no lo permite, la vía del conector a WordPress es la única que da control total. Mientras tanto, una mejora inmediata sin tocar plantillas: que el agente escriba los titulares en formato "Piso en venta en Santa Susanna, 3 hab, terraza, 189.000 €" en vez de "VIVE DE VACACIONES TODO EL AÑO". Eso lo puedes vender como formación de 1 hora dentro de la Fase 2.
- **Fase 1 es ahora más sólida y más barata de ejecutar** que en la primera versión: todo es Yoast + WPML + redirecciones en `.htaccess`. 6-8 h. Margen bueno a 450 €.
- **Las URLs fantasma de `/es/compra/...`** pueden ser cientos (todo el catálogo anterior). Pide en Search Console el listado de 404 antes de hacer las redirecciones; con una regla genérica `/es/compra/* → serra-s.es/compra` se resuelve en una línea.

## Mensaje para enviar el informe (WhatsApp o email)

> Hola, buenos días. Os paso la auditoría de serra-s.com como quedamos: [enlace].
>
> Resumen rápido: la web corporativa está bien montada por dentro, pero Google no sabe que sois una inmobiliaria de Santa Susanna: la portada se titula "Inici", no hay descripciones en ninguna página y el plugin de SEO está instalado sin configurar. Y lo más importante: los inmuebles no están en la web, viven en serra-s.es con direcciones ilegibles, y de más de 100 inmuebles Google solo tiene uno indexado. Nada de esto obliga a rehacer la web.
>
> En el informe tenéis qué arreglar primero y el precio cerrado si queréis que lo hagamos nosotros (Fase 1 en una semana, 450 €). Si lo preferís hacer con vuestro proveedor, el documento sirve como lista de tareas.
>
> Para la segunda fase hay dos caminos con vuestra web de Inmovilla (actualizar su plantilla o traer los inmuebles a serra-s.com); os lo explico en una llamada de 15 minutos cuando os vaya bien. Un saludo, Nacho · Sultox · 722 83 50 57
