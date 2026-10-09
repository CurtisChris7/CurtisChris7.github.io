from pathlib import Path
import math, random, html
p=Path(__file__).parent/'assets';p.mkdir(exist_ok=True)

def svg(content,bg='#e8e7dd',size=(900,680)):
 w,h=size
 return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect width="100%" height="100%" fill="{bg}"/>{content}</svg>'''
# CIPHERGRID image
s=[]
s.append('''<defs><pattern id="grain" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#204639" opacity=".07"/></pattern><marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#e3774b"/></marker></defs><rect width="900" height="680" fill="url(#grain)"/><circle cx="755" cy="115" r="265" fill="#d8decf"/><circle cx="755" cy="115" r="195" fill="none" stroke="#8b9c8f" stroke-dasharray="2 12" stroke-width="2"/>''')
s.append('<text x="72" y="68" fill="#3d5e50" font-family="monospace" font-size="17" letter-spacing="3">MULTIMODAL RULE INFERENCE / 01</text>')
s.append('<g transform="translate(112,110) rotate(-5 304 274)"><rect x="-22" y="-22" width="608" height="552" rx="8" fill="#d1d7c8"/><rect x="-12" y="-12" width="588" height="532" rx="5" fill="#f5f3e8"/>')
random.seed(23)
cells=[]
for row in range(8):
 for col in range(8):
  x=4+col*70;y=4+row*63
  wall=(row,col) in {(0,2),(0,4),(1,2),(2,2),(3,2),(3,3),(3,5),(5,0),(5,1),(5,5),(6,5),(7,5),(1,6),(4,6)}
  v='ca' if wall else 'pa'
  if (row,col)==(0,0):v='na'
  if (row,col)==(7,7):v='da'
  if (row,col) in {(2,5),(6,2)}:v='ea'
  c={'ca':'#a3b9ab','pa':'#e9ebdf','na':'#eab28e','da':'#83a799','ea':'#d6adac'}[v]
  s.append(f'<rect x="{x}" y="{y}" width="63" height="56" rx="3" fill="{c}"/><text x="{x+31.5}" y="{y+33}" font-family="monospace" font-size="17" text-anchor="middle" fill="#426358">{v}</text>')
s.append('<path d="M36 34 L106 34 L106 97 L106 160 L176 160 L246 160 L246 97 L316 97 L386 97 L386 160 L456 160 L456 223 L526 223 L526 286 L526 349 L456 349 L456 412 L526 412 L526 475" fill="none" stroke="#e37649" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity=".8" marker-end="url(#arrow)"/>')
s.append('</g>')
s.append('''<g transform="translate(646,424)"><rect width="206" height="126" rx="5" fill="#1d4437"/><text x="18" y="31" fill="#a5cab6" font-family="monospace" font-size="12" letter-spacing="1">DECODE → PLAN</text><text x="18" y="68" fill="#f8f4e7" font-family="monospace" font-size="17">za · ma · ga</text><text x="18" y="99" fill="#edaa80" font-family="monospace" font-size="13">? ? ? → goal</text></g><path d="M742 560 L742 625" stroke="#38594c" stroke-width="1"/><text x="684" y="647" fill="#38594c" font-family="monospace" font-size="11" letter-spacing="1">635 CASES</text>''')
(p/'ciphergrid.svg').write_text(svg(''.join(s),'#e8e8db'),encoding='utf-8')

# Human / worker AI figure
s=['''<defs><pattern id="hgrid" width="35" height="35" patternUnits="userSpaceOnUse"><path d="M35 0H0V35" fill="none" stroke="#b69c91" opacity=".18" stroke-width="1"/></pattern></defs><rect width="900" height="680" fill="url(#hgrid)"/>''']
s.append('<circle cx="448" cy="306" r="225" fill="#eed8c9" stroke="#b99986" stroke-width="1.5"/><circle cx="448" cy="306" r="164" fill="none" stroke="#bc9c8b" stroke-width="1" stroke-dasharray="5 9"/>')
s.append('<g transform="translate(95,152)"><rect width="330" height="342" rx="9" fill="#f9f3e8" stroke="#c4a69a"/><rect width="330" height="62" rx="9" fill="#d6ad9d"/><text x="21" y="39" fill="#543e38" font-size="16" font-family="monospace">HUMAN EXPERTISE</text><circle cx="46" cy="129" r="23" fill="#d17858"/><path d="M5 208Q5 150 46 150Q88 150 88 208" fill="#d17858"/><text x="103" y="125" font-size="17" fill="#30463c" font-family="Arial">Goals &amp; judgment</text><text x="103" y="151" font-size="13" fill="#5e6b61" font-family="monospace">Direction retained</text><rect x="19" y="238" width="284" height="10" rx="5" fill="#cdd9cb"/><rect x="19" y="263" width="211" height="10" rx="5" fill="#d9dfd4"/><rect x="19" y="287" width="248" height="10" rx="5" fill="#d9dfd4"/></g>')
s.append('<g transform="translate(484,214)"><rect width="318" height="296" rx="9" fill="#254a3d"/><rect width="318" height="62" rx="9" fill="#346b55"/><text x="22" y="39" fill="#e4ecdd" font-size="16" font-family="monospace">AI SUPPORT</text><circle cx="72" cy="137" r="31" fill="none" stroke="#eab48f" stroke-width="5"/><circle cx="72" cy="137" r="11" fill="#eab48f"/><circle cx="72" cy="137" r="50" fill="none" stroke="#6d9e84" stroke-dasharray="4 9"/><text x="142" y="131" font-size="18" fill="#e5ece4" font-family="Arial">Propose</text><text x="142" y="159" font-size="18" fill="#e5ece4" font-family="Arial">Refine</text><rect x="25" y="225" width="260" height="9" rx="4" fill="#6a9983"/><rect x="25" y="248" width="211" height="9" rx="4" fill="#6a9983"/></g>')
s.append('''<path d="M407 260C453 243 473 246 505 260" stroke="#e37e58" stroke-width="7" fill="none"/><path d="M505 260l-16 -17l1 28Z" fill="#e37e58"/><path d="M505 417C464 440 440 440 409 427" stroke="#e37e58" stroke-width="7" fill="none"/><path d="M409 427l16 -17l1 27Z" fill="#e37e58"/><text x="99" y="90" fill="#765b51" font-family="monospace" font-size="19" letter-spacing="2">WORKER-CENTERED SYSTEMS</text>''')
(p/'worker-ai.svg').write_text(svg(''.join(s),'#f0dfd2'),encoding='utf-8')
# legibility visualization
s=['''<defs><pattern id="lines" width="42" height="42" patternUnits="userSpaceOnUse"><path d="M42 0H0V42" fill="none" stroke="#b0c4c1" opacity=".16"/></pattern></defs><rect width="900" height="680" fill="url(#lines)"/><text x="73" y="91" fill="#557474" font-family="monospace" font-size="18" letter-spacing="2">THE PROFESSIONAL LEGIBILITY GAP</text><rect x="72" y="158" width="285" height="325" rx="10" fill="#e8f0eb" stroke="#a7c2b5"/><rect x="537" y="158" width="285" height="325" rx="10" fill="#31574d"/>''']
s.append('<text x="104" y="207" fill="#386657" font-family="monospace" font-size="14">LIVED EXPERTISE</text><text x="569" y="207" fill="#bbd7c7" font-family="monospace" font-size="14">RECOGNIZED VALUE</text>')
for i,word in enumerate(['EXPERIENCE','KNOW-HOW','IDENTITY','GOALS']):
 y=261+i*50;s.append(f'<rect x="103" y="{y-22}" width="217" height="38" rx="4" fill="#cfdfd5"/><text x="121" y="{y+3}" fill="#35594c" font-family="monospace" font-size="15">{word}</text>')
for i,word in enumerate(['CREDENTIALS','VISIBILITY','ACCESS','OPPORTUNITY']):
 y=261+i*50;s.append(f'<rect x="568" y="{y-22}" width="222" height="38" rx="4" fill="#467668"/><text x="583" y="{y+3}" fill="#eff4ea" font-family="monospace" font-size="14">{word}</text>')
s.append('''<path d="M358 329H539" stroke="#d67757" stroke-width="6" stroke-dasharray="7 10"/><path d="M520 315l21 14l-21 14" fill="none" stroke="#d67757" stroke-width="6"/><rect x="370" y="269" width="154" height="43" rx="5" fill="#e6ab8e"/><text x="447" y="294" text-anchor="middle" fill="#613e31" font-size="13" font-family="monospace">TRANSLATION</text><text x="450" y="549" text-anchor="middle" fill="#607979" font-family="monospace" font-size="17" letter-spacing="2">SKILLS ≠ RECOGNITION</text>''')
(p/'legibility.svg').write_text(svg(''.join(s),'#dce8e8'),encoding='utf-8')
# medical posts
s=['''<defs><pattern id="dots" width="25" height="25" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.1" fill="#bbbcc8"/></pattern></defs><rect width="900" height="680" fill="url(#dots)"/><text x="77" y="96" font-size="18" font-family="monospace" letter-spacing="2" fill="#6b6b83">WHO GETS AN ANSWER?</text>''']
for i,(x,y,w,h,title) in enumerate([(76,158,386,130,'QUESTION / 01'),(96,314,356,130,'QUESTION / 02'),(116,470,336,130,'QUESTION / 03')]):
 s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fcfbf6" stroke="#cfd0d8"/><circle cx="{x+31}" cy="{y+36}" r="12" fill="#adb8bf"/><text x="{x+60}" y="{y+40}" fill="#546175" font-family="monospace" font-size="14">{title}</text>')
 for row in range(2):s.append(f'<rect x="{x+28}" y="{y+69+row*21}" rx="4" width="{w-75-row*47}" height="8" fill="#d9dce2"/>')
s.append('''<path d="M463 228Q542 228 575 338M452 387Q539 387 575 338M454 543Q537 520 575 338" fill="none" stroke="#a3a2b7" stroke-width="4" stroke-dasharray="6 9"/><circle cx="664" cy="335" r="122" fill="#5d6b83"/><circle cx="664" cy="335" r="89" fill="none" stroke="#bdc9d8" stroke-width="3"/><circle cx="664" cy="317" r="29" fill="#f0d9bf"/><path d="M608 389Q608 349 664 349Q720 349 720 389" fill="#f0d9bf"/><text x="664" y="465" text-anchor="middle" font-family="monospace" font-size="15" fill="#445570" letter-spacing="1">EXPERT ATTENTION</text><circle cx="815" cy="166" r="34" fill="#efaa87"/><text x="815" y="178" fill="#4d4b56" text-anchor="middle" font-size="37" font-family="Arial">?</text>''')
(p/'medical.svg').write_text(svg(''.join(s),'#ebeaf0'),encoding='utf-8')
# positional encoding
s=['''<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#9da9a2" opacity=".18"/></pattern></defs><rect width="900" height="680" fill="url(#g)"/><text x="77" y="91" fill="#516356" font-family="monospace" font-size="18" letter-spacing="2">POSITIONAL REPRESENTATIONS</text><path d="M84 523H810M85 150V526" fill="none" stroke="#8d9d8d" stroke-width="2"/>''']
for i,(color,freq,amp,phase) in enumerate([('#c27952',.013,112,0),('#558f7d',.020,80,1.2),('#7782a1',.034,57,0.8)]):
 pts=[]
 for x in range(87,808,5):
  y=337 + (i-1)*67+amp*math.sin((x-87)*freq+phase)
  pts.append(f'{x},{y:.1f}')
 s.append(f'<polyline points="{" ".join(pts)}" stroke="{color}" fill="none" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" opacity=".86"/>')
s.append('''<g transform="translate(542,112)"><rect width="253" height="92" rx="5" fill="#e1e9dd" stroke="#c7d2c8"/><text x="19" y="32" font-family="monospace" font-size="13" fill="#61796e">FROM SINUSOIDAL</text><text x="19" y="64" font-family="monospace" font-size="13" fill="#355d4e">TO RoPE / ALiBi</text></g><g fill="#566b5b" font-family="monospace" font-size="12"><text x="85" y="561">POSITION →</text><text x="79" y="600">ORDER / DISTANCE / STRUCTURE</text></g>''')
(p/'positional.svg').write_text(svg(''.join(s),'#e8eadd'),encoding='utf-8')
# social card
social='''<rect x="0" y="0" width="1200" height="630" fill="#17372e"/><circle cx="985" cy="298" r="238" fill="none" stroke="#8ba998" stroke-width="2"/><circle cx="985" cy="298" r="177" fill="none" stroke="#8ba998" stroke-dasharray="5 11"/><circle cx="985" cy="298" r="115" fill="#e4ece0"/><text x="985" y="334" fill="#1a3c30" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="102">CC</text><text x="74" y="118" font-family="Arial" font-size="21" letter-spacing="4" fill="#c6d9c8">PHD RESEARCHER · NORTHEASTERN UNIVERSITY</text><text x="70" y="323" font-family="Georgia" font-size="113" fill="#f4f4e9">Christopher</text><text x="70" y="437" font-family="Georgia" font-style="italic" font-size="113" fill="#e7a082">Curtis.</text><text x="75" y="533" font-family="Arial" font-size="25" fill="#c4d9c9">AI EVALUATION / HUMAN–AI SYSTEMS</text>'''
(p/'social-card.svg').write_text(svg(social,'#17372e',(1200,630)),encoding='utf-8')
(p/'favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#1a382f"/><text x="32" y="46" font-family="Georgia" font-size="53" font-style="italic" text-anchor="middle" fill="#f0e9dd">c<tspan fill="#e78b6b">.</tspan></text></svg>''',encoding='utf-8')
print('Created:',*[q.name for q in p.glob('*.svg')])
