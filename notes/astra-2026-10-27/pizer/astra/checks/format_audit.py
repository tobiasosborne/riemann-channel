"""Normalize draft TeX delimiters with --fix, otherwise validate formatting."""
from pathlib import Path
import re,sys
path=Path(__file__).resolve().parents[1]/'astra-proofs.md'
text=path.read_text()
if '--fix' in sys.argv:
    text=text.replace('\\[','$$').replace('\\]','$$')
    out=[]; display=False; changes=0
    for line in text.splitlines(keepends=True):
        if line.strip()=='$$':
            display=not display; out.append(line); continue
        if display: out.append(line); continue
        stack=[]; pairs=[]
        for i,c in enumerate(line):
            if c=='(': stack.append(i)
            elif c==')' and stack:
                o=stack.pop()
                explicit=(o>0 and line[o-1]=='\\') or (i>0 and line[i-1]=='\\')
                end=i-1 if line[i-1]=='\\' else i
                body=line[o+1:end]
                math=explicit or bool(re.search(r'[\\_^=<>|]',body)) or bool(re.fullmatch(r'[A-Za-z]',body)) or bool(re.fullmatch(r'[0-9A-Za-z ,]+',body) and ',' in body and not re.search(r'[A-Za-z]{2}',body))
                if math: pairs.append((o-1 if o>0 and line[o-1]=='\\' else o,i+1,body))
        selected=[]
        for a,b,body in sorted(pairs,key=lambda q:(q[0],-q[1])):
            if selected and a<selected[-1][1]: continue
            selected.append((a,b,body))
        for a,b,body in reversed(selected):
            line=line[:a]+'$'+body+'$'+line[b:]; changes+=1
        out.append(line)
    assert not display
    text=''.join(out); path.write_text(text)
    print('Normalized inline math spans:',changes)
assert '\\(' not in text and '\\)' not in text
display=False; inline=0
for n,line in enumerate(text.splitlines(),1):
    if line.strip()=='$$': display=not display
    elif not display:
        assert line.count('$')%2==0, (n,line)
        inline+=line.count('$')//2
assert not display
print('Inline math spans:',inline,'display boundaries:',sum(line.strip()=='$$' for line in text.splitlines()))
print('FORMAT AUDIT PASS')
