#!/usr/bin/env python3
"""Original, hand-redrawn emoji-scale geometry. Build SVGs and metadata offline."""
from pathlib import Path
from math import sin,cos,pi
import json,html
ROOT=Path(__file__).resolve().parents[1]
W='#FFFFFF';R='#E5323E';Y='#FFCC33';G='#269B59';B='#2455A4';L='#55ACEE';K='#292F33';D='#253B80'
def n(x):return f'{x:.3f}'.rstrip('0').rstrip('.')
def rect(x,y,w,h,c):return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" fill="{c}"/>'
def path(d,c,stroke=None,sw=.5):return f'<path d="{d}" fill="{c}"'+(f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if stroke else '')+'/>'
def poly(points,c):return '<polygon points="'+' '.join(f'{n(x)},{n(y)}' for x,y in points)+f'" fill="{c}"/>'
def circle(x,y,r,c):return f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{c}"/>'
def ellipse(x,y,rx,ry,c):return f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(rx)}" ry="{n(ry)}" fill="{c}"/>'
def star(x,y,r,c=W,points=5,inner=.42):
 return poly([(x+(r if i%2==0 else r*inner)*sin(i*pi/points),y-(r if i%2==0 else r*inner)*cos(i*pi/points)) for i in range(points*2)],c)
def stripes(colors):return ''.join(rect(0,5+i*26/len(colors),36,26/len(colors)+.015,c) for i,c in enumerate(colors))
def diamond(c,dx=15,dy=10):return poly([(18,18-dy),(18+dx,18),(18,18+dy),(18-dx,18)],c)
def cross(x,y,s,c):return rect(x-s*.16,y-s*.65,s*.32,s*1.3,c)+rect(x-s*.5,y-s*.32,s,s*.28,c)
def southern_cross(x,y,s,c=W):return ''.join(star(x+dx*s,y+dy*s,r*s,c) for dx,dy,r in [(0,-.65,.26),(-.65,0,.24),(.65,.04,.24),(.15,.38,.14),(0,.82,.3)])
# A compact geometric alphabet, rendered as paths rather than font-dependent SVG text.
GLYPHS={'A':'0,6 2,0 4,6|1,3 3,3','B':'0,6 0,0 3,0 4,1 4,2 3,3 0,3|3,3 4,4 4,5 3,6 0,6','C':'4,0 1,0 0,1 0,5 1,6 4,6','D':'0,6 0,0 2,0 4,2 4,4 2,6 0,6','E':'4,0 0,0 0,6 4,6|0,3 3,3','F':'0,6 0,0 4,0|0,3 3,3','G':'4,0 1,0 0,1 0,5 1,6 4,6 4,3 2,3','H':'0,0 0,6|4,0 4,6|0,3 4,3','I':'1,0 3,0|2,0 2,6|1,6 3,6','L':'0,0 0,6 4,6','M':'0,6 0,0 2,3 4,0 4,6','N':'0,6 0,0 4,6 4,0','O':'1,0 3,0 4,1 4,5 3,6 1,6 0,5 0,1 1,0','P':'0,6 0,0 3,0 4,1 4,2 3,3 0,3','Q':'1,0 3,0 4,1 4,5 3,6 1,6 0,5 0,1 1,0|2,4 4,6','R':'0,6 0,0 3,0 4,1 4,2 3,3 0,3|2,3 4,6','S':'4,0 1,0 0,1 0,2 1,3 3,3 4,4 4,5 3,6 0,6','T':'0,0 4,0|2,0 2,6','U':'0,0 0,5 1,6 3,6 4,5 4,0','V':'0,0 2,6 4,0','X':'0,0 4,6|4,0 0,6','1':'1,1 2,0 2,6|0,6 4,6','2':'0,1 1,0 3,0 4,1 4,2 0,6 4,6','3':'0,0 3,0 4,1 4,2 3,3 1,3|3,3 4,4 4,5 3,6 0,6','8':'1,0 3,0 4,1 4,2 3,3 1,3 0,2 0,1 1,0|1,3 0,4 0,5 1,6 3,6 4,5 4,4 3,3'}
def lettering(t,x,y,height,c,angle=0):
 scale=height/6; width=(len(t)*5-1)*scale;result=''
 for i,ch in enumerate(t):
  for seg in GLYPHS.get(ch,'').split('|'):
   if not seg:continue
   pts=[tuple(map(float,a.split(','))) for a in seg.split()]
   dd='M'+' L'.join(f'{n(x-width/2+(i*5+a)*scale)} {n(y+b*scale)}' for a,b in pts)
   result+=path(dd,'none',c,max(.12,height*.10))
 return f'<g transform="rotate({angle} {x} {y})">{result}</g>'
def wreath(x,y,s,c=G):
 out=''
 for sign in [-1,1]:
  out+=path(f'M{n(x)} {n(y+s)} Q{n(x+sign*s*1.35)} {n(y+s*.65)} {n(x+sign*s*.75)} {n(y-s*.85)}','none',c,.38)
  for i in range(6):
   a=i*pi/11;xx=x+sign*s*(.48+.5*sin(a));yy=y+s*(.82-i*.30)
   out+=f'<g transform="rotate({sign*(30+i*8)} {n(xx)} {n(yy)})">'+ellipse(xx,yy,s*.14,s*.27,c)+'</g>'
 return out

def shield(d,c):return path(d,c)
def crest_al():
 out=wreath(18,19,4.1)+star(18,11,1.3,K)+star(18,11,1.05,W)
 out+=path('M14.8 14H21.2V21Q18 24 14.8 21Z',L)
 out+=rect(14.8,14,6.4,2.5,W)+star(16,15.1,.65,B)+star(18,15.1,.65,B)+star(20,15.1,.65,B)
 out+=poly([(15,19),(16,17),(17,19),(18,17),(19,19),(20,17),(21,19),(21,20),(15,20)],R)
 out+=path('M15 21Q16 20 17 21T19 21T21 21','none',W,.5)
 out+=path('M14 24Q18 25 22 24L22 25Q18 26 14 25Z',G)
 return out

def crest_ce():
 out=rect(15.7,11.6,4.6,1.7,Y)
 for xx in [16,17.3,18.6,19.9]:out+=rect(xx,11.1,.55,.8,Y)
 out+=path('M14.5 14Q18 13 21.5 14L21 17Q22 22 18 25Q14 22 15 17Z',K)
 out+=path('M15.3 14.6Q18 13.8 20.7 14.6L20.2 17Q21 21.8 18 24Q15 21.8 15.8 17Z',W)
 out+=path('M16 15.4H20L19.6 17Q20.5 21 18 22.8Q15.5 21 16.4 17Z',G)
 out+=circle(18,18.5,2,L)+poly([(16.4,19.2),(17.4,17.8),(18.2,19),(19,17.9),(19.7,19.2)],Y)
 out+=path('M16.5 20.2Q18 19.4 19.5 20.2','none',W,.4)+star(18,15.4,.65,W)
 return out

def crest_rj():
 out=wreath(18,18.5,5.0,'#628C4C')+star(18,10.9,1.1,Y)
 out+=ellipse(18,18.2,3.9,6,Y)+ellipse(18,18.2,3.4,5.5,L)
 out+=poly([(15.1,18.2),(16.5,16.5),(17.3,17.4),(19,14.9),(20.6,18.2)],K)
 out+=poly([(15.1,19.2),(17,18.1),(20.8,18.8),(20.5,20.3),(15.5,20.3)],G)
 out+=path('M15.3 20.4Q16.6 19.8 18 20.4T20.7 20.4','none',W,.5)
 out+=circle(18,22,1.5,W)+circle(18,22,1.05,B)+star(18,22,.8,W)
 out+=path('M13 25Q18 27 23 25L22.4 26.5Q18 28 13.6 26.5Z',Y)
 return out

def crest_rn():
 out=path('M12.8 12.5H23.2V23.8Q18 27 12.8 23.8Z',Y)+wreath(18,19.5,4.1,G)
 out+=path('M14.8 15H21.2V22Q18 24.7 14.8 22Z',L)
 out+=poly([(14.8,20),(17,18.8),(19,19.4),(21.2,19),(21.2,22),(18,23.6),(14.8,22)],G)
 out+=rect(16.4,15.7,3.2,2.3,W)+rect(16.1,15.3,.8,1,W)+rect(17.6,15.3,.8,1,W)+rect(19.1,15.3,.8,1,W)
 out+=rect(17.7,16.7,.6,1.3,K)+poly([(17.9,18.5),(17.9,20.3),(19.4,20.3)],W)
 out+=path('M17.3 20.6H20.1L19.5 21.3H17.7Z',K)+star(18,13.4,.85,W)
 return out

def crest_rs():
 out=ellipse(18,18,5,6.1,W)
 for sign in [-1,1]:
  for i in range(3):
   x=18+sign*(3+i*.4)
   out+=path(f'M18 23L{n(x)} 13','none',Y,.35)+poly([(x,13),(x+sign*1.6,14.5),(x,16)],G if i%2==0 else R)
 out+=wreath(18,20,3.2,G)+ellipse(18,17.8,2.6,3.7,Y)+ellipse(18,17.8,2.05,3.15,W)
 out+=rect(16.9,17,2.2,2.4,L)+rect(17.7,17.7,.6,2.4,K)+poly([(16.8,17),(18,15.8),(19.2,17)],R)
 out+=path('M14.2 23.4Q18 24.4 21.8 23.4L21.3 24.4Q18 25.2 14.7 24.4Z',Y)
 return out

def crest_sc():
 out=wreath(18,20,4.3,G)+star(18,13,2.5,W)
 # Eagle silhouette with spread wings; anchor, shield, and crossed tools.
 out+=path('M18 14L16.5 16L13 15L14.5 18L16.6 19L16.2 22L18 20.8L19.8 22L19.4 19L21.5 18L23 15L19.5 16Z','#836340')
 out+=circle(18,15,1.1,K)+poly([(18.6,14.9),(20,15.3),(18.6,15.7)],Y)
 out+=path('M18 20V24M16 23Q18 25 20 23','none',K,.5)
 out+=path('M15 24L21 18M15 18L21 24','none',Y,.55)
 out+=path('M16.5 17.5H19.5V20L18 21.3L16.5 20Z',W)+rect(17.7,17.5,.6,3,R)
 out+=path('M13 25Q18 26.3 23 25L22.3 26.4Q18 27.4 13.7 26.4Z',R)
 return out
F={}
F['AC']=rect(0,5,36,26,G)+poly([(0,5),(36,5),(0,31)],Y)+star(5.5,10.5,2.6,R)
F['AL']=rect(0,5,12,26,R)+rect(12,5,12,26,W)+rect(24,5,12,26,L)+crest_al()
# Amapá: blue/yellow fields, green chevron band, black-white separators, Fort São José.
F['AP']=stripes([D,Y])+poly([(0,5),(9,13),(36,13),(36,23),(9,23),(0,31)],K)+poly([(0,5.8),(9.4,13.7),(36,13.7),(36,22.3),(9.4,22.3),(0,30.2)],W)+poly([(0,6.6),(9.8,14.4),(36,14.4),(36,21.6),(9.8,21.6),(0,29.4)],G)
F['AP']+=poly([(5.6,14.6),(6.4,16.7),(8.5,17.5),(6.4,18.3),(5.6,20.4),(4.8,18.3),(2.7,17.5),(4.8,16.7)],W)+poly([(5.6,15.5),(6.1,17),(7.6,17.5),(6.1,18),(5.6,19.5),(5.1,18),(3.6,17.5),(5.1,17)],K)+poly([(5.6,16),(7.1,17.5),(5.6,19),(4.1,17.5)],G)
F['AM']=stripes([W,R,W])+rect(0,5,15,26/3,D)
# 61 small municipal stars plus the larger central star, following reference rows.
gaps={2:{3,4,5,6},3:{4,5},4:{3,4,6}}
F['AM']+=''.join(star(.8+1.45*j,5.75+1.17*i,.24) for i in range(7) for j in range(10) if j not in gaps.get(i,set()))+star(7.75,9.15,1.05)
F['BA']=stripes([W,R,W,R])+rect(0,5,13,13,D)+poly([(6.5,7),(11.3,15.8),(1.7,15.8)],W)
F['CE']=rect(0,5,36,26,G)+diamond(Y)+circle(18,18,7.6,W)+crest_ce()
# DF Brasília cross: four arrow-ended arms and an open central diamond.
F['DF']=rect(0,5,36,26,W)+rect(11.3,11.3,13.4,13.4,G)
arm=poly([(17.1,16.8),(17.1,13.6),(16.2,13.6),(18,11.7),(19.8,13.6),(18.9,13.6),(18.9,16.8)],Y)
F['DF']+=''.join(f'<g transform="rotate({a} 18 18)">{arm}</g>' for a in [0,90,180,270])+diamond(Y,2.8,2.8)+diamond(G,1.45,1.45)
F['ES']=stripes([L,W,'#F4ABCA'])+lettering('TRABALHA E CONFIA',18,16.8,1.7,L)
F['GO']=stripes([G,Y]*4)+rect(0,5,15,13,B)+southern_cross(7.5,11.3,5)
F['MA']=stripes([R,W,K,W,R,W,K,W,R])+rect(0,5,13,13,D)+star(6.5,11.5,4.1)
F['MT']=rect(0,5,36,26,D)+diamond(W)+circle(18,18,6.2,G)+star(18,18,5.8,Y)
F['MS']=rect(0,5,36,26,L)+poly([(0,5),(20,5),(0,31)],W)+poly([(0,5),(15.5,5),(0,24)],G)+star(30,25.7,3,Y)
F['MG']=rect(0,5,36,26,W)+poly([(18,11),(25,23),(11,23)],R)
F['MG']+=lettering('LIBERTAS',11.4,13.8,1.3,K,-60)+lettering('QUAE SERA',24.6,14,1.3,K,60)+lettering('TAMEN',18,25,1.3,K)
F['PA']=rect(0,5,36,26,R)+poly([(0,5),(7.5,5),(36,25.5),(36,31),(28.5,31),(0,10.5)],W)+star(18,18,3.3,L)
F['PB']=rect(0,5,36,26,R)+rect(0,5,12,26,K)+lettering('NEGO',24,16.6,3.1,W)
F['PR']=rect(0,5,36,26,G)+poly([(0,5),(9,5),(36,24.5),(36,31),(27,31),(0,11.5)],W)+wreath(18,19.5,5,G)+circle(18,18,5.6,B)+southern_cross(18,18.3,3.4)
F['PR']+=path('M12.6 15.6Q18 14.3 23.4 16L23.4 18.2Q18 16.5 12.6 17.8Z',W)+lettering('PARANA',18,15.7,1.25,G)
F['PE']=stripes([B,B,W])
for r,c in [(10.1,R),(9.2,Y),(8.3,G)]:F['PE']+=path(f'M{n(18-r)} 22.333A{r} {r} 0 0 1 {n(18+r)} 22.333','none',c,.9)
F['PE']+=star(18,8,1.15,Y)+star(18,18.4,2.15,Y,16,.75)+circle(18,18.4,1.3,Y)+cross(18,26.7,3.2,R)
F['PI']=stripes([G,Y]*6+[G])+rect(0,5,14,10,D)+star(7,9.2,3)+lettering('13 DE MARCO DE 1823',7,13.2,.65,W)
F['RJ']=rect(0,5,36,26,W)+rect(18,5,18,13,L)+rect(0,18,18,13,L)+crest_rj()
F['RN']=stripes([G,W])+crest_rn()
F['RS']=rect(0,5,36,26,R)+poly([(0,5),(36,5),(0,18)],G)+poly([(0,31),(36,18),(36,31)],Y)+crest_rs()
F['RO']=stripes([D,Y])+poly([(18,18),(36,31),(0,31)],G)+star(18,16.7,4.9)
F['RR']=rect(0,5,36,26,W)+poly([(0,5),(29,5),(0,19.5)],L)+poly([(7,31),(36,16.5),(36,31)],G)+star(18,18,5.9,Y)+rect(0,27.9,36,.65,R)
F['SC']=stripes([R,W,R])+diamond('#8BC34A',14.8,10.5)+crest_sc()
F['SP']=stripes([K,W]*6+[K])+rect(0,5,14,10,R)+circle(7,10,3.4,W)
F['SP']+=path('M5 7.9L6.1 8.1L6.6 7.4L7.6 8.3L9.1 8.2L9.8 9.3L8.9 10.4L8.2 10.8L8 12.1L7.1 13L6.5 11.3L5.7 10.7L5.6 9.7L4.5 9Z',B)
F['SP']+=''.join(star(x,y,.8,Y) for x,y in [(1.8,6.8),(12.2,6.8),(1.8,13.2),(12.2,13.2)])
F['SE']=stripes([G,Y,G,Y])+rect(0,5,14,13,D)+star(7,11.5,2.1)+''.join(star(x,y,1) for x,y in [(2.4,7.3),(11.6,7.3),(2.4,15.7),(11.6,15.7)])
F['TO']=rect(0,5,36,26,W)+poly([(0,5),(25,5),(0,22)],B)+poly([(11,31),(36,14),(36,31)],Y)+star(18,18,5,Y,16,.35)+circle(18,18,2,Y)
ROWS=[('AC','Acre','norte'),('AL','Alagoas','nordeste'),('AP','Amapá','norte'),('AM','Amazonas','norte'),('BA','Bahia','nordeste'),('CE','Ceará','nordeste'),('DF','Distrito Federal','centro-oeste'),('ES','Espírito Santo','sudeste'),('GO','Goiás','centro-oeste'),('MA','Maranhão','nordeste'),('MT','Mato Grosso','centro-oeste'),('MS','Mato Grosso do Sul','centro-oeste'),('MG','Minas Gerais','sudeste'),('PA','Pará','norte'),('PB','Paraíba','nordeste'),('PR','Paraná','sul'),('PE','Pernambuco','nordeste'),('PI','Piauí','nordeste'),('RJ','Rio de Janeiro','sudeste'),('RN','Rio Grande do Norte','nordeste'),('RS','Rio Grande do Sul','sul'),('RO','Rondônia','norte'),('RR','Roraima','norte'),('SC','Santa Catarina','sul'),('SP','São Paulo','sudeste'),('SE','Sergipe','nordeste'),('TO','Tocantins','norte')]
NOTES={'AL':'Crest redrawn as star, shield, hills, water, wreath and ribbon; micro-detail omitted.','AP':'Fort reduced to a four-point plan; separator bands thickened for small sizes.','AM':'61 small stars plus the central star retained; spacing normalized; tiny stars read as texture below 36px.','CE':'Crest retains crown, shield and landscape; tiny heraldic details omitted.','DF':'Cross arms and arrow tips redrawn; open diamond retained.','ES':'Motto retained in geometric path lettering, straightened; very small text is decorative at 18px.','MG':'Motto retained around triangle in geometric path lettering; not legible at smallest sizes.','PB':'NEGO retained as original geometric path lettering.','PR':'Wreath and Southern Cross retained; curved band flattened and lettering simplified.','PE':'Rainbow, star, sun and cross retained; sun reduced to sixteen rays.','PI':'2005 date retained as geometric lettering, without cedilla; decorative at small sizes.','RJ':'Crest retains star, wreath, landscape, medallion and ribbon; inscriptions omitted.','RN':'Crest retains shield, vegetation, fort and boat; inscriptions omitted.','RS':'Crest retains white oval, flags, shield, liberty cap, wreath and ribbon; inscriptions omitted.','SC':'Crest retains eagle, shield, anchor, crossed tools and wreath; inscriptions omitted.','SP':'Brazil map hand-redrawn as an approximate silhouette; four canton stars retained.','TO':'Sun uses sixteen broad rays; official fields adapted to shared proportions.'}
SOURCES={'AC':'Bandeira_do_Acre.svg','AL':'Bandeira_de_Alagoas.svg','AP':'Bandeira_do_Amapá.svg','AM':'Bandeira_do_Amazonas.svg','BA':'Bandeira_da_Bahia.svg','CE':'Bandeira_do_Ceará.svg','DF':'Bandeira_do_Distrito_Federal_(Brasil).svg','ES':'Bandeira_do_Espírito_Santo.svg','GO':'Flag_of_Goiás.svg','MA':'Bandeira_do_Maranhão.svg','MT':'Bandeira_de_Mato_Grosso.svg','MS':'Bandeira_de_Mato_Grosso_do_Sul.svg','MG':'Bandeira_de_Minas_Gerais.svg','PA':'Bandeira_do_Pará.svg','PB':'Bandeira_da_Paraíba.svg','PR':'Bandeira_do_Paraná.svg','PE':'Bandeira_de_Pernambuco.svg','PI':'Bandeira_do_Piauí.svg','RJ':'Bandeira_do_estado_do_Rio_de_Janeiro.svg','RN':'Bandeira_do_Rio_Grande_do_Norte.svg','RS':'Bandeira_do_Rio_Grande_do_Sul.svg','RO':'Bandeira_de_Rondônia.svg','RR':'Bandeira_de_Roraima.svg','SC':'Bandeira_de_Santa_Catarina.svg','SP':'Bandeira_do_estado_de_São_Paulo.svg','SE':'Bandeira_de_Sergipe.svg','TO':'Bandeira_do_Tocantins.svg'}
metadata=[]
for code,name,region in ROWS:
 stem='br-'+code.lower();notes=NOTES.get(code,'Main fields and symbols retained; proportions normalized to emoji canvas.')
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" role="img" aria-labelledby="{stem}-title {stem}-desc">
<title id="{stem}-title">{html.escape(name)} state flag</title>
<desc id="{stem}-desc">Stylized Brazilian federative-unit flag. {html.escape(notes)}</desc>
<defs><clipPath id="{stem}-clip"><rect y="5" width="36" height="26" rx="4"/></clipPath></defs>
<g clip-path="url(#{stem}-clip)">{F[code]}</g>
</svg>\n'''
 (ROOT/'svg').mkdir(exist_ok=True);(ROOT/'svg'/f'{stem}.svg').write_text(svg)
 metadata.append(dict(code=code,iso='BR-'+code,name=name,region=region,svg=f'svg/{stem}.svg',png={str(s):f'png/{s}/{stem}.png' for s in [36,72,144,512]},reference='https://commons.wikimedia.org/wiki/File:'+SOURCES[code],simplification=notes))
(ROOT/'metadata').mkdir(exist_ok=True)
(ROOT/'metadata'/'states.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
(ROOT/'metadata'/'states.ts').write_text('// Relative asset paths are package-root-relative.\nexport const brazilStates = '+json.dumps({x['code']:x for x in metadata},ensure_ascii=False,indent=2)+' as const;\nexport type BrazilStateCode = keyof typeof brazilStates;\n')
(ROOT/'react-native').mkdir(exist_ok=True)
(ROOT/'react-native'/'StateFlag.tsx').write_text('''import React from 'react';
import { Image, type ImageStyle, type StyleProp } from 'react-native';
import type { BrazilStateCode } from '../metadata/states';
const assets = {
'''+''.join(f"  {code}: require('../png/144/br-{code.lower()}.png'),\n" for code,_,_ in ROWS)+'''} as const;
export function StateFlag({ state, size = 24, style }: {
  state: BrazilStateCode; size?: number; style?: StyleProp<ImageStyle>;
}) {
  return <Image source={assets[state]} accessibilityLabel={`Bandeira: ${state}`}
    resizeMode="contain" style={[{ width: size, height: size }, style]} />;
}
''')
print(f'Built {len(metadata)} SVG masters and metadata.')
