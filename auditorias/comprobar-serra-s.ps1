# Comprobaciones de serra-s.com desde un PC con Windows 10/11 (usa curl.exe, incluido en Windows).
# Uso: abre PowerShell, pega todo el bloque y pulsa Enter. Deja el resultado en el Escritorio (serra-s-check.txt).

$out = "$env:USERPROFILE\Desktop\serra-s-check.txt"
"Comprobacion serra-s.com  $(Get-Date -Format 'yyyy-MM-dd HH:mm')" | Out-File $out -Encoding utf8

# 1) Redirecciones: que hace cada variante del dominio
"`n### REDIRECCIONES (codigo -> destino)" | Tee-Object -FilePath $out -Append
foreach ($u in "http://serra-s.com/","https://serra-s.com/","http://www.serra-s.com/","https://www.serra-s.com/","https://serra-s.com/es","https://www.serra-s.com/es/","https://www.serra-s.com/es","http://serra-s.es/","https://serra-s.es/","https://www.serra-s.es/","https://www.serra-s.es/index.php?vistas=1") {
  $line = & curl.exe -sS -o NUL -w "%{http_code} -> %{redirect_url}" --max-time 20 -A "Mozilla/5.0" $u 2>&1
  "$u : $line" | Tee-Object -FilePath $out -Append
}

# 2) Contenido de las paginas clave
$pages = [ordered]@{
  "PORTADA_CA"   = "https://www.serra-s.com/"
  "PORTADA_ES"   = "https://www.serra-s.com/es/serra-s-inmobiliaries-compraventa-de-inmuebles/"
  "ES_SIN_WWW"   = "https://serra-s.com/es"
  "CONTACTE"     = "https://www.serra-s.com/contacte/"
  "FICHA"        = "https://www.serra-s.com/es/compra/terrenos/barcelona/premia-de-dalt/528"
  "WEB_ANTIGUA"  = "https://www.serra-s.es/"
  "ROBOTS"       = "https://www.serra-s.com/robots.txt"
  "SITEMAP_IDX"  = "https://www.serra-s.com/sitemap_index.xml"
  "SITEMAP"      = "https://www.serra-s.com/sitemap.xml"
}
$pat = @(
  '<title[^>]*>[^<]*</title>',
  '<meta[^>]+name=["'']description["''][^>]*>',
  '<meta[^>]+name=["'']robots["''][^>]*>',
  '<meta[^>]+property=["'']og:title["''][^>]*>',
  '<meta[^>]+name=["'']generator["''][^>]*>',
  '<link[^>]+rel=["'']canonical["''][^>]*>',
  '<link[^>]+hreflang=[^>]*>',
  '<html[^>]*>',
  '<h1[^>]*>.*?</h1>'
)
foreach ($k in $pages.Keys) {
  $u = $pages[$k]
  $html = (& curl.exe -sSL --max-time 30 -A "Mozilla/5.0" $u 2>&1) | Out-String
  "`n===== $k  $u  (bytes: $($html.Length))" | Tee-Object -FilePath $out -Append
  if ($k -like "ROBOTS*" -or $k -like "SITEMAP*") {
    $html.Substring(0, [Math]::Min(1500, $html.Length)) | Tee-Object -FilePath $out -Append
    continue
  }
  foreach ($p in $pat) {
    [regex]::Matches($html, $p, 'IgnoreCase,Singleline') | ForEach-Object { ($_.Value -replace '\s+', ' ').Substring(0, [Math]::Min(300, ($_.Value -replace '\s+', ' ').Length)) } | Select-Object -First 6 | Tee-Object -FilePath $out -Append
  }
  $imgs = [regex]::Matches($html, '<img[^>]*>', 'IgnoreCase')
  $sinAlt = ($imgs | Where-Object { $_.Value -notmatch 'alt=' }).Count
  "wp-content: $(([regex]::Matches($html,'wp-content')).Count) | wpml: $(([regex]::Matches($html,'wpml|sitepress','IgnoreCase')).Count) | yoast: $(([regex]::Matches($html,'yoast','IgnoreCase')).Count) | json-ld: $(([regex]::Matches($html,'application/ld\+json')).Count) | imagenes: $($imgs.Count) | sin alt: $sinAlt" | Tee-Object -FilePath $out -Append
  "scripts:" | Tee-Object -FilePath $out -Append
  [regex]::Matches($html, '<script[^>]+src=["'']([^"'']+)["'']', 'IgnoreCase') | ForEach-Object { "  " + $_.Groups[1].Value } | Select-Object -First 12 | Tee-Object -FilePath $out -Append
}

"`nListo. Archivo: $out" | Tee-Object -FilePath $out -Append
Start-Process notepad.exe $out
