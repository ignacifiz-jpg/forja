# Auditoría SEO rápida · SERRA-S Immobiliàries (serra-s.com)

**Fecha:** 7 de septiembre de 2026 · **Preparado por:** Sultox · **Para:** Serra-S Immobiliàries, Santa Susanna

> Método: comprobación directa de la web (títulos, descripciones, redirecciones, hreflang, robots, sitemap, plataforma) el 7 de septiembre de 2026, análisis de lo que Google tiene indexado de serra-s.com y serra-s.es, presencia en portales (idealista, habitaclia) y comparación con la competencia local.

---

## Resumen en 3 líneas

1. La web corporativa está bien montada por dentro (WordPress, redirecciones, sitemap, caché), pero **Google no sabe qué es ni dónde está**: la portada se titula "Inici", ninguna página tiene descripción y Yoast SEO está instalado sin configurar.
2. **Los inmuebles no están en la web.** Viven en otro dominio, serra-s.es, con URLs ilegibles y peor SEO. De más de 100 inmuebles, Google tiene uno indexado. Las fichas antiguas de serra-s.com dan 404.
3. Lo primero se arregla en **una semana sin tocar el diseño**. Lo segundo depende de la plataforma de fichas; se confirma en esa misma semana.

---

## Hallazgos por prioridad

### 1. CRÍTICO · Los títulos no dicen a qué os dedicáis ni dónde, y no hay descripciones

| Página | `<title>` real | Meta description |
|---|---|---|
| `www.serra-s.com/` | Inici | Ninguna |
| `/es/serra-s-inmobiliaries-compraventa-de-inmuebles/` | Inicio | Ninguna |
| `/contacte/` | Contacte - SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquiler | Ninguna |
| `/es/noticias/` | Noticias - SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquiler | Google lo corta |
| `www.serra-s.es/` | SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquil... | "servicio de Broker hipotecario, Renta vitalicia, Certificados Energéticos, Cédulas de habitabilidad, seguros de impago y seguros de hogar" |

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

- `www.serra-s.com` (WordPress, tema Enfold, WPML, Yoast, W3 Total Cache) **no tiene ninguna ficha de inmueble**: el sitemap solo tiene `post-sitemap`, `page-sitemap` y `category-sitemap`.
- Los inmuebles están en `www.serra-s.es`, la plataforma de fichas (activa: assets con fecha 2026-07-29). URLs tipo `/ficha/index.php?codigo=12449_23982185`. Su portada, servida sin idioma, sale en inglés con `canonical` a `/en`, descripción = lista de servicios, 6 H1 y 7 de 16 imágenes sin alt.
- Resultado: 85 inmuebles en idealista y 111 en habitaclia; Google tiene **una** ficha indexada (casa en Canet de Mar, `codigo=12449_23982185`).

**Solución:** título, descripción y datos estructurados (`RealEstateListing` / `Offer`) automáticos por ficha; URLs legibles; enlazar las fichas desde la web corporativa. Se hace sobre la plataforma actual; si su proveedor no permite tocar plantillas, avisar tras la Fase 1 y proponer alternativa con precio cerrado.

### 3. ALTO · Las fichas antiguas de serra-s.com dan 404

Google todavía muestra `/es/compra/terrenos/barcelona/premia-de-dalt/528` (terreno en Premià de Dalt, ref. PD270720T, 660.000 €). Hoy responde "Page not found" con `noindex`. También indexa `serra-s.com/es` con título "SERRA-S" y snippet "Tu portal inmobiliario de confianza": es el fantasma del buscador anterior, que vivía en serra-s.com/es y ahora está en serra-s.es. Se cambió de plataforma sin redirigir.

**Solución:** 301 de todas las URLs antiguas del buscador (`/es/compra/...`, `/es/content/...`) a su equivalente en serra-s.es o a la página de compra. Retirada en Search Console.

### 4. MEDIO · Señalización de idiomas incompleta

hreflang existe (WPML): la portada CA declara `ca`, `es` y `en` (`/en/`); la portada ES declara solo `ca` y `es`; contacto declara `ca` y `es` (`/es/contacto/`). No hay ninguna URL `/en/` indexada en Google ⚠️ (comprobar si `/en/` existe). Las páginas en catalán llevan la coletilla del título en castellano.

**Solución:** hreflang coherente en todas las páginas, coletilla por idioma, y versión EN real mínima (portada, comprar, contacto) si quieren comprador extranjero.

### 5. MEDIO · La marca está escrita de tres maneras

"SERRA-S **inmobiliàries**" (títulos de la web y de serra-s.es), "SERRA-S **immobiliàries**" (idealista, logo), "SERRA-S **Gestions Immobiliàries**" (habitaclia, firma de correo). Elegir una y usarla en web, portales, Google Business y redes.

### 6. MEDIO · Páginas basura indexadas

`/es/category/sense-categoria-es/` ("Sense categoria Archives") está indexada y además el `category-sitemap.xml` se la ofrece a Google. Solución: `noindex` en archivos de categoría, etiqueta, autor y adjuntos, y desactivar el sitemap de categorías en Yoast.

### 7. MEDIO · Portada en castellano con URL larga y dos saltos

`serra-s.com/es` → 301 → `www.serra-s.com/es` → 301 → `/es/inicio/` → canonical a `/es/serra-s-inmobiliaries-compraventa-de-inmuebles/` (la que Google indexa como "Inicio"). Funciona, pero son tres URLs para una página. Solución: portada ES en `/es/` y 301 desde las otras dos.

### 8. MEDIO · Datos de contacto inconsistentes fuera de la web

Portales: "Carretera N-II km 673, Centro Comercial Carrefour" y "N-2, 11, 08398 Santa Susanna". Unificar NAP en web, Google Business, idealista, habitaclia y Facebook. Horario: L-S 10:00-13:30 y 17:00-20:30 · domingos y festivos 10:00-13:00. Teléfonos: 93 102 84 44 y 675 142 221. Email: info@serra-s.com.

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
| **Fase 1 · Base** | Títulos y descripciones de todas las páginas en CA/ES (Yoast), 301 de las URLs antiguas del buscador, hreflang coherente, noindex de archivos + sitemap de categorías fuera, portada ES en `/es/`, marca unificada, Google Business Profile, Search Console, `RealEstateAgent`, diagnóstico de la plataforma de fichas | 1 semana | **450 €** |
| **Fase 2 · Inmuebles y zona** | Título, descripción y datos estructurados automáticos en todas las fichas de serra-s.es, URLs legibles si la plataforma lo permite, fichas enlazadas desde la web corporativa, versión EN mínima, 5 páginas de zona (Santa Susanna, Malgrat, Pineda, Calella, Canet), mejora de velocidad | 2 semanas | **890 €** |
| Fase 1 + 2 juntas | Todo lo anterior | 3 semanas | **1.190 €** |

La Fase 2 se hace sobre la plataforma de fichas actual. Si su proveedor no permite modificar plantillas, se avisa al acabar la Fase 1 y se propone alternativa con precio cerrado antes de empezar. Sin cuotas mensuales.

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
| Versión inglesa | Sin páginas indexadas; `/en/` declarado en hreflang | Pendiente: `curl` a `/en/` (ver abajo). |
| WordPress + WPML + Yoast | **Confirmado** | Tema Enfold, W3 Total Cache + Redis. |
| Alt en imágenes | **Refutado para WP** (0 sin alt); **confirmado para serra-s.es** (7/16) | Movido a "lo que ya está bien" / comprobaciones. |
| Marca en tres grafías | Confirmado | |
| Sense categoria indexado | Confirmado + está en `category-sitemap.xml` | |
| 85 / 111 / 47 | Confirmado en títulos de Google (7 sep) | |
| Título VirtuaHome | Corregido: es de `inmuebles.virtuahome.es/venta.php`; portada "INICIO - VIRTUA HOME" | |
| NAP doble | Visto en snippets; comprobar en Maps ⚠️ | |

## Pendiente (5 minutos desde el Mac)

1. **PageSpeed** móvil y escritorio de `https://www.serra-s.com/` en pagespeed.web.dev. Enfold + jquery-migrate + html5shiv: espera 40-60 en móvil. Si baja de 50, subir velocidad a hallazgo ALTO.
2. **Google Maps**: nota, nº de reseñas y dirección de "SERRA-S immobiliàries" y de "Virtua Home Santa Susanna". Añadir al hallazgo 8.
3. **Segundo script** (bloque `serra-s-check2`): estado de `/en/`, lista completa de páginas y posts del sitemap, serra-s.es en castellano, enlaces de la web corporativa hacia serra-s.es, y pistas del proveedor de la plataforma de fichas.

## Riesgos y decisiones

- **Plataforma de fichas desconocida.** Scripts de serra-s.es: `buscadorareas/componentes-v3-externo.js`, `js/EnviarPostHog.js`, `js/modulos/...` con cache-busting `?x=20260729111100`. No es Inmovilla ni Witei a simple vista; parece desarrollo a medida de un proveedor local. Pregunta al cliente quién les lleva serra-s.es antes de comprometer la Fase 2. Por eso el informe dice "si su proveedor no permite modificar plantillas, os proponemos alternativa con precio cerrado".
- **Alternativa si la plataforma es cerrada:** traer las fichas a WordPress con un plugin inmobiliario (conector XML/feed del CRM) y dejar serra-s.es como espejo con canonical a la web. Estimar aparte: 8-12 h extra.
- **Fase 1 es ahora más sólida y más barata de ejecutar** que en la primera versión: todo es Yoast + WPML + redirecciones en `.htaccess`. 6-8 h. Margen bueno a 450 €.
- **Las URLs fantasma de `/es/compra/...`** pueden ser cientos (todo el catálogo anterior). Pide en Search Console el listado de 404 antes de hacer las redirecciones; con una regla genérica `/es/compra/* → serra-s.es/compra` se resuelve en una línea.

## Mensaje para enviar el informe (WhatsApp o email)

> Hola, buenos días. Os paso la auditoría de serra-s.com como quedamos: [enlace].
>
> Resumen rápido: la web corporativa está bien montada por dentro, pero Google no sabe que sois una inmobiliaria de Santa Susanna: la portada se titula "Inici", no hay descripciones en ninguna página y el plugin de SEO está instalado sin configurar. Y lo más importante: los inmuebles no están en la web, viven en serra-s.es con direcciones ilegibles, y de más de 100 inmuebles Google solo tiene uno indexado. Nada de esto obliga a rehacer la web.
>
> En el informe tenéis qué arreglar primero y el precio cerrado si queréis que lo hagamos nosotros (Fase 1 en una semana, 450 €). Si lo preferís hacer con vuestro proveedor, el documento sirve como lista de tareas.
>
> Una pregunta para afinar la segunda fase: ¿quién os lleva la plataforma de fichas de serra-s.es? Si os cuadra, lo vemos en una llamada de 15 minutos cuando os vaya bien. Un saludo, Nacho · Sultox · 722 83 50 57
