"""Builds DRON.html: the shared head, nav and mobile menu from SportGuardian.html, then dron.css and dron-main.html.
Run from the repo root: python tools/dron/build/build.py"""
import re

sg = open('SportGuardian.html', encoding='utf-8').read().split('\n')
head = '\n'.join(sg[0:55])
head = head.replace('<title>Sport Guardian | Olena Bozhenko</title>', '<title>DRON | Olena Bozhenko</title>')
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="DRON, a drone-as-a-service product designed from research to handoff with AI tools: research, audience, jobs to be done, flows, tone of voice, wireframes, journey map, design system and handoff, by Olena Bozhenko.">', head)
head = head.replace('<!-- Display layer. Content source: sportguardian.md -->', '<!-- Display layer. Content source: dron.md; built by tools/dron/build/build.py -->')
head = head.replace('  /* project colours (sportguardian.md): teal #418B91, green #15EDA3 */\n  --teal:#418B91;--green:#15EDA3;--deep:#2F6A6F;\n', '')
assert 'teal' not in head
menu = '\n'.join(sg[258:281])
css = open('tools/dron/build/dron.css', encoding='utf-8').read()
css = css.replace('url(../../../assets/work/dron/handoff-ground.webp)', 'url(assets/work/dron/handoff-ground.webp)')
css = css.replace('@keyframes chip{0%{background:#3E3E3E;color:var(--txt)}33%,100%{background:#3E3E3E;color:var(--txt)}0.01%,33%{background:var(--green);color:var(--charcoal)}}', '@keyframes chip{0%,33%{background:var(--green);color:var(--charcoal)}33.01%,100%{background:#3E3E3E;color:var(--txt)}}')
tail = '\n'.join(sg[281:283])
body = '\n'.join(sg[283:285]) + '\n' + '\n'.join(sg[289:324])
body = body.replace('<a class="skip" href="#work-grid">Skip to the product</a>', '<a class="skip" href="#research">Skip to the process</a>')
main = open('tools/dron/build/dron-main.html', encoding='utf-8').read()
out = head + '\n' + css + '\n' + menu + '\n' + tail + '\n' + body + '\n\n' + main
assert '—' not in out.split('<body>')[1], 'no em dash in visible text'
open('DRON.html', 'w', encoding='utf-8').write(out)
print('DRON.html', len(out.split('\n')), 'lines')
