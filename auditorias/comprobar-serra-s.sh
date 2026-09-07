out="$HOME/Desktop/serra-s-check.txt"
UA='Mozilla/5.0 (Macintosh) Sultox-check'

check() {
  name=$1; u=$2
  html=$(curl -sSL --max-time 30 -A "$UA" "$u" 2>&1)
  echo; echo "===== $name  $u  (bytes: ${#html})"
  case $name in
    ROBOTS*|SITEMAP*) printf '%s\n' "$html" | head -c 1500; echo; return;;
  esac
  printf '%s' "$html" | perl -0777 -ne '
    for my $re (
      qr{<title[^>]*>[^<]*</title>}i,
      qr{<meta[^>]+name=["\x27]description["\x27][^>]*>}i,
      qr{<meta[^>]+name=["\x27]robots["\x27][^>]*>}i,
      qr{<meta[^>]+property=["\x27]og:title["\x27][^>]*>}i,
      qr{<meta[^>]+name=["\x27]generator["\x27][^>]*>}i,
      qr{<link[^>]+rel=["\x27]canonical["\x27][^>]*>}i,
      qr{<link[^>]+hreflang=[^>]*>}i,
      qr{<html[^>]*>}i,
      qr{<h1[^>]*>.*?</h1>}is,
    ) {
      my $n = 0;
      while (/$re/g) { my $m = $&; $m =~ s/\s+/ /g; print substr($m, 0, 300), "\n"; last if ++$n >= 6 }
    }
    my $wp   = () = /wp-content/g;
    my $wpml = () = /wpml|sitepress/ig;
    my $yo   = () = /yoast/ig;
    my $ld   = () = /application\/ld\+json/g;
    my @imgs = /<img[^>]*>/ig;
    my $noalt = grep { not /alt=/i } @imgs;
    print "wp-content: $wp | wpml: $wpml | yoast: $yo | json-ld: $ld | imagenes: ", scalar(@imgs), " | sin alt: $noalt\n";
    print "scripts:\n";
    my $c = 0;
    while (/<script[^>]+src=["\x27]([^"\x27]+)["\x27]/ig) { print "  $1\n"; last if ++$c >= 12 }
  '
}

{
  echo "Comprobacion serra-s.com  $(date '+%Y-%m-%d %H:%M')"
  echo; echo "### REDIRECCIONES (codigo -> destino)"
  for u in \
    http://serra-s.com/ https://serra-s.com/ http://www.serra-s.com/ https://www.serra-s.com/ \
    https://serra-s.com/es https://www.serra-s.com/es/ https://www.serra-s.com/es \
    http://serra-s.es/ https://serra-s.es/ https://www.serra-s.es/ 'https://www.serra-s.es/index.php?vistas=1'
  do
    printf '%s : ' "$u"
    curl -sS -o /dev/null -w '%{http_code} -> %{redirect_url}\n' --max-time 20 -A "$UA" "$u" 2>&1
  done

  check PORTADA_CA  https://www.serra-s.com/
  check PORTADA_ES  https://www.serra-s.com/es/serra-s-inmobiliaries-compraventa-de-inmuebles/
  check ES_SIN_WWW  https://serra-s.com/es
  check CONTACTE    https://www.serra-s.com/contacte/
  check FICHA       https://www.serra-s.com/es/compra/terrenos/barcelona/premia-de-dalt/528
  check WEB_ANTIGUA https://www.serra-s.es/
  check ROBOTS      https://www.serra-s.com/robots.txt
  check SITEMAP_IDX https://www.serra-s.com/sitemap_index.xml
  check SITEMAP     https://www.serra-s.com/sitemap.xml

  echo; echo "Listo. Archivo: $out"
} 2>&1 | tee "$out"

command -v open >/dev/null && open -e "$out"
