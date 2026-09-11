"""Convert a Claude Code session .jsonl into a readable Markdown transcript.
Keeps user prompts and assistant prose; tool calls are reduced to one-line
markers (tool name + description); tool results and thinking are omitted."""
import json, sys, datetime
src, dst = sys.argv[1], sys.argv[2]
out=[]
def ts(d):
    t=d.get('timestamp');
    return datetime.datetime.fromisoformat(t.replace('Z','+00:00')).strftime('%Y-%m-%d %H:%M UTC') if t else ''
for line in open(src):
    d=json.loads(line)
    if d.get('isSidechain'): continue
    t=d.get('type')
    if t not in ('user','assistant'): continue
    m=d.get('message',{}); c=m.get('content')
    if t=='user':
        if isinstance(c,str): text=c
        else:
            parts=[]
            for b in c:
                if b.get('type')=='text': parts.append(b['text'])
                elif b.get('type')=='tool_result': pass
            text='\n'.join(parts)
        if not text.strip(): continue
        if text.startswith('<command-message>'): text='`/familiarize-project` (skill invocation)'
        if text.startswith('<system-reminder>') or text.startswith('[SYSTEM NOTIFICATION') or 'task-notification' in text[:200]: continue
        if text.startswith('Base directory for this skill'): continue
        out.append(f'\n---\n\n## TJO — {ts(d)}\n\n{text.strip()}\n')
    else:
        parts=[]
        for b in c:
            if b.get('type')=='text' and b['text'].strip(): parts.append(b['text'].strip())
            elif b.get('type')=='tool_use':
                inp=b.get('input',{}); desc=inp.get('description') or inp.get('file_path') or inp.get('skill') or ''
                parts.append(f'> *[tool: {b["name"]} — {desc}]*')
        if parts: out.append(f'\n### Claude — {ts(d)}\n\n'+'\n\n'.join(parts)+'\n')
open(dst,'w').write('# Session transcript — arithmetic-quantum-mechanics, 2026-09-10/11\n\nConverted from the Claude Code session log `session-2026-09-10-be21a927.jsonl` (kept verbatim alongside). Tool results and model reasoning are omitted; tool calls appear as one-line markers.\n'+''.join(out))
print('wrote',dst,len(out),'entries')
