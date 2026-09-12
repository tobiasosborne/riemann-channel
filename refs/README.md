# refs

`fetch_sources.sh` downloads the arXiv TeX source of every paper cited in
`notes/prior-art-quantum-ihara.md` into `refs/src/<arxiv-id>/` (gitignored; other
people's TeX is not redistributed here) and writes `manifest.sha256`. Quotes in
`notes/` are cited as `<arxiv-id>:<file>:<line>` against these files, so anyone can
re-fetch and byte-check them. Preference: TeX source, never PDF text extraction.
