import os

def w(path, html):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

STYLE = """<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--preto:#0f0f0f;--branco:#fff;--cf:#f5f5f3;--cb:#e2e2e0;--ct:#6b6b6b;--verde:#1a7a4a;--vm:#c0392b}
body{font-family:'Inter',sans-serif;background:var(--cf);color:var(--preto)}
header{background:#fff;border-bottom:1px solid var(--cb);padding:0 24px;height:60px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}
.logo{font-family:'DM Serif Display',serif;font-size:22px;color:var(--preto);text-decoration:none}
.logo span{color:var(--verde)}
nav{display:flex;gap:24px}
nav a{font-size:14px;color:var(--ct);text-decoration:none;font-weight:500}
nav a:hover{color:var(--preto)}
@media(max-width:560px){nav{display:none}}
.ad{background:#fff;border-bottom:1px solid var(--cb);display:flex;align-items:center;justify-content:center;padding:12px 16px;min-height:110px}
.ad-box{background:#f0f0ee;border:2px dashed #ccc;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#999;font-size:12px;font-weight:600;text-transform:uppercase;gap:4px;width:100%;max-width:728px;height:90px}
.ad-sm{background:#f0f0ee;border:2px dashed #ccc;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#999;font-size:12px;font-weight:600;text-transform:uppercase;gap:4px;width:100%;max-width:336px;height:280px}
.ad-label{font-size:10px;color:#bbb}
.hero{background:var(--preto);color:#fff;padding:48px 24px 72px;text-align:center}
.ey{font-size:12px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:var(--verde);margin-bottom:12px}
.hero h1{font-family:'DM Serif Display',serif;font-size:clamp(24px,4vw,44px);line-height:1.1;margin-bottom:12px;max-width:600px;margin-left:auto;margin-right:auto}
.hero p{font-size:15px;color:#aaa;max-width:440px;margin:0 auto;line-height:1.6}
.badge{display:inline-block;background:var(--verde);color:#fff;font-size:11px;font-weight:600;padding:4px 10px;border-radius:20px;margin-bottom:12px}
.wrap{max-width:820px;margin:-40px auto 0;padding:0 16px 64px}
.card{background:#fff;border-radius:16px;box-shadow:0 4px 24px rgba(0,0,0,0.08);overflow:hidden;margin-bottom:20px}
.cb{padding:28px}
.gi{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:20px}
@media(max-width:560px){.gi{grid-template-columns:1fr}}
.campo label{display:block;font-size:12px;font-weight:600;letter-spacing:0.5px;text-transform:uppercase;color:var(--ct);margin-bottom:7px}
.campo input,.campo select{width:100%;padding:13px 15px;border:1.5px solid var(--cb);border-radius:10px;font-size:15px;font-family:'Inter',sans-serif;color:var(--preto);background:#fff;-webkit-appearance:none}
.campo input:focus,.campo select:focus{outline:none;border-color:var(--verde)}
.btn{width:100%;padding:15px;background:var(--verde);color:#fff;border:none;border-radius:10px;font-size:16px;font-weight:600;font-family:'Inter',sans-serif;cursor:pointer}
.btn:hover{background:#155f39}
.res{display:none;border-top:1px solid var(--cb)}
.res.v{display:block}
.adm{padding:20px 28px;background:var(--cf);border-bottom:1px solid var(--cb);display:flex;justify-content:center}
.ri{padding:28px;background:var(--cf)}
.rt{font-size:13px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:var(--ct);margin-bottom:18px}
.rg{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:24px}
@media(max-width:560px){.rg{grid-template-columns:1fr}}
.ri-item{background:#fff;border-radius:12px;padding:18px;border:1px solid var(--cb)}
.ri-item.d{background:var(--verde);border-color:var(--verde)}
.ri-item.d .rl{color:rgba(255,255,255,0.7)}
.ri-item.d .rv{color:#fff}
.rl{font-size:11px;font-weight:600;letter-spacing:0.5px;text-transform:uppercase;color:var(--ct);margin-bottom:5px}
.rv{font-size:22px;font-weight:700;color:var(--preto)}
.tt{font-size:13px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:var(--ct);margin-bottom:10px}
.tw{border-radius:10px;overflow:hidden;border:1px solid var(--cb)}
table{width:100%;border-collapse:collapse;font-size:13px}
thead tr{background:var(--preto);color:#fff}
thead th{padding:11px 14px;text-align:left;font-weight:600;font-size:11px;letter-spacing:0.5px;text-transform:uppercase}
tbody tr{border-bottom:1px solid var(--cb);background:#fff}
tbody tr:hover{background:var(--cf)}
tbody tr:last-child{border-bottom:none}
tbody td{padding:10px 14px}
td.j{color:var(--vm)}
.adr{max-width:820px;margin:0 auto;padding:0 16px;display:flex;justify-content:center;margin-bottom:48px}
footer{background:var(--preto);color:#666;text-align:center;padding:28px 24px;font-size:13px}
footer strong{color:#fff}
.ic{max-width:820px;margin:20px auto 0;padding:0 16px}
.ic-card{background:#fff;border-radius:12px;padding:24px;border:1px solid var(--cb);margin-bottom:12px}
.ic-card h3{font-size:14px;font-weight:600;margin-bottom:8px}
.ic-card p{font-size:13px;color:var(--ct);line-height:1.6}
.bc{max-width:820px;margin:0 auto;padding:0 16px}
.bread{font-size:13px;color:var(--ct);margin:16px 0 0}
.bread a{color:var(--verde);text-decoration:none}
.sg{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:36px}
@media(max-width:560px){.sg{grid-template-columns:1fr 1fr}}
.sl{background:#fff;border:1px solid var(--cb);border-radius:8px;padding:12px;text-decoration:none;color:var(--preto);font-size:13px;font-weight:500;text-align:center;transition:border-color 0.2s}
.sl:hover{border-color:var(--verde);color:var(--verde)}
.sp{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0}
@media(max-width:560px){.sp{grid-template-columns:1fr 1fr}}
.sp-item{background:var(--cf);border-radius:8px;padding:14px}
.sp-l{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px;color:var(--ct);margin-bottom:4px}
.sp-v{font-size:16px;font-weight:700}
.faq{max-width:820px;margin:0 auto 20px;padding:0 16px}
.faq-i{background:#fff;border-radius:10px;padding:20px;border:1px solid var(--cb);margin-bottom:10px}
.faq-i h3{font-size:14px;font-weight:600;margin-bottom:8px}
.faq-i p{font-size:13px;color:var(--ct);line-height:1.6}
</style>"""

JS = """<script>
function pm(s){return parseFloat(s.replace(/[R$\\s.]/g,'').replace(',','.'))||0}
function fm(v){return v.toLocaleString('pt-BR',{style:'currency',currency:'BRL'})}
function calc(){
  const vl=pm(document.getElementById('vl').value);
  const en=pm(document.getElementById('en').value);
  const pr=parseInt(document.getElementById('pr').value);
  const tx=parseFloat(document.getElementById('tx').value.replace(',','.').replace('%','').trim())/100;
  if(!vl||!tx||vl<=en){alert('Preencha todos os campos.');return}
  const p=vl-en;
  const parc=p*(tx*Math.pow(1+tx,pr))/(Math.pow(1+tx,pr)-1);
  const tot=parc*pr;
  document.getElementById('rp').textContent=fm(parc);
  document.getElementById('rt').textContent=fm(tot+en);
  document.getElementById('rj').textContent=fm(tot-p);
  let s=p,l='';
  for(let i=1;i<=pr;i++){const j=s*tx;const a=parc-j;s-=a;l+=`<tr><td>${i}</td><td>${fm(parc)}</td><td class="j">${fm(j)}</td><td>${fm(a)}</td><td>${fm(Math.max(s,0))}</td></tr>`;}
  document.getElementById('tb').innerHTML=l;
  const r=document.getElementById('res');r.classList.add('v');r.scrollIntoView({behavior:'smooth',block:'start'});
}
['vl','en'].forEach(id=>{
  const el=document.getElementById(id);
  if(el)el.addEventListener('input',function(){
    let v=this.value.replace(/\\D/g,'');
    if(!v){this.value='';return}
    this.value=(parseInt(v)/100).toLocaleString('pt-BR',{style:'currency',currency:'BRL'});
  });
});
</script>"""

HDR = """<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=DM+Serif+Display&display=swap" rel="stylesheet"/>"""

def nav(ativo=''):
    return f"""<header>
<a href="/" class="logo">Simul<span>Auto</span></a>
<nav>
<a href="/carros"{'style="color:var(--verde);font-weight:600"' if ativo=='carros' else ''}>Carros</a>
<a href="/motos">Motos</a>
<a href="/comparar-bancos"{'style="color:var(--verde);font-weight:600"' if ativo=='bancos' else ''}>Comparar Bancos</a>
</nav>
</header>"""

def ad_topo():
    return '<div class="ad"><div class="ad-box">📢 AdSense 728×90<span class="ad-label">Leaderboard</span></div></div>'

def ad_meio():
    return '<div class="adm"><div class="ad-sm">📢 AdSense 336×280<span class="ad-label">Rectangle • Maior CTR</span></div></div>'

def ad_rod():
    return '<div class="adr"><div class="ad-box">📢 AdSense 728×90<span class="ad-label">Leaderboard Rodapé</span></div></div>'

def footer():
    return '<footer><strong>SimulAuto</strong> — Simulador de Financiamento de Veículos<br/>Simulações são estimativas educativas. Consulte a instituição financeira.</footer>'

def calc_form(vl='', en='', tx='1.99', label='Calcular financiamento'):
    vl_v = f'value="{vl}"' if vl else 'placeholder="R$ 80.000"'
    en_v = f'value="{en}"' if en else 'placeholder="R$ 16.000"'
    return f"""<div class="cb">
<div class="gi">
<div class="campo"><label>Valor do veículo</label><input type="text" id="vl" {vl_v} inputmode="numeric"/></div>
<div class="campo"><label>Valor de entrada</label><input type="text" id="en" {en_v} inputmode="numeric"/></div>
<div class="campo"><label>Prazo</label><select id="pr">
<option value="12">12 meses</option><option value="24">24 meses</option>
<option value="36">36 meses</option><option value="48" selected>48 meses</option>
<option value="60">60 meses</option></select></div>
<div class="campo"><label>Taxa mensal</label><input type="text" id="tx" value="{tx}%" inputmode="decimal"/></div>
</div>
<button class="btn" onclick="calc()">{label}</button>
</div>
<div class="res" id="res">
{ad_meio()}
<div class="ri">
<p class="rt">Resultado da simulação</p>
<div class="rg">
<div class="ri-item d"><p class="rl">Parcela mensal</p><p class="rv" id="rp">—</p></div>
<div class="ri-item"><p class="rl">Total pago</p><p class="rv" id="rt">—</p></div>
<div class="ri-item"><p class="rl">Total em juros</p><p class="rv" id="rj">—</p></div>
</div>
<p class="tt">Evolução mês a mês</p>
<div class="tw"><table>
<thead><tr><th>Mês</th><th>Parcela</th><th>Juros</th><th>Amortização</th><th>Saldo devedor</th></tr></thead>
<tbody id="tb"></tbody>
</table></div>
</div>
</div>"""

# Modelos
modelos = [
    ("fiat-strada","Fiat Strada",125000,1.99,142903),
    ("volkswagen-polo","Volkswagen Polo",92000,1.89,122677),
    ("fiat-argo","Fiat Argo",88000,1.89,102639),
    ("volkswagen-t-cross","Volkswagen T-Cross",115000,1.99,92837),
    ("hyundai-hb20","Hyundai HB20",88990,1.89,85035),
    ("chevrolet-onix","Chevrolet Onix",101790,1.89,79895),
    ("hyundai-creta","Hyundai Creta",129990,1.99,76000),
    ("fiat-mobi","Fiat Mobi",82560,1.79,73013),
    ("jeep-compass","Jeep Compass",174990,2.09,68000),
    ("honda-hrv","Honda HR-V",149900,1.99,65000),
    ("chevrolet-tracker","Chevrolet Tracker",132990,1.99,63000),
    ("volkswagen-saveiro","Volkswagen Saveiro",95000,1.89,67753),
    ("fiat-toro","Fiat Toro",165000,2.09,52133),
    ("toyota-hilux","Toyota Hilux",279990,2.19,49732),
    ("chevrolet-onix-plus","Chevrolet Onix Plus",112490,1.89,52959),
    ("volkswagen-virtus","Volkswagen Virtus",108000,1.89,36980),
    ("hyundai-hb20s","Hyundai HB20S",98990,1.89,36948),
    ("toyota-corolla","Toyota Corolla",179990,1.99,33252),
    ("ford-ranger","Ford Ranger",259990,2.19,34063),
    ("chevrolet-s10","Chevrolet S10",219990,2.19,31458),
    ("renault-kwid","Renault Kwid",79990,1.79,57938),
    ("toyota-corolla-cross","Toyota Corolla Cross",179990,2.09,45000),
    ("jeep-renegade","Jeep Renegade",134990,1.99,42000),
    ("nissan-kicks","Nissan Kicks",134990,1.99,38000),
    ("volkswagen-tera","Volkswagen Tera",98000,1.89,35000),
    ("fiat-fastback","Fiat Fastback",139990,1.99,32000),
    ("honda-civic","Honda Civic",179990,2.09,28000),
    ("toyota-yaris","Toyota Yaris",109990,1.99,25000),
    ("chevrolet-spin","Chevrolet Spin",125990,1.99,22000),
    ("fiat-pulse","Fiat Pulse",109990,1.99,48000),
    ("volkswagen-nivus","Volkswagen Nivus",122990,1.99,44000),
    ("jeep-commander","Jeep Commander",239990,2.19,28000),
    ("toyota-sw4","Toyota SW4",369990,2.29,18000),
    ("honda-wrv","Honda WR-V",139990,1.99,32000),
    ("fiat-cronos","Fiat Cronos",109990,1.89,28000),
    ("peugeot-208","Peugeot 208",109990,1.99,22000),
    ("renault-duster","Renault Duster",139990,1.99,35000),
    ("ford-territory","Ford Territory",174990,2.09,18000),
    ("byd-dolphin-mini","BYD Dolphin Mini",120000,1.89,32488),
    ("caoa-chery-tiggo7","Caoa Chery Tiggo 7",149990,2.09,38440),
    ("haval-h6","GWM Haval H6",199990,2.09,22000),
    ("hyundai-tucson","Hyundai Tucson",224990,2.09,20000),
    ("kia-sportage","Kia Sportage",219990,2.09,18000),
    ("volkswagen-amarok","Volkswagen Amarok",329990,2.29,15000),
    ("chevrolet-montana","Chevrolet Montana",129990,1.99,25000),
    ("ram-rampage","RAM Rampage",219990,2.19,20000),
    ("mitsubishi-eclipse-cross","Mitsubishi Eclipse Cross",179990,2.09,15000),
    ("honda-hr-v-2025","Honda HR-V 2025",154900,1.99,28000),
    ("fiat-doblo","Fiat Doblo",145990,1.99,15000),
    ("chevrolet-s10-2025","Chevrolet S10 2025",229990,2.19,12000),
]

for slug,nome,preco,taxa,emp in modelos:
    en = int(preco*0.2)
    pf = f"R$ {preco:,.0f}".replace(",",".")
    ef = f"R$ {en:,.0f}".replace(",",".")
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Financiamento {nome} 2025 — Simule Parcelas | SimulAuto</title>
<meta name="description" content="Simule o financiamento do {nome} 2025. Taxa média {taxa}% a.m. Calcule parcelas gratuitamente."/>
<link rel="canonical" href="https://simulauto.com.br/financiamento/{slug}"/>
{HDR}{STYLE}</head>
<body>
{nav('carros')}{ad_topo()}
<div class="bc"><p class="bread"><a href="/">SimulAuto</a> › <a href="/carros">Carros</a> › {nome}</p></div>
<section class="hero">
<span class="badge">{emp:,} emplacamentos em 2025</span>
<p class="ey">Simulador Gratuito</p>
<h1>Financiamento {nome} 2025</h1>
<p>Calcule parcelas com taxa média de {taxa}% a.m. Sem cadastro.</p>
</section>
<div class="wrap"><div class="card">{calc_form(pf,ef,str(taxa),f"Calcular financiamento do {nome}")}</div></div>
<div class="ic">
<div class="ic-card">
<h3>Financiamento {nome} 2025</h3>
<p>O {nome} teve {emp:,} emplacamentos em 2025. Preço médio: {pf}. Com entrada de 20% ({ef}), taxa de {taxa}% a.m.</p>
<div class="sp">
<div class="sp-item"><p class="sp-l">Preço médio</p><p class="sp-v">{pf}</p></div>
<div class="sp-item"><p class="sp-l">Entrada 20%</p><p class="sp-v">{ef}</p></div>
<div class="sp-item"><p class="sp-l">Taxa média</p><p class="sp-v">{taxa}% a.m.</p></div>
<div class="sp-item"><p class="sp-l">Prazo máx.</p><p class="sp-v">60 meses</p></div>
<div class="sp-item"><p class="sp-l">Emplacamentos</p><p class="sp-v">{emp:,}</p></div>
<div class="sp-item"><p class="sp-l">Sistema</p><p class="sp-v">Tabela Price</p></div>
</div>
</div>
</div>
<div class="faq">
<div class="faq-i"><h3>Qual a parcela do {nome} em 48 meses?</h3><p>Com {pf}, entrada de 20% e taxa de {taxa}% a.m., a parcela em 48 meses fica entre R$ 1.800 e R$ 3.500. Use o simulador acima para o valor exato.</p></div>
<div class="faq-i"><h3>Qual banco tem a menor taxa para o {nome}?</h3><p>BTG Pactual (1,00% a.m.), Caixa (1,49% a.m.) e Santander (1,49% a.m.) lideram em 2025. Veja <a href="/comparar-bancos" style="color:var(--verde)">comparação completa</a>.</p></div>
<div class="faq-i"><h3>Posso financiar o {nome} sem entrada?</h3><p>Sim, Itaú, Santander e BB permitem 100% financiado dependendo do seu perfil de crédito.</p></div>
</div>
<div class="bc" style="margin-top:0">
<p class="tt" style="margin-bottom:12px">Simule outros modelos</p>
<div class="sg">
<a href="/financiamento/fiat-strada" class="sl">Fiat Strada</a>
<a href="/financiamento/volkswagen-polo" class="sl">VW Polo</a>
<a href="/financiamento/hyundai-hb20" class="sl">Hyundai HB20</a>
<a href="/financiamento/chevrolet-onix" class="sl">Chevrolet Onix</a>
<a href="/financiamento/jeep-compass" class="sl">Jeep Compass</a>
<a href="/financiamento/toyota-corolla" class="sl">Toyota Corolla</a>
</div>
</div>
{ad_rod()}{footer()}{JS}</body></html>"""
    w(f"financiamento/{slug}.html", html)

print(f"Modelos: {len(modelos)} criados")

# Bancos
bancos = [
    ("itau","Itaú",1.99,"O Itaú oferece financiamento de veículos com taxa média de 1,99% a.m., para carros novos e usados com prazo de até 60 meses."),
    ("bradesco","Bradesco",1.72,"O Bradesco aceita veículos com até 12 anos de fabricação. Taxa média de 1,72% a.m. com prazos flexíveis."),
    ("santander","Santander",1.49,"O Santander oferece taxa a partir de 1,49% a.m. com parcerias diretas em concessionárias e aprovação rápida."),
    ("caixa","Caixa Econômica Federal",1.49,"A Caixa tem taxa a partir de 1,49% a.m., exigindo entrada mínima de 20%. Uma das mais baixas do mercado."),
    ("banco-do-brasil","Banco do Brasil",2.18,"O BB permite financiar até 100% do veículo com carência de até 180 dias. Taxa média de 2,18% a.m."),
    ("btg-pactual","BTG Pactual",1.00,"O BTG Pactual tem a menor taxa do Brasil em 2025: 1,00% a.m. Aprovação 100% digital."),
    ("safra","Banco Safra",1.43,"O Banco Safra oferece 1,43% a.m. para clientes com bom perfil de crédito."),
    ("sicredi","Sicredi",1.43,"O Sicredi oferece condições diferenciadas para cooperados com taxa de 1,43% a.m."),
]

for slug,nome,taxa,desc in bancos:
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Simulador Financiamento Carro {nome} 2025 | SimulAuto</title>
<meta name="description" content="Simule financiamento de carro no {nome}. Taxa média {taxa}% a.m. Calcule parcelas gratuitamente."/>
<link rel="canonical" href="https://simulauto.com.br/financiamento/banco-{slug}"/>
{HDR}{STYLE}</head>
<body>
{nav('bancos')}{ad_topo()}
<div class="bc"><p class="bread"><a href="/">SimulAuto</a> › <a href="/comparar-bancos">Bancos</a> › {nome}</p></div>
<section class="hero">
<span class="badge">Taxa a partir de {taxa}% a.m.</span>
<p class="ey">Simulador por Banco</p>
<h1>Financiamento de Carro — {nome}</h1>
<p>Calcule parcelas com a taxa média do {nome} para 2025.</p>
</section>
<div class="wrap"><div class="card">{calc_form(tx=str(taxa),label=f"Simular no {nome}")}</div></div>
<div class="ic"><div class="ic-card"><h3>{nome} — Financiamento de Veículos</h3><p>{desc}</p></div></div>
<div class="faq">
<div class="faq-i"><h3>Qual a taxa do {nome} para financiamento de carro?</h3><p>A taxa média do {nome} é de {taxa}% ao mês em 2025, segundo dados do Banco Central.</p></div>
<div class="faq-i"><h3>O {nome} financia carro usado?</h3><p>Sim, a maioria dos bancos financia veículos novos e usados. Condições variam conforme o perfil do cliente.</p></div>
</div>
{ad_rod()}{footer()}{JS}</body></html>"""
    w(f"financiamento/banco-{slug}.html", html)

print(f"Bancos: {len(bancos)} criados")

# Páginas por valor
valores = [
    ("30-mil","R$ 30.000",30000),
    ("40-mil","R$ 40.000",40000),
    ("50-mil","R$ 50.000",50000),
    ("60-mil","R$ 60.000",60000),
    ("70-mil","R$ 70.000",70000),
    ("80-mil","R$ 80.000",80000),
    ("90-mil","R$ 90.000",90000),
    ("100-mil","R$ 100.000",100000),
    ("120-mil","R$ 120.000",120000),
    ("150-mil","R$ 150.000",150000),
    ("200-mil","R$ 200.000",200000),
    ("250-mil","R$ 250.000",250000),
]

for slug,vnome,vval in valores:
    en = int(vval*0.2)
    vf = f"R$ {vval:,.0f}".replace(",",".")
    ef = f"R$ {en:,.0f}".replace(",",".")
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Parcela Carro {vnome} Financiado 2025 | SimulAuto</title>
<meta name="description" content="Quanto fica a parcela de um carro de {vnome} financiado? Simule em 24, 36, 48 ou 60 meses. Grátis."/>
<link rel="canonical" href="https://simulauto.com.br/financiamento/parcela-carro-{slug}"/>
{HDR}{STYLE}</head>
<body>
{nav()}{ad_topo()}
<section class="hero">
<p class="ey">Calculadora de Parcelas</p>
<h1>Quanto fica a parcela de um carro de {vnome}?</h1>
<p>Simule em 24, 36, 48 ou 60 meses. Resultado imediato.</p>
</section>
<div class="wrap"><div class="card">{calc_form(vf,ef,label=f"Calcular parcela carro {vnome}")}</div></div>
<div class="faq">
<div class="faq-i"><h3>Qual a parcela de um carro de {vnome} em 48 meses?</h3><p>Com entrada de 20% ({ef}) e taxa de 1,99% a.m., a parcela em 48 meses fica em torno de {("R$ "+str(round((vval-en)*0.0199*(1.0199**48)/((1.0199**48)-1)))).replace(".",",")}. Use o simulador para o valor exato.</p></div>
<div class="faq-i"><h3>Vale a pena financiar um carro de {vnome}?</h3><p>Depende da sua renda e das condições oferecidas. O ideal é que as parcelas não ultrapassem 30% da renda mensal.</p></div>
</div>
{ad_rod()}{footer()}{JS}</body></html>"""
    w(f"financiamento/parcela-carro-{slug}.html", html)

print(f"Valores: {len(valores)} criados")
