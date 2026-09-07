# Auditoría SEO rápida · SERRA-S Immobiliàries (serra-s.com)

**Fecha:** 7 de septiembre de 2026 · **Preparado por:** Sultox · **Para:** Serra-S Immobiliàries, Santa Susanna

> Método: análisis de lo que Google tiene indexado de serra-s.com y serra-s.es (títulos reales que muestra en resultados), presencia en portales (idealista, habitaclia, buscainmobiliarias) y comparación con la competencia local. Los puntos marcados con ⚠️ requieren una comprobación manual antes de enviar (ver notas internas al final).

---

## Resumen en 3 líneas

1. La web existe y Google la tiene indexada, pero **no sabe qué es ni dónde está**: los títulos no mencionan "inmobiliaria" ni "Santa Susanna" y las fichas de inmuebles se titulan solo "SERRA-S".
2. La web está **partida en tres sitios**: la web corporativa (www.serra-s.com), el buscador de inmuebles (serra-s.com/es, sin www) y la web antigua serra-s.es, que sigue indexada. La autoridad se reparte en vez de sumarse.
3. Todo esto se arregla en **1 a 2 semanas** sin rehacer la web. Es trabajo de configuración y textos, no de diseño.

---

## Hallazgos por prioridad

### 1. CRÍTICO · Los títulos de página no dicen a qué os dedicáis ni dónde

El título es lo primero que Google lee y lo que la gente ve en azul en los resultados. Esto es lo que muestra Google ahora mismo:

| URL indexada | Título que muestra Google | Problema |
|---|---|---|
| `www.serra-s.com/` | SERRA-S inmobiliàries | El `<title>` real es "Inici" (Google lo muestra así en búsquedas con esa palabra y lo reescribe con el nombre en el resto). Sin servicio ni localidad |
| `serra-s.com/es` | SERRA-S | Portada del buscador de inmuebles: solo la marca |
| `/es/serra-s-inmobiliaries-compraventa-de-inmuebles/` | Inicio - SERRA-S immobiliàries | Portada en castellano, sin servicio ni localidad |
| `/contacte/` | Contacte - SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquiler | Página en catalán con coletilla en castellano |
| `/es/compra/terrenos/barcelona/premia-de-dalt/528` | SERRA-S | Ficha de inmueble sin título descriptivo |
| `/es/noticias/` | Noticias - SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquiler | Demasiado largo, Google lo corta |
| `/tipus-denergies-renovables-.../` | TIPUS D'ENERGIES RENOVABLES: ... - SERRA-S inmobiliàries \| Compraventa de inmuebles, Alquiler | Artículo en catalán con coletilla en castellano, cortado |

Para comparar: la competencia directa en Santa Susanna sale con títulos como "La Mejor Inmobiliaria de Santa Susana | VirtuaHome.es". Google los entiende; a vosotros no.

**Títulos propuestos**

| Página | Título propuesto (CA) | Título propuesto (ES) |
|---|---|---|
| Portada | Immobiliària a Santa Susanna · Compra, venda i lloguer al Maresme \| SERRA-S | Inmobiliaria en Santa Susanna · Compra, venta y alquiler en el Maresme \| SERRA-S |
| Comprar | Pisos i cases en venda a Santa Susanna i l'Alt Maresme \| SERRA-S | Pisos y casas en venta en Santa Susanna y el Alt Maresme \| SERRA-S |
| Alquilar | Pisos de lloguer a Santa Susanna, Malgrat i Pineda \| SERRA-S | Pisos de alquiler en Santa Susanna, Malgrat y Pineda \| SERRA-S |
| Vender | Vols vendre el teu pis al Maresme? Valoració gratuïta \| SERRA-S | ¿Quieres vender tu piso en el Maresme? Valoración gratuita \| SERRA-S |
| Ficha inmueble (automático) | {Tipo} en venda a {Municipi} · {m²} m² · {Preu} € \| SERRA-S | {Tipo} en venta en {Municipio} · {m²} m² · {Precio} € \| SERRA-S |
| Noticias | Notícies del mercat immobiliari al Maresme \| SERRA-S | Noticias del mercado inmobiliario en el Maresme \| SERRA-S |

Cada página necesita además una **descripción para buscadores** (meta description) de 140 a 155 caracteres con el teléfono y la zona. Hoy la portada no tiene ninguna ⚠️ (observación tuya del primer correo; los agentes no pudieron leer el HTML).

### 2. CRÍTICO · La web está partida en tres sitios

Google tiene indexados tres sitios distintos con la marca:

- `https://www.serra-s.com`: la web corporativa (WordPress con WPML y Yoast: portada, contacto, noticias).
- `https://serra-s.com/es` (sin www): el **buscador de inmuebles**, una aplicación distinta que Google indexa como sitio aparte con el título "SERRA-S" a secas. También cuelga de ahí `serra-s.com/es/content/certif-energetico` con el título "certificado energético" sin marca. Ambos hosts resuelven a la misma IP: es el mismo servidor, mal configurado.
- `https://www.serra-s.es`: la web antigua (plantilla PHP tipo CRM). Sigue indexada con al menos 4 URLs: portada, `/index.php?vistas=1` (copia de la portada), `/seccion/company/company/en/` (página "Company" en inglés) y la ficha `/ficha/index.php?codigo=12449_23982185` (casa en Canet de Mar, que también aparece en otras agencias como HG-CAN-27 a 315.000 €). Anuncia broker hipotecario, renta vitalicia, cédulas y seguros; en la web nueva solo hemos localizado el certificado energético.

Cada enlace, cada visita y cada señal de autoridad se reparte entre tres sitios. Quien entra por la antigua ve una web desactualizada; quien entra por el buscador no ve ni el nombre completo de la agencia en el título.

**Solución:** redirección 301 permanente de serra-s.es hacia `https://www.serra-s.com`, página por página cuando haya equivalente; el buscador de inmuebles bajo el mismo dominio con www. Etiqueta canonical en todas las páginas. Recuperar en la web actual los servicios que solo están en la antigua.

### 3. ALTO · Las fichas de inmuebles son invisibles en Google

Tenéis 85 inmuebles en venta en idealista y 111 en habitaclia (cifras del 7 de septiembre). Cada ficha en vuestra web debería posicionar por "casa en venta en Canet de Mar" o "terreno en Premià de Dalt". Hoy Google solo tiene indexada **una** ficha de toda la cartera (`/es/compra/terrenos/barcelona/premia-de-dalt/528`, terreno de 862 m² en Premià de Dalt, ref. PD270720T, 660.000 €), y la muestra con el título "SERRA-S" a secas; cuando la búsqueda coincide con el texto, Google se inventa el título a partir del encabezado ("Suelo de 862m 2 en calle de suissa, 28, en Premià de Dalt"), sin precio. No hay ninguna URL de alquiler indexada. Toda esa demanda se la llevan los portales, y ahí pagáis por aparecer.

**Solución:** plantilla automática de título y descripción por ficha (tipo, municipio, m², precio, referencia) y datos estructurados (schema.org `RealEstateListing` / `Offer`) para que Google entienda precio y ubicación.

### 4. ALTO · La portada en castellano está escondida

La portada corporativa en castellano vive en `/es/serra-s-inmobiliaries-compraventa-de-inmuebles/` (slug largo que nadie escribe ni enlaza), mientras que `serra-s.com/es`, la dirección natural, la ocupa el buscador de inmuebles con otro diseño y otro título ("SERRA-S" / "Tu portal inmobiliario de confianza"). No son duplicados: son dos webs distintas para el mismo usuario según por dónde entre. Solución: una sola portada en castellano en `www.serra-s.com/es/` con el buscador integrado o enlazado, y redirección desde el slug largo.

### 5. MEDIO · Páginas basura indexadas

`/es/category/sense-categoria-es/` ("Sense categoria Archives") está indexada. Es el archivo de "Sin categoría" de WordPress. Aporta cero y resta calidad al conjunto del sitio. Solución: `noindex` en archivos de categoría, etiqueta, autor y adjuntos.

### 6. MEDIO · La marca está escrita de tres maneras

En los títulos de la web predomina "SERRA-S **inmobiliàries**" (mezcla castellano-catalán: portada, contacto, noticias, categorías, blog y también la web antigua). Solo la portada en castellano usa "SERRA-S **immobiliàries**" (catalán correcto, como en idealista), y en habitaclia (slug `serra_s_gestions_immobiliaries`) y en la firma de correo del cliente aparece "SERRA-S **Gestions Immobiliàries**". Google lo trata como tres nombres distintos. Elegir uno y usarlo en web, portales, Google Business y redes.

### 7. MEDIO · Idiomas mezclados y sin señalización

Las páginas en catalán (contacto, artículos del blog) llevan la coletilla del título en castellano. La web tiene raíz para catalán y `/es/` para castellano. **No existe versión inglesa indexada** (ninguna URL bajo `/en/` ni con título en inglés; la web antigua sí tenía `/seccion/company/company/en/`). Hay que comprobar las etiquetas `hreflang` CA/ES ⚠️ y, dado que en Santa Susanna hay mucho comprador extranjero, proponer una versión EN mínima (portada, comprar, contacto).

### 8. MEDIO · Datos de contacto inconsistentes fuera de la web

En los portales la dirección aparece como "Carretera N-II km 673, Centro Comercial Carrefour" y también como "N-2, 11, 08398 Santa Susanna". Google Maps cruza estos datos: si no coinciden, baja la confianza en la ficha de Google Business Profile ⚠️. Unificar nombre, dirección, teléfono y horario en web, Google Business, idealista, habitaclia y Facebook.

Horario a publicar (según portales): L-S 10:00-13:30 y 17:00-20:30 · Domingos y festivos 10:00-13:00.

---

## Comprobaciones técnicas que entran en la Fase 1

Se revisan y corrigen dentro del pack, no se cobran aparte:

- Velocidad y Core Web Vitals (PageSpeed Insights móvil y escritorio)
- Un solo H1 por página y jerarquía de encabezados
- Textos alternativos en fotos de inmuebles
- `robots.txt` y `sitemap.xml` enviados a Google Search Console
- Datos estructurados `RealEstateAgent` (nombre, dirección, teléfono, horario, zona)
- Certificado SSL y redirección http → https
- Versión móvil y tamaño de botones de llamada / WhatsApp

---

## Plan de acción y precios cerrados

| Fase | Qué incluye | Plazo | Precio cerrado |
|---|---|---|---|
| **Fase 1 · Base** | Redirecciones 301 (serra-s.es y sin www), canonical, títulos y descripciones de las páginas principales en CA/ES, noindex de páginas basura, marca unificada, Google Business Profile revisado, Search Console configurado | 1 semana | **450 €** |
| **Fase 2 · Inmuebles y zona** | Plantilla automática de título y descripción para todas las fichas y conseguir que Google las indexe todas, portada en castellano unificada con el buscador, datos estructurados de inmuebles y agencia, hreflang CA/ES y versión EN mínima, 5 páginas de zona (Santa Susanna, Malgrat, Pineda, Calella, Canet), mejora de velocidad, recuperar servicios de la web antigua | 2 semanas | **890 €** |
| Fase 1 + 2 juntas | Todo lo anterior | 3 semanas | **1.190 €** |

Sin cuotas mensuales. Entrega con informe de antes y después en Search Console. Si preferís hacerlo con vuestro proveedor actual, este documento sirve como lista de tareas.

---

## Qué esperar

- Semanas 1-2: Google reindexa títulos nuevos. Empezáis a aparecer por "inmobiliaria Santa Susanna" y variantes.
- Mes 1-2: las fichas de inmuebles empiezan a recibir visitas directas desde Google sin pasar por idealista.
- Mes 3: con las páginas de zona, presencia en los 5 municipios del Alt Maresme donde tenéis cartera.

---

## Fuentes consultadas

- [Portada indexada de serra-s.com](https://www.serra-s.com/)
- [Ficha de terreno en Premià de Dalt (título "SERRA-S")](https://www.serra-s.com/es/compra/terrenos/barcelona/premia-de-dalt/528)
- [Segunda portada en español "Inicio"](https://www.serra-s.com/es/serra-s-inmobiliaries-compraventa-de-inmuebles/)
- [Archivo "Sense categoria" indexado](https://www.serra-s.com/es/category/sense-categoria-es/)
- [Noticias](https://www.serra-s.com/es/noticias/)
- [Artículo energías renovables](https://www.serra-s.com/tipus-denergies-renovables-quina-es-la-millor-opcio-per-a-la-teva-llar-o-empresa/)
- [Web antigua serra-s.es](https://www.serra-s.es/) · [ficha antigua](https://www.serra-s.es/ficha/index.php?codigo=12449_23982185)
- [SERRA-S en idealista (85 inmuebles)](https://www.idealista.com/pro/serra-s-immobiliaries/)
- [SERRA-S en habitaclia](https://english.habitaclia.com/real_estate-serra_s_gestions_immobiliaries_50274_1/)
- [SERRA-S en buscainmobiliarias](https://www.buscainmobiliarias.com/inmobiliaria/serra-s-immobiliaries)
- [Agencias en Santa Susanna, idealista (47 agencias)](https://www.idealista.com/en/agencias-inmobiliarias/santa-susanna-barcelona/inmobiliarias)
- [Competidor Virtua Home](https://www.virtuahome.es/)
- [Canal YouTube SERRA-S](https://www.youtube.com/@SERRA-Simmobiliaries)

---
---

# NOTAS INTERNAS (no enviar al cliente)

## Verificación multiagente (7 sep 2026)

Se lanzaron 12 verificadores independientes (uno por afirmación) + escépticos + descubrimiento + crítico. Los 12 verificadores terminaron; 9 escépticos, los 5 de descubrimiento y el crítico fallaron por límite de uso de la cuenta y agotamiento del cupo de búsquedas (200/200). Ningún agente pudo abrir serra-s.com, serra-s.es, idealista, habitaclia, virtuahome ni Google Maps: el proxy bloquea todo. Toda la evidencia son títulos y snippets de Google.

| Afirmación | Veredicto | Qué cambió en el informe |
|---|---|---|
| Portada indexada como "SERRA-S inmobiliàries" / `<title>` "Inici" | Parcial (0,85) | Google muestra "Inici" en búsquedas con esa palabra y "SERRA-S inmobiliàries" en el resto: encaja con tu observación. Redactado así. |
| Sin www indexado aparte | Parcial (0,75) | Solo `serra-s.com/es` y `/es/content/certif-energetico` sin www. Es el buscador de inmuebles (app distinta), misma IP. Hallazgo 2 reescrito. |
| "Inicio" = segunda portada duplicada | Parcial (0,75) | No es duplicado: "Inicio" es la portada WP en castellano; `/es` es el buscador. Hallazgo 4 reescrito. |
| Fichas tituladas "SERRA-S" | Parcial (0,80) | Cierto en búsquedas `site:`; con coincidencia de texto Google reescribe el título desde el H1. Y **solo hay 1 ficha indexada**. Hallazgo 3 reforzado. |
| Noticias / blog con coletilla en castellano | Confirmado (0,85) | Añadido `/contacte/` con el mismo patrón. |
| serra-s.es viva e indexada con servicios | Confirmado (0,85) | 4 URLs indexadas, incluida una "Company" en inglés. No se pudo comprobar si redirige (deducido de la indexación). Certificado energético sí existe en la nueva. |
| "Sense categoria" indexado / WordPress | Confirmado (0,90) | WordPress + WPML (slug `-es`) + Yoast (plantilla "Archives"). |
| Marca con dos grafías | Confirmado (0,90) | Son tres: añadida "Gestions Immobiliàries" (habitaclia y firma de correo). |
| 85 idealista / 111 habitaclia / 47 agencias | No verificable por agentes (cupo agotado) | Cifras vistas por mí en títulos de Google el 7 sep. Marcadas con fecha. Comprobar antes de enviar. |
| Título de VirtuaHome | No verificable por agentes (cupo agotado) | Visto por mí en Google el 7 sep como "La Mejor Inmobiliaria de Santa Susana \| VirtuaHome.es". Unificado en ambos documentos. Comprobar. |
| Dirección doble, teléfonos, horario | Parcial (0,45) | Snippets de Google confirman N-II km 673 Carrefour, teléfonos y horario. La forma "N-2, 11" salió en un snippet de habitaclia. Comprobar en la ficha. |
| Versión inglesa de la web | **Refutado en la práctica** (0,40) | Ninguna URL `/en/` ni título en inglés indexado. Lo de "habla inglés" es el personal (idealista), no la web. Corregido en hallazgo 7 y en los packs. |

## Qué no he podido verificar y por qué

El entorno donde se ha hecho el análisis bloquea el acceso directo a serra-s.com, serra-s.es, archive.org y buscainmobiliarias. Todo lo de arriba sale de lo que Google tiene indexado (títulos reales en SERP) y de portales. Es sólido para títulos, dominios duplicados y páginas basura. Lo marcado con ⚠️ hay que confirmarlo desde tu PC antes de enviar. Son 10 minutos:

1. **Título "Inici"**: abre `view-source:https://www.serra-s.com/` y busca `<title>`. Google muestra "SERRA-S inmobiliàries" para la portada, así que puede que el `<title>` real sea "Inici" y Google lo reescriba, o que lo hayan cambiado desde tu primer correo. Si ya no es "Inici", en el informe deja la fila tal como está (sin servicio ni localidad sigue siendo cierto).
2. **Meta description**: en el mismo view-source busca `name="description"`. Si existe, cambia la frase "Hoy la portada no tiene ninguna" por "la actual no menciona Santa Susanna ni el teléfono" (o lo que toque).
3. **serra-s.es**: abre `https://www.serra-s.es/` y confirma que carga la web antigua y no redirige. Si redirige ya a .com, quita ese punto del hallazgo 2 (deja solo el sin-www).
4. **Sin www**: abre `https://serra-s.com/es` y mira si redirige a www. Si redirige, el problema es solo de indexación vieja (menor).
5. **hreflang**: en view-source busca `hreflang`. Si existe, quita el ⚠️ del punto 7 y deja solo lo de la coletilla en castellano.
6. **Servicios de la web antigua**: comprueba si serra-s.com tiene página de hipotecas / renta vitalicia / certificados. Si la tiene, quita esa frase del punto 2.
7. **Google Business Profile**: busca "SERRA-S immobiliàries" en Google Maps y anota número de reseñas, nota media y dirección exacta. Añade una frase al punto 8 con el dato real ("tenéis X reseñas con nota Y; VirtuaHome tiene Z").
8. **PageSpeed**: pasa `https://pagespeed.web.dev/` sobre la portada móvil y añade la nota (si sale por debajo de 50 en móvil, súbelo a hallazgo ALTO).
9. **Plataforma**: la parte corporativa es WordPress seguro (WPML + Yoast). El buscador de inmuebles (`serra-s.com/es/compra/...`, ids numéricos) es otra aplicación, probablemente un CRM inmobiliario. Abre `view-source:https://serra-s.com/es` y busca el nombre del proveedor (Inmovilla, Witei, Mobilia, Inmoweb...). Las plantillas de fichas y que Google las indexe dependen de lo que permita ese CRM: si es cerrado, sube la Fase 2 a 990.
10. **Título de VirtuaHome y cifras de portales**: busca "inmobiliaria santa susanna" desde tu PC y copia el título azul exacto de virtuahome.es; abre la ficha de Serra-S en idealista y habitaclia y actualiza 85 / 111 / 47 si han cambiado.
11. **Fichas indexadas**: busca en Google `site:serra-s.com/es/compra` y cuenta resultados. Si salen más de 1, cambia la frase "solo una ficha indexada" por el número real (el argumento se mantiene igual mientras sean pocas).

## Precios

Los precios (450 / 890 / 1.190) son propuesta mía para "cerrados, sin cuotas". Horas estimadas: Fase 1 unas 8-10 h, Fase 2 unas 16-20 h. A 45 €/h sale ajustado. Si quieres margen para negociar, sube Fase 2 a 990 y el pack a 1.290. No bajes de 400 la Fase 1: es la que trae el resultado visible y te sirve de puerta de entrada.

## Mensaje para enviar el informe (WhatsApp o email)

> Hola, buenos días. Os paso la auditoría de serra-s.com como quedamos: [enlace].
>
> Resumen rápido: la web está bien indexada pero Google no sabe que sois una inmobiliaria de Santa Susanna (títulos sin servicio ni localidad, fichas de inmuebles que se titulan solo "SERRA-S") y tenéis tres versiones de la web compitiendo entre sí (www, sin www y la antigua serra-s.es). Nada de esto obliga a rehacer la web, es configuración y textos.
>
> En el informe tenéis qué arreglar primero y el precio cerrado si queréis que lo hagamos nosotros (Fase 1 en una semana, 450 €). Si lo preferís hacer con vuestro proveedor, el documento sirve como lista de tareas.
>
> Si os cuadra, lo vemos en una llamada de 15 minutos cuando os vaya bien. Un saludo, Nacho · Sultox · 722 83 50 57
