
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<title>מעקב הזמנות שירות - ספקים יחידים</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;800&family=Fira+Code:wght@500&display=swap');

:root{
--ink:#1c1f24;
--char:#2a2f38;
--paper:#f4f1ea;
--paper-2:#eae5da;
--ember:#b3241c;
--ember-dark:#8a1b15;
--ember-light:#d9564b;
--amber:#c88a1f;
--line:#d8d1c2;
--ok:#3f7d5a;
--white:#fffdf9;
--shadow: 0 1px 2px rgba(28,31,36,.06), 0 8px 24px rgba(28,31,36,.08);
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:transparent;font-family:'Heebo',Arial,sans-serif;color:var(--ink);}
.app{max-width:1180px;margin:0 auto;padding:18px 18px 60px;}

/* ---- Header / brand ---- */
.brand{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:22px;padding-bottom:16px;border-bottom:2px solid var(--ink);}
.brand-left{display:flex;align-items:center;gap:12px;}
.brand-mark{width:44px;height:44px;border-radius:10px;background:linear-gradient(155deg,var(--ember),var(--ember-dark));display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:var(--shadow);}
.brand-mark svg{width:24px;height:24px;}
.brand-title{font-weight:800;font-size:20px;letter-spacing:-0.2px;line-height:1.15;}
.brand-sub{font-size:12.5px;color:#6b6255;font-weight:500;margin-top:2px;}
.nav{display:flex;gap:6px;background:var(--paper-2);padding:4px;border-radius:11px;}
.nav button{border:none;background:transparent;padding:9px 16px;border-radius:8px;font-family:inherit;font-size:13.5px;font-weight:600;color:#6b6255;cursor:pointer;transition:all .15s;}
.nav button.active{background:var(--ink);color:var(--paper);box-shadow:var(--shadow);}
.nav button:not(.active):hover{color:var(--ink);}

/* ---- Wizard steps indicator ---- */
.steps{display:flex;align-items:center;gap:0;margin-bottom:26px;}
.step{display:flex;align-items:center;gap:10px;flex:1;}
.step-num{width:30px;height:30px;border-radius:50%;border:2px solid var(--line);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;color:#9c9384;background:var(--white);flex-shrink:0;transition:all .2s;}
.step.done .step-num{background:var(--ok);border-color:var(--ok);color:#fff;}
.step.current .step-num{background:var(--ember);border-color:var(--ember);color:#fff;}
.step-label{font-size:13px;font-weight:600;color:#9c9384;}
.step.current .step-label,.step.done .step-label{color:var(--ink);}
.step-line{flex:1;height:2px;background:var(--line);margin:0 -2px;}
.step.done + .step .step-line, .step.done .step-line{background:var(--ok);}

/* ---- Cards / panels ---- */
.panel{background:var(--white);border:1px solid var(--line);border-radius:16px;padding:26px;box-shadow:var(--shadow);}
.panel h2{margin:0 0 4px;font-size:19px;font-weight:800;}
.panel .hint{font-size:13px;color:#847a6b;margin:0 0 20px;}

.field{margin-bottom:18px;}
.field label{display:block;font-size:13px;font-weight:700;color:var(--char);margin-bottom:7px;}
select, input[type=text], input[type=number]{
width:100%;padding:11px 13px;border:1.5px solid var(--line);border-radius:9px;font-family:inherit;font-size:14.5px;background:var(--paper);color:var(--ink);transition:border-color .15s;
}
select:focus, input:focus{outline:none;border-color:var(--ember);background:var(--white);}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:16px;}

.btn{border:none;border-radius:9px;padding:12px 22px;font-family:inherit;font-weight:700;font-size:14px;cursor:pointer;transition:all .15s;display:inline-flex;align-items:center;gap:8px;}
.btn-primary{background:var(--ember);color:#fff;}
.btn-primary:hover{background:var(--ember-dark);}
.btn-primary:disabled{background:#cbbfae;cursor:not-allowed;}
.btn-ghost{background:transparent;color:var(--char);border:1.5px solid var(--line);}
.btn-ghost:hover{border-color:var(--ink);}
.btn-sm{padding:8px 14px;font-size:12.5px;}
.actions-row{display:flex;justify-content:space-between;margin-top:26px;}

/* ---- Supplier grid ---- */
.supplier-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}
.supplier-card{border:1.5px solid var(--line);border-radius:13px;padding:18px 16px;cursor:pointer;background:var(--white);transition:all .15s;text-align:center;}
.supplier-card:hover{border-color:var(--ember-light);transform:translateY(-2px);box-shadow:var(--shadow);}
.supplier-card.selected{border-color:var(--ember);background:#fbeeec;}
.supplier-card .ini{width:42px;height:42px;border-radius:50%;background:var(--paper-2);color:var(--ember-dark);font-weight:800;font-size:15px;display:flex;align-items:center;justify-content:center;margin:0 auto 10px;}
.supplier-card.selected .ini{background:var(--ember);color:#fff;}
.supplier-card .name{font-weight:700;font-size:14px;}
.supplier-card .count{font-size:11.5px;color:#9c9384;margin-top:3px;}

/* ---- Line items ---- */
.line-item{border:1.5px solid var(--line);border-radius:12px;padding:16px;margin-bottom:12px;background:var(--paper);position:relative;}
.line-item .del{position:absolute;top:10px;left:10px;background:none;border:none;color:#9c9384;cursor:pointer;font-size:16px;width:26px;height:26px;border-radius:50%;}
.line-item .del:hover{background:#f0e2df;color:var(--ember);}
.line-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:12px;align-items:end;}
.line-total{font-size:12.5px;color:#847a6b;margin-top:8px;font-weight:600;}
.line-total b{color:var(--ink);font-family:'Fira Code',monospace;}
.add-line-btn{width:100%;border:1.5px dashed var(--line);background:transparent;border-radius:12px;padding:13px;font-family:inherit;font-weight:700;color:#6b6255;cursor:pointer;font-size:13.5px;}
.add-line-btn:hover{border-color:var(--ember);color:var(--ember);}

.summary-bar{display:flex;justify-content:space-between;align-items:center;background:var(--ink);color:var(--paper);border-radius:12px;padding:16px 20px;margin-top:18px;}
.summary-bar .lbl{font-size:12.5px;color:#b8b0a1;font-weight:600;}
.summary-bar .val{font-size:24px;font-weight:800;font-family:'Fira Code',monospace;}

.context-chip{display:inline-flex;align-items:center;gap:6px;background:var(--paper-2);border-radius:20px;padding:6px 14px;font-size:12.5px;font-weight:700;color:var(--char);margin-bottom:18px;}
.context-chip .dot{width:6px;height:6px;border-radius:50%;background:var(--ember);}

/* ---- Confirmation ---- */
.confirm-wrap{text-align:center;padding:40px 20px;}
.confirm-icon{width:64px;height:64px;border-radius:50%;background:var(--ok);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;}
.confirm-icon svg{width:30px;height:30px;stroke:#fff;}

/* ---- Report ---- */
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px;}
.kpi{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:var(--shadow);}
.kpi .lbl{font-size:12px;font-weight:700;color:#847a6b;margin-bottom:6px;}
.kpi .val{font-size:24px;font-weight:800;font-family:'Fira Code',monospace;}
.kpi .val.small{font-size:17px;}

.filters{display:flex;gap:10px;margin-bottom:18px;flex-wrap:wrap;align-items:center;}
.filters select, .filters input{width:auto;padding:8px 12px;font-size:13px;}
.filters .spacer{flex:1;}

.breakdown{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:22px;}
.bd-panel{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:18px 20px;box-shadow:var(--shadow);}
.bd-panel h3{margin:0 0 14px;font-size:14px;font-weight:800;}
.bd-row{display:grid;grid-template-columns:110px 1fr 70px;gap:10px;align-items:center;margin-bottom:9px;font-size:12.5px;}
.bd-row .nm{font-weight:700;color:var(--char);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.bd-bar-bg{height:8px;background:var(--paper-2);border-radius:5px;overflow:hidden;}
.bd-bar{height:100%;background:linear-gradient(90deg,var(--amber),var(--ember));border-radius:5px;}
.bd-row .amt{text-align:left;font-family:'Fira Code',monospace;font-weight:700;color:var(--ink);}

table{width:100%;border-collapse:collapse;background:var(--white);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);}
thead th{background:var(--ink);color:var(--paper);text-align:right;padding:12px 14px;font-size:12px;font-weight:700;}
tbody td{padding:11px 14px;font-size:13px;border-bottom:1px solid var(--paper-2);}
tbody tr:last-child td{border-bottom:none;}
tbody tr:hover{background:var(--paper);}
.tag{display:inline-block;padding:3px 10px;border-radius:20px;background:var(--paper-2);font-size:11.5px;font-weight:700;color:var(--char);}
.amt-cell{font-family:'Fira Code',monospace;font-weight:700;}
.empty-state{text-align:center;padding:50px 20px;color:#9c9384;}
.empty-state svg{width:44px;height:44px;margin-bottom:12px;opacity:.5;}
.table-wrap{max-height:420px;overflow:auto;border-radius:14px;}
.report-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:18px;}
.loading{text-align:center;padding:60px;color:#9c9384;font-size:13px;}
@media (max-width:760px){
.supplier-grid{grid-template-columns:repeat(2,1fr)}
.kpis{grid-template-columns:repeat(2,1fr)}
.breakdown{grid-template-columns:1fr}
.line-grid{grid-template-columns:1fr 1fr}
.row2{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div id="root" class="app"></div>

<script>
/* ============ DATA ============ */
const DISTRICTS = {
"מחוז צפון": ["נוף הגליל","טבריה","עפולה","גליל מרכזי (כרמיאל)","גליל גולן (צפת)"],
"מחוז חוף": ["חיפה","קריות","חדרה","זבולון (עכו)"],
"מחוז מרכז": ["ראשון לציון","רחובות","איילון","פתח תקווה","נתניה","השרון (כפר סבא)"],
"מחוז דן": ["תל אביב-יפו","רמת גן","בני ברק","גבעתיים","חולות (חולון)","הרצליה"],
"מחוז ירושלים": ["בירה (ירושלים - גבעת מרדכי)","האומה (ירושלים - רוממה)","אגוז (ואדי ג'וז)","בית שמש"],
"מחוז דרום": ["באר שבע","אשדוד","אשקלון","נתיבות","דימונה","אילת"],
"מחוז יהודה ושומרון (יו\"ש)": ["שומרון (אריאל)","בנימין (מעלה אדומים)","יהודה (גוש עציון)"]
};

const SUPPLIERS = {
"עמוס גזית": ["כיול, כיול נייד/ניוד והחלפת סוללות לגלאים","טיפול תקופתי / תלת-שנתי בציוד חילוץ וערכות חילוץ","טיפול תקופתי בחליפות חומ\"ס","טיפול חד-שנתי / תקופתי למנ\"פ","תיקון מצלמה תרמית בחו\"ל","חלפים ואביזרים (צינורות, מחברים, וסת לחץ, מתאם, אטמים, סוללות)","טיפול בציוד בטיחות"],
"הידרונוע": ["תיקון וטיפול בפורצי דלתות וערכות חילוץ","חלפים ותחזוקת ציוד (צינור לחץ, שסתום, שמן הידראולי, אטמים, חיבור מהיר, ברז לחץ)","תיקון ציוד מלבן לחיצה","טיפול ותחזוקת כלים לפי דגם"],
"סיג": ["טיפול תקופתי / חצי שנתי (חציון א' / ב')","טיפול תקופתי לבמות / במות מורכבות משאית (כולל נסיעות ושעות עבודה)","שיפוץ, תיקון והחלפת חיישנים / כרטיס אלקטרוני בסל ובבמה","קריאה לשירות / תיקון בתחנה","תיקון רכב / כלי","רכישת חלפים (Water Hose, Limit Switch, Inductive Sensor)"],
"עופר": ["תיקון וטיפול בציוד חילוץ וערכות (הולמטרון, כריות הרמה, חותך מיני)","תיקון תותח / שלט לתותח מפוקד","חלפים ואביזרים (וסת לחץ, מחברים, סוללות, סטרטר, אטמים, שסתומים)","בדיקה וטיפול שנתי במכשיר AFT12"],
"טקפיקס": [],
"רותם": ["טיפול תקופתי","תיקון גלאי"],
"רותם חומ\"ס": ["אספקת סוללות לפנס","טיפול בחליפות טסימקס","תיקון / יחידת מילוי למערכת מילוט וערכת פוני","חלפים ושירותי מעבדה (כרטיס ניתוב, Knucklehead Magnet)"],
"סנפיר": ["טיפול שנתי ובדיקת מדחס"],
"אמפרוקו": ["כיול ותיקון גלאים (כולל גלאי חוקר / מיני ריי)","אספקת פילטרים למיני ריי","בדיקה וכיול ציוד","בדיקה והחלפת סוללה / חיישן"],
"גטרגרופ": ["טיפול שנתי, תקופתי ותיקון מנפ\"ים, מנשאים ומסכות","טיפול שנתי, תקופתי ותיקון מדחסים ובנק אוויר נייח","תיקון והחלפת משקפיים / מגן פנים לקסדות","טיפול ותיקון ערכות קאפס / כיבוי אש","כיול ובדיקת גלאי גז","תיקון ושליחת מצלמה תרמית לחו\"ל","בדיקה תקופתית למערכות נשימה ומסכות פנים","חלפים ואביזרים (סוללות, צינורות לחץ, ממברנות, אבזמים, רצועות)"]
};
const SUPPLIER_NAMES = Object.keys(SUPPLIERS);
const OTHER_LABEL = "אחר (טיפול לא מופיע ברשימה)";

function fmt(n){ return "₪" + Number(n||0).toLocaleString('he-IL',{maximumFractionDigits:0}); }
function uid(){ return Date.now().toString(36)+Math.random().toString(36).slice(2,8); }

/* ============ STATE ============ */
let state = {
view: 'wizard', // wizard | report
step: 1,
district: '', station: '', supplier: '',
lines: [ blankLine() ],
orders: null, // null = loading
saving:false,
justSaved:false,
filters:{district:'', supplier:''}
};
function blankLine(){ return { id:uid(), service:'', customText:'', qty:1, unitCost:'' }; }

async function loadOrders(){
try{
const res = await window.storage.get('orders', true);
state.orders = res ? JSON.parse(res.value) : [];
}catch(e){ state.orders = []; }
render();
}
async function saveOrders(){
try{
await window.storage.set('orders', JSON.stringify(state.orders), true);
}catch(e){ console.error('storage error', e); }
}

/* ============ ICONS ============ */
const ICON_FLAME = `<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2c1 3-2 4-2 7a4 4 0 0 0 8 0c0-1.5-1-2.5-1-2.5.5 2-1 3-1 3-1-4 2-5 2-8-3 1-6 4-6 8.5A6.5 6.5 0 0 0 18.5 17 6.5 6.5 0 0 1 12 22a7 7 0 0 1-7-7c0-5 4-8 7-13z"/></svg>`;
const ICON_CHECK = `<svg viewBox="0 0 24 24" fill="none" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>`;
const ICON_EMPTY = `<svg viewBox="0 0 24 24" fill="none" stroke="#9c9384" stroke-width="1.5"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>`;

/* ============ RENDER ============ */
function render(){
const root = document.getElementById('root');
root.innerHTML = `
${brand()}
${state.view==='wizard' ? wizardView() : reportView()}
`;
attachEvents();
}

function brand(){
return `
<div class="brand">
<div class="brand-left">
<div class="brand-mark">${ICON_FLAME}</div>
<div>
<div class="brand-title">מעקב הזמנות שירות — ספקים יחידים</div>
<div class="brand-sub">7 מחוזות · תיעוד טיפולים ותיקונים · תמונת מצב לניצול הזמנות</div>
</div>
</div>
<div class="nav">
<button data-nav="wizard" class="${state.view==='wizard'?'active':''}">הזמנה חדשה</button>
<button data-nav="report" class="${state.view==='report'?'active':''}">דוח ניצול</button>
</div>
</div>`;
}

function stepsBar(){
const labels = ['מחוז ותחנה','בחירת ספק','פרטי שירות'];
return `<div class="steps">
${labels.map((l,i)=>{
const n=i+1; const cls = n<state.step?'done':(n===state.step?'current':'');
return `<div class="step ${cls}">
${i>0?'<div class="step-line"></div>':''}
<div class="step-num">${n<state.step?'✓':n}</div>
<div class="step-label">${l}</div>
</div>`;
}).join('')}
</div>`;
}

function wizardView(){
if(state.step===1) return stepsBar()+step1();
if(state.step===2) return stepsBar()+step2();
return stepsBar()+step3();
}

function step1(){
const stations = state.district ? DISTRICTS[state.district] : [];
return `
<div class="panel">
<h2>שלב 1 — מחוז ותחנה</h2>
<p class="hint">בחרו את המחוז ואת התחנה האזורית שמזמינה את השירות.</p>
<div class="row2">
<div class="field">
<label>מחוז</label>
<select id="sel-district">
<option value="">בחרו מחוז...</option>
${Object.keys(DISTRICTS).map(d=>`<option value="${d}" ${state.district===d?'selected':''}>${d}</option>`).join('')}
</select>
</div>
<div class="field">
<label>תחנה אזורית</label>
<select id="sel-station" ${!state.district?'disabled':''}>
<option value="">${state.district?'בחרו תחנה...':'בחרו קודם מחוז'}</option>
${stations.map(s=>`<option value="${s}" ${state.station===s?'selected':''}>${s}</option>`).join('')}
</select>
</div>
</div>
<div class="actions-row">
<span></span>
<button class="btn btn-primary" id="to-step2" ${(!state.district||!state.station)?'disabled':''}>המשך לבחירת ספק →</button>
</div>
</div>`;
}

function step2(){
return `
<div class="panel">
<div class="context-chip"><span class="dot"></span>${state.district} · ${state.station}</div>
<h2>שלב 2 — בחירת ספק</h2>
<p class="hint">בחרו את הספק היחיד שמבצע את הטיפול או התיקון.</p>
<div class="supplier-grid">
${SUPPLIER_NAMES.map(s=>{
const ini = s.replace(/["\u201c\u201d\(\)]/g,'').trim().split(' ').map(w=>w[0]).slice(0,2).join('');
const cnt = SUPPLIERS[s].length;
return `<div class="supplier-card ${state.supplier===s?'selected':''}" data-supplier="${s}">
<div class="ini">${ini}</div>
<div class="name">${s}</div>
<div class="count">${cnt?cnt+' סוגי שירות':'ללא רשימה מוגדרת'}</div>
</div>`;
}).join('')}
</div>
<div class="actions-row">
<button class="btn btn-ghost" id="back-step1">→ חזרה</button>
<button class="btn btn-primary" id="to-step3" ${!state.supplier?'disabled':''}>המשך לפרטי שירות →</button>
</div>
</div>`;
}

function step3(){
const services = (SUPPLIERS[state.supplier]||[]);
const total = state.lines.reduce((sum,l)=> sum + (Number(l.qty||0) * Number(l.unitCost||0)), 0);
const linesValid = state.lines.every(l => (l.service && (l.service!==OTHER_LABEL || l.customText.trim())) && Number(l.qty)>0 && Number(l.unitCost)>=0 && l.unitCost!=='');
return `
<div class="panel">
<div class="context-chip"><span class="dot"></span>${state.district} · ${state.station} · ${state.supplier}</div>
<h2>שלב 3 — פרטי השירות</h2>
<p class="hint">עבור כל סוג טיפול/תיקון שבוצע: כמות פריטי ציוד ועלות ליחידה. ניתן להוסיף כמה שורות שירות שנדרש.</p>

${state.lines.map((l,idx)=>lineItemHtml(l, idx, services)).join('')}
<button class="add-line-btn" id="add-line">+ הוספת סוג שירות נוסף</button>

<div class="summary-bar">
<div><div class="lbl">סה"כ עלות ההזמנה</div><div class="val">${fmt(total)}</div></div>
<div style="text-align:left"><div class="lbl">שורות שירות</div><div class="val" style="font-size:18px">${state.lines.length}</div></div>
</div>

<div class="actions-row">
<button class="btn btn-ghost" id="back-step2">→ חזרה</button>
<button class="btn btn-primary" id="submit-order" ${(!linesValid||state.saving)?'disabled':''}>${state.saving?'שומר...':'שמירת ההזמנה ✓'}</button>
</div>
</div>`;
}

function lineItemHtml(l, idx, services){
return `
<div class="line-item" data-line="${l.id}">
${state.lines.length>1?`<button class="del" data-del="${l.id}">✕</button>`:''}
<div class="line-grid">
<div class="field" style="margin-bottom:0">
<label>סוג טיפול / תיקון</label>
<select data-field="service" data-line="${l.id}">
<option value="">בחרו...</option>
${services.map(s=>`<option value="${s.replace(/"/g,'&quot;')}" ${l.service===s?'selected':''}>${s}</option>`).join('')}
<option value="${OTHER_LABEL}" ${l.service===OTHER_LABEL?'selected':''}>${OTHER_LABEL}</option>
</select>
</div>
<div class="field" style="margin-bottom:0">
<label>כמות פריטים</label>
<input type="number" min="1" step="1" data-field="qty" data-line="${l.id}" value="${l.qty}">
</div>
<div class="field" style="margin-bottom:0">
<label>עלות ליחידה (₪)</label>
<input type="number" min="0" step="0.01" data-field="unitCost" data-line="${l.id}" value="${l.unitCost}">
</div>
<div class="field" style="margin-bottom:0">
<label>סה"כ לשורה</label>
<input type="text" disabled value="${fmt(Number(l.qty||0)*Number(l.unitCost||0))}">
</div>
</div>
${l.service===OTHER_LABEL?`
<div class="field" style="margin-top:12px;margin-bottom:0">
<label>פירוט הטיפול / התיקון</label>
<input type="text" data-field="customText" data-line="${l.id}" value="${(l.customText||'').replace(/"/g,'&quot;')}" placeholder="תארו את סוג השירות שבוצע">
</div>`:''}
</div>`;
}

function confirmView(){
return `
<div class="panel confirm-wrap">
<div class="confirm-icon">${ICON_CHECK}</div>
<h2>ההזמנה נשמרה בהצלחה</h2>
<p class="hint">${state.district} · ${state.station} · ${state.supplier}</p>
<button class="btn btn-primary" id="new-order" style="margin-top:14px">הזמנה נוספת</button>
<button class="btn btn-ghost" id="go-report" style="margin-top:14px">מעבר לדוח ניצול</button>
</div>`;
}

/* ============ REPORT ============ */
function reportView(){
if(state.orders===null) return `<div class="loading">טוען נתונים...</div>`;
const all = state.orders;
const filtered = all.filter(o =>
(!state.filters.district || o.district===state.filters.district) &&
(!state.filters.supplier || o.supplier===state.filters.supplier)
);

const totalCost = filtered.reduce((s,o)=>s+o.totalCost,0);
const totalOrders = filtered.length;
const totalItems = filtered.reduce((s,o)=>s+o.items.reduce((s2,i)=>s2+Number(i.qty),0),0);
const avg = totalOrders? totalCost/totalOrders : 0;

const bySupplier = {};
const byDistrict = {};
filtered.forEach(o=>{
bySupplier[o.supplier] = (bySupplier[o.supplier]||0) + o.totalCost;
byDistrict[o.district] = (byDistrict[o.district]||0) + o.totalCost;
});
const maxSupplier = Math.max(1,...Object.values(bySupplier));
const maxDistrict = Math.max(1,...Object.values(byDistrict));

const rows = filtered.slice().sort((a,b)=> b.createdAt - a.createdAt);

return `
<div class="report-top">
<div>
<h2 style="margin:0 0 4px;font-size:19px;font-weight:800;">דוח ניצול הזמנות</h2>
<p class="hint" style="margin:0">תמונת מצב מצטברת על כל ההזמנות שהוזנו על ידי המחוזות</p>
</div>
<button class="btn btn-ghost btn-sm" id="export-csv" ${!filtered.length?'disabled':''}>ייצוא ל-CSV ⬇</button>
</div>

<div class="kpis">
<div class="kpi"><div class="lbl">סה"כ עלות</div><div class="val">${fmt(totalCost)}</div></div>
<div class="kpi"><div class="lbl">מס' הזמנות</div><div class="val">${totalOrders}</div></div>
<div class="kpi"><div class="lbl">סה"כ פריטים</div><div class="val">${totalItems}</div></div>
<div class="kpi"><div class="lbl">עלות ממוצעת להזמנה</div><div class="val small">${fmt(avg)}</div></div>
</div>

<div class="filters">
<select id="filter-district">
<option value="">כל המחוזות</option>
${Object.keys(DISTRICTS).map(d=>`<option value="${d}" ${state.filters.district===d?'selected':''}>${d}</option>`).join('')}
</select>
<select id="filter-supplier">
<option value="">כל הספקים</option>
${SUPPLIER_NAMES.map(s=>`<option value="${s}" ${state.filters.supplier===s?'selected':''}>${s}</option>`).join('')}
</select>
<div class="spacer"></div>
<span class="hint" style="margin:0">${filtered.length} תוצאות</span>
</div>

${!filtered.length ? `
<div class="empty-state panel">${ICON_EMPTY}<div style="font-weight:700;color:var(--char)">אין עדיין הזמנות תואמות</div><div style="font-size:12.5px;margin-top:4px">הזמנות שיוזנו על ידי המחוזות יופיעו כאן</div></div>
` : `
<div class="breakdown">
<div class="bd-panel">
<h3>עלות לפי ספק</h3>
${Object.entries(bySupplier).sort((a,b)=>b[1]-a[1]).map(([k,v])=>`
<div class="bd-row"><div class="nm">${k}</div><div class="bd-bar-bg"><div class="bd-bar" style="width:${(v/maxSupplier*100).toFixed(0)}%"></div></div><div class="amt">${fmt(v)}</div></div>
`).join('')}
</div>
<div class="bd-panel">
<h3>עלות לפי מחוז</h3>
${Object.entries(byDistrict).sort((a,b)=>b[1]-a[1]).map(([k,v])=>`
<div class="bd-row"><div class="nm">${k}</div><div class="bd-bar-bg"><div class="bd-bar" style="width:${(v/maxDistrict*100).toFixed(0)}%"></div></div><div class="amt">${fmt(v)}</div></div>
`).join('')}
</div>
</div>

<div class="table-wrap">
<table>
<thead><tr>
<th>תאריך</th><th>מחוז</th><th>תחנה</th><th>ספק</th><th>שורות שירות</th><th>פריטים</th><th>עלות כוללת</th>
</tr></thead>
<tbody>
${rows.map(o=>`
<tr>
<td>${new Date(o.createdAt).toLocaleDateString('he-IL')}</td>
<td>${o.district}</td>
<td>${o.station}</td>
<td><span class="tag">${o.supplier}</span></td>
<td>${o.items.map(i=>i.service===OTHER_LABEL?i.customText:i.service).join('; ')}</td>
<td>${o.items.reduce((s,i)=>s+Number(i.qty),0)}</td>
<td class="amt-cell">${fmt(o.totalCost)}</td>
</tr>
`).join('')}
</tbody>
</table>
</div>
`}
`;
}

/* ============ EVENTS ============ */
function attachEvents(){
document.querySelectorAll('[data-nav]').forEach(b=>b.onclick=()=>{ state.view=b.dataset.nav; render(); });

// step1
const selD = document.getElementById('sel-district');
if(selD) selD.onchange = e=>{ state.district=e.target.value; state.station=''; render(); };
const selS = document.getElementById('sel-station');
if(selS) selS.onchange = e=>{ state.station=e.target.value; render(); };
const to2 = document.getElementById('to-step2');
if(to2) to2.onclick = ()=>{ state.step=2; render(); };

// step2
document.querySelectorAll('[data-supplier]').forEach(c=>c.onclick=()=>{
state.supplier = c.dataset.supplier; state.lines=[blankLine()]; render();
});
const back1 = document.getElementById('back-step1');
if(back1) back1.onclick = ()=>{ state.step=1; render(); };
const to3 = document.getElementById('to-step3');
if(to3) to3.onclick = ()=>{ state.step=3; render(); };

// step3
const back2 = document.getElementById('back-step2');
if(back2) back2.onclick = ()=>{ state.step=2; render(); };
const addLine = document.getElementById('add-line');
if(addLine) addLine.onclick = ()=>{ state.lines.push(blankLine()); render(); };
document.querySelectorAll('[data-del]').forEach(b=>b.onclick=()=>{
state.lines = state.lines.filter(l=>l.id!==b.dataset.del); render();
});
document.querySelectorAll('[data-field]').forEach(el=>{
el.onchange = e=>{
const line = state.lines.find(l=>l.id===e.target.dataset.line);
if(!line) return;
line[e.target.dataset.field] = e.target.value;
render();
};
});
const submit = document.getElementById('submit-order');
if(submit) submit.onclick = async ()=>{
state.saving = true; render();
const items = state.lines.map(l=>({
service: l.service, customText: l.service===OTHER_LABEL? l.customText.trim() : '',
qty: Number(l.qty), unitCost: Number(l.unitCost), lineCost: Number(l.qty)*Number(l.unitCost)
}));
const order = {
id: uid(), district: state.district, station: state.station, supplier: state.supplier,
items, totalCost: items.reduce((s,i)=>s+i.lineCost,0), createdAt: Date.now()
};
state.orders = state.orders || [];
state.orders.push(order);
await saveOrders();
state.saving=false;
state.step = 'confirm';
render();
};

const newOrder = document.getElementById('new-order');
if(newOrder) newOrder.onclick = ()=>{
state.district=''; state.station=''; state.supplier=''; state.lines=[blankLine()]; state.step=1; render();
};
const goReport = document.getElementById('go-report');
if(goReport) goReport.onclick = ()=>{ state.view='report'; render(); };

// report
const fD = document.getElementById('filter-district');
if(fD) fD.onchange = e=>{ state.filters.district = e.target.value; render(); };
const fS = document.getElementById('filter-supplier');
if(fS) fS.onchange = e=>{ state.filters.supplier = e.target.value; render(); };
const exp = document.getElementById('export-csv');
if(exp) exp.onclick = exportCsv;
}

function exportCsv(){
const filtered = state.orders.filter(o =>
(!state.filters.district || o.district===state.filters.district) &&
(!state.filters.supplier || o.supplier===state.filters.supplier)
);
const header = ['תאריך','מחוז','תחנה','ספק','סוג שירות','כמות','עלות ליחידה','עלות שורה'];
const lines = [header.join(',')];
filtered.forEach(o=>{
o.items.forEach(i=>{
const svc = (i.service===OTHER_LABEL? i.customText : i.service)||'';
lines.push([
new Date(o.createdAt).toLocaleDateString('he-IL'), o.district, o.station, o.supplier,
'"'+svc.replace(/"/g,'""')+'"', i.qty, i.unitCost, i.lineCost
].join(','));
});
});
const blob = new Blob(["\uFEFF"+lines.join('\n')], {type:'text/csv;charset=utf-8;'});
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url; a.download = 'דוח_ניצול_הזמנות.csv'; a.click();
URL.revokeObjectURL(url);
}

/* patch wizardView to handle confirm pseudo-step */
const origWizardView = wizardView;
wizardView = function(){
if(state.step==='confirm') return confirmView();
return origWizardView();
};

loadOrders();
render();
</script>
</body>
</html>