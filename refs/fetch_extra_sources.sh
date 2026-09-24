#!/usr/bin/env bash
# Fetch the non-arXiv sources cited by db/provenance.tsv (RTP round 1, lane B1, 2026-09-24) into refs/src/<key>/
# (gitignored) and regenerate the text files that the provenance rows address. Text layers come from
# `pdftotext -layout` (poppler-utils). Two sources are image-only scans whose OCR text (tesseract 5.3.4) is
# committed under refs/ocr/<key>/ and copied into place, so that line numbers are stable without tesseract.
# Hashes of the cited text files are appended to refs/manifest-extra.sha256. Run from anywhere.
set -eu
cd "$(dirname "$0")"
UA="Mozilla/5.0"
fetch() { # key url file
  mkdir -p "src/$1"; [ -f "src/$1/$3" ] || timeout 180 curl -sSL -A "$UA" -o "src/$1/$3" "$2"; }
txt() { # key
  [ -f "src/$1/paper.txt" ] || pdftotext -layout "src/$1/paper.pdf" "src/$1/paper.txt"; }
fetch bombieri-2000 "http://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0" paper.pdf; txt bombieri-2000
fetch yoshida-1992 "https://projecteuclid.org/ebooks/advanced-studies-in-pure-mathematics/Zeta-Functions-in-Geometry/chapter/On-Hermitian-forms-attached-to-zeta-functions/10.2969/aspm/02110281.pdf" paper.pdf; txt yoshida-1992
fetch klp-2000 "http://www.dei.unipd.it/~languasco/lavoripdf/R12.pdf" paper.pdf; txt klp-2000
fetch vandenberghe-andersen-2015 "https://www.seas.ucla.edu/~vandenbe/publications/chordalsdp.pdf" paper.pdf; txt vandenberghe-andersen-2015
fetch coste-2002 "https://perso.univ-rennes1.fr/goulwen.fichou/RAG1.pdf" paper.pdf; txt coste-2002
# image-only scans: Landau 1912 (GDZ, https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0071/LOG_0057.pdf,
# page images .../content/PPN235181684_0071/1000/0/00000NNN.jpg, NNN = 566..582) and Burg 1975 (Stanford SEP thesis
# page https://sep.sites.stanford.edu/publications/theses/maximum-entropy-spectral-analysis-sep-6-1975, chapter
# PDFs on Google Drive). The committed OCR text is the cited file; the PDFs are optional for reading.
fetch landau-1912 "https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0071/LOG_0057.pdf" paper.pdf || true
mkdir -p src/landau-1912 src/burg-1975
cp -n ocr/landau-1912/paper.ocr.txt src/landau-1912/ 2>/dev/null || true
cp -n ocr/burg-1975/*.ocr.txt src/burg-1975/ 2>/dev/null || true
: > manifest-extra.sha256
for f in src/bombieri-2000/paper.txt src/yoshida-1992/paper.txt src/klp-2000/paper.txt src/vandenberghe-andersen-2015/paper.txt src/coste-2002/paper.txt src/landau-1912/paper.ocr.txt src/burg-1975/ch1.ocr.txt src/burg-1975/ch2a.ocr.txt src/burg-1975/ch2b.ocr.txt; do
  [ -f "$f" ] && sha256sum "$f" >> manifest-extra.sha256
done
echo "extra sources: $(wc -l < manifest-extra.sha256) text files hashed"
