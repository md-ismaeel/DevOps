<!-- <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Low Ember Coffee — small-batch, roasted weekly</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:        #1c140f;
    --bg-raised: #251a13;
    --cream:     #f2e6d6;
    --cream-dim: #c9b8a3;
    --amber:     #e0a447;
    --amber-dim: #7a5a2a;
    --moss:      #7c8a5f;
    --rust:      #b1573b;
    --line:      rgba(242,230,214,0.14);
    --radius: 3px;
  }
  *{box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{
    margin:0;
    background:var(--bg);
    color:var(--cream);
    font-family:'Fraunces', Georgia, serif;
    line-height:1.5;
    -webkit-font-smoothing:antialiased;
  }
  .mono{font-family:'Space Mono', monospace; letter-spacing:0.03em;}
  a{color:inherit;}

  /* ---------- layout shells ---------- */
  header.site{
    position:sticky; top:0; z-index:40;
    display:flex; align-items:center; justify-content:space-between;
    padding:18px 5vw;
    background:rgba(28,20,15,0.86);
    backdrop-filter:blur(8px);
    border-bottom:1px solid var(--line);
  }
  .brand{display:flex; align-items:center; gap:10px; font-size:1.15rem; font-weight:600;}
  .brand .mark{
    width:26px;height:26px;border-radius:50%;
    background:radial-gradient(circle at 35% 30%, var(--amber), var(--rust) 75%);
    box-shadow:0 0 0 1px var(--line);
  }
  nav.site-links{display:flex; gap:28px; font-family:'Space Mono',monospace; font-size:0.78rem; text-transform:uppercase; letter-spacing:0.08em; color:var(--cream-dim);}
  nav.site-links a{text-decoration:none; transition:color .2s;}
  nav.site-links a:hover{color:var(--amber);}

  #cart-toggle{
    position:relative;
    background:transparent;
    border:1px solid var(--line);
    color:var(--cream);
    font-family:'Space Mono',monospace;
    font-size:0.78rem;
    padding:8px 14px;
    border-radius:var(--radius);
    cursor:pointer;
    display:flex; align-items:center; gap:8px;
    transition:border-color .2s, color .2s;
  }
  #cart-toggle:hover{border-color:var(--amber); color:var(--amber);}
  #cart-count{
    background:var(--amber); color:#1c140f; font-weight:700;
    border-radius:50%; min-width:18px; height:18px; display:inline-flex;
    align-items:center; justify-content:center; font-size:0.7rem; padding:0 3px;
  }

  /* ---------- hero ---------- */
  .hero{
    padding:9vh 5vw 8vh;
    display:grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap:6vw;
    align-items:center;
    border-bottom:1px solid var(--line);
  }
  .hero h1{
    font-size:clamp(2.6rem, 5.4vw, 4.4rem);
    font-weight:600;
    line-height:1.02;
    margin:0 0 22px;
    font-optical-sizing:auto;
  }
  .hero h1 em{
    font-style:italic; color:var(--amber); font-weight:500;
  }
  .hero p.lede{
    max-width:46ch; color:var(--cream-dim); font-size:1.08rem; margin:0 0 30px;
  }
  .hero .cta-row{display:flex; gap:16px; align-items:center; flex-wrap:wrap;}
  .btn-primary{
    background:var(--amber); color:#1c140f; border:none;
    font-family:'Space Mono',monospace; font-weight:700; font-size:0.82rem;
    padding:14px 26px; border-radius:var(--radius); cursor:pointer;
    text-transform:uppercase; letter-spacing:0.06em;
    transition:transform .15s ease, background .2s;
  }
  .btn-primary:hover{transform:translateY(-2px); background:#eeb865;}
  .hero-note{font-family:'Space Mono',monospace; font-size:0.75rem; color:var(--cream-dim);}

  /* signature element: roast dial */
  .roast-clock{
    justify-self:center;
    width:min(280px, 60vw);
    aspect-ratio:1/1;
    position:relative;
  }
  .roast-clock svg{width:100%; height:100%;}
  .roast-clock .clock-label{
    position:absolute; inset:0; display:flex; flex-direction:column;
    align-items:center; justify-content:center; text-align:center;
    pointer-events:none;
  }
  .roast-clock .clock-label .big{font-family:'Space Mono',monospace; font-size:2rem; font-weight:700; color:var(--amber);}
  .roast-clock .clock-label .small{font-family:'Space Mono',monospace; font-size:0.68rem; color:var(--cream-dim); text-transform:uppercase; letter-spacing:0.08em; margin-top:4px;}

  /* ---------- filter row ---------- */
  .shop-head{
    padding:7vh 5vw 3vh;
    display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:20px;
  }
  .shop-head h2{font-size:1.9rem; font-weight:600; margin:0;}
  .shop-head .eyebrow{font-family:'Space Mono',monospace; font-size:0.72rem; color:var(--amber); text-transform:uppercase; letter-spacing:0.12em; margin-bottom:8px; display:block;}
  .filters{display:flex; gap:8px; flex-wrap:wrap;}
  .filter-btn{
    background:transparent; border:1px solid var(--line); color:var(--cream-dim);
    font-family:'Space Mono',monospace; font-size:0.72rem; text-transform:uppercase; letter-spacing:0.05em;
    padding:8px 14px; border-radius:20px; cursor:pointer; transition:all .2s;
  }
  .filter-btn:hover{border-color:var(--amber); color:var(--cream);}
  .filter-btn.active{background:var(--amber); border-color:var(--amber); color:#1c140f; font-weight:700;}

  /* ---------- product grid ---------- */
  .grid{
    display:grid;
    grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));
    gap:1px;
    background:var(--line);
    margin:0 5vw 10vh;
    border:1px solid var(--line);
  }
  .card{
    background:var(--bg);
    padding:28px 24px 24px;
    display:flex; flex-direction:column; gap:14px;
    transition:background .25s;
  }
  .card:hover{background:var(--bg-raised);}
  .card-top{display:flex; justify-content:space-between; align-items:flex-start;}
  .swatch{
    width:52px; height:66px; border-radius:2px 2px 8px 8px;
    flex-shrink:0;
    box-shadow:inset 0 -18px 20px rgba(0,0,0,0.25);
  }
  .freshness{
    display:flex; align-items:center; gap:6px;
    font-family:'Space Mono',monospace; font-size:0.68rem; color:var(--cream-dim);
  }
  .dot{width:8px; height:8px; border-radius:50%; flex-shrink:0;}
  .dot.fresh{background:var(--moss);}
  .dot.turning{background:var(--amber);}
  .dot.resting{background:var(--rust);}

  .card h3{font-size:1.3rem; font-weight:600; margin:0;}
  .card .origin{font-family:'Space Mono',monospace; font-size:0.72rem; color:var(--amber); text-transform:uppercase; letter-spacing:0.05em;}
  .card .desc{color:var(--cream-dim); font-size:0.92rem; margin:0; flex-grow:1;}
  .card .tags{display:flex; gap:6px; flex-wrap:wrap;}
  .tag{font-family:'Space Mono',monospace; font-size:0.65rem; border:1px solid var(--line); color:var(--cream-dim); padding:3px 8px; border-radius:12px;}

  .card-foot{display:flex; align-items:center; justify-content:space-between; margin-top:6px;}
  .price{font-family:'Space Mono',monospace; font-size:1.05rem; font-weight:700;}
  .add-btn{
    background:transparent; border:1px solid var(--amber); color:var(--amber);
    font-family:'Space Mono',monospace; font-size:0.72rem; text-transform:uppercase; letter-spacing:0.05em;
    padding:9px 16px; border-radius:var(--radius); cursor:pointer; transition:all .2s;
  }
  .add-btn:hover{background:var(--amber); color:#1c140f;}
  .add-btn.added{background:var(--moss); border-color:var(--moss); color:#1c140f;}

  /* ---------- footer ---------- */
  footer{
    padding:5vh 5vw 6vh; border-top:1px solid var(--line);
    display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px;
    font-family:'Space Mono',monospace; font-size:0.72rem; color:var(--cream-dim);
  }

  /* ---------- cart drawer ---------- */
  .overlay{
    position:fixed; inset:0; background:rgba(10,7,5,0.55);
    opacity:0; pointer-events:none; transition:opacity .25s; z-index:60;
  }
  .overlay.open{opacity:1; pointer-events:auto;}
  .drawer{
    position:fixed; top:0; right:0; height:100%; width:min(380px, 92vw);
    background:var(--bg-raised); border-left:1px solid var(--line);
    transform:translateX(100%); transition:transform .3s ease;
    z-index:70; display:flex; flex-direction:column;
  }
  .drawer.open{transform:translateX(0);}
  .drawer-head{
    padding:22px 24px; border-bottom:1px solid var(--line);
    display:flex; justify-content:space-between; align-items:center;
  }
  .drawer-head h3{margin:0; font-size:1.2rem;}
  .close-btn{background:none; border:none; color:var(--cream-dim); font-size:1.4rem; cursor:pointer; line-height:1;}
  .close-btn:hover{color:var(--amber);}
  .drawer-items{flex-grow:1; overflow-y:auto; padding:10px 24px;}
  .empty-cart{color:var(--cream-dim); font-size:0.9rem; padding:40px 0; text-align:center;}
  .line-item{
    display:flex; gap:12px; padding:16px 0; border-bottom:1px solid var(--line);
  }
  .line-item .swatch{width:38px; height:48px;}
  .li-info{flex-grow:1;}
  .li-info h4{margin:0 0 4px; font-size:0.98rem; font-weight:600;}
  .li-info .mono{font-size:0.7rem; color:var(--cream-dim);}
  .qty-row{display:flex; align-items:center; gap:10px; margin-top:8px;}
  .qty-btn{
    width:22px; height:22px; border:1px solid var(--line); background:none; color:var(--cream);
    border-radius:50%; cursor:pointer; font-family:'Space Mono',monospace; font-size:0.85rem;
    display:flex; align-items:center; justify-content:center;
  }
  .qty-btn:hover{border-color:var(--amber); color:var(--amber);}
  .li-remove{background:none; border:none; color:var(--rust); font-family:'Space Mono',monospace; font-size:0.68rem; cursor:pointer; text-decoration:underline; padding:0;}
  .li-price{font-family:'Space Mono',monospace; font-weight:700; align-self:flex-start;}
  .drawer-foot{padding:20px 24px 26px; border-top:1px solid var(--line);}
  .subtotal-row{display:flex; justify-content:space-between; font-family:'Space Mono',monospace; margin-bottom:16px; font-size:0.95rem;}
  .checkout-btn{
    width:100%; background:var(--amber); color:#1c140f; border:none;
    font-family:'Space Mono',monospace; font-weight:700; font-size:0.82rem;
    padding:14px; border-radius:var(--radius); cursor:pointer; text-transform:uppercase; letter-spacing:0.06em;
  }
  .checkout-btn:hover{background:#eeb865;}
  .checkout-note{text-align:center; font-size:0.68rem; color:var(--cream-dim); margin-top:10px; font-family:'Space Mono',monospace;}

  .toast{
    position:fixed; bottom:26px; left:50%; transform:translateX(-50%) translateY(20px);
    background:var(--cream); color:#1c140f; font-family:'Space Mono',monospace; font-size:0.78rem;
    padding:12px 20px; border-radius:var(--radius); opacity:0; transition:all .3s; z-index:80;
    pointer-events:none;
  }
  .toast.show{opacity:1; transform:translateX(-50%) translateY(0);}

  @media (max-width:800px){
    .hero{grid-template-columns:1fr; text-align:left;}
    .roast-clock{justify-self:flex-start;}
    nav.site-links{display:none;}
  }

  @media (prefers-reduced-motion: reduce){
    *{transition:none !important; animation:none !important; scroll-behavior:auto !important;}
  }

  :focus-visible{outline:2px solid var(--amber); outline-offset:2px;}
</style>
</head>
<body>

<header class="site">
  <div class="brand"><span class="mark"></span> Low Ember</div>
  <nav class="site-links">
    <a href="#shop">Shop</a>
    <a href="#about">About</a>
    <a href="#footer">Contact</a>
  </nav>
  <button id="cart-toggle" aria-label="Open cart">
    Cart <span id="cart-count">0</span>
  </button>
</header>

<section class="hero" id="about">
  <div>
    <h1>Roasted Tuesdays.<br>Shipped <em>Wednesdays</em>.</h1>
    <p class="lede">We roast in ten-kilo batches out of a converted garage in the Cordillera foothills, and we never hold stock longer than a week. What you get is coffee that still remembers being green.</p>
    <div class="cta-row">
      <button class="btn-primary" onclick="document.getElementById('shop').scrollIntoView()">Browse this week's roast</button>
      <span class="hero-note">4 lots · while they last</span>
    </div>
  </div>
  <div class="roast-clock" aria-hidden="true">
    <svg viewBox="0 0 200 200">
      <circle cx="100" cy="100" r="88" fill="none" stroke="var(--line)" stroke-width="10"/>
      <circle id="dial-progress" cx="100" cy="100" r="88" fill="none" stroke="var(--amber)" stroke-width="10"
        stroke-linecap="round" stroke-dasharray="553" stroke-dashoffset="553"
        transform="rotate(-90 100 100)"/>
    </svg>
    <div class="clock-label">
      <span class="big" id="dial-day">Tue</span>
      <span class="small" id="dial-sub">roast day</span>
    </div>
  </div>
</section>

<section class="shop-head" id="shop">
  <div>
    <span class="eyebrow">This week's lots</span>
    <h2>Four bags. One truck route.</h2>
  </div>
  <div class="filters" role="group" aria-label="Filter by roast style">
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="light">Light / Washed</button>
    <button class="filter-btn" data-filter="dark">Dark / Blend</button>
    <button class="filter-btn" data-filter="decaf">Decaf</button>
  </div>
</section>

<div class="grid" id="product-grid"></div>

<footer id="footer">
  <span>© 2026 Low Ember Coffee — Cordillera Ridge, no shop online yet, just this page.</span>
  <span>hello@lowember.coffee</span>
</footer>

<div class="overlay" id="overlay"></div>
<aside class="drawer" id="drawer" aria-label="Shopping cart">
  <div class="drawer-head">
    <h3>Your bag</h3>
    <button class="close-btn" id="close-drawer" aria-label="Close cart">&times;</button>
  </div>
  <div class="drawer-items" id="drawer-items"></div>
  <div class="drawer-foot">
    <div class="subtotal-row"><span>Subtotal</span><span id="subtotal">$0.00</span></div>
    <button class="checkout-btn" id="checkout-btn">Checkout</button>
    <p class="checkout-note">Demo page — no real payment is taken.</p>
  </div>
</aside>

<div class="toast" id="toast"></div>

<script>
  const products = [
    {
      id:'marigold-ridge', name:'Marigold Ridge', origin:'Ethiopia · Guji',
      style:'light', desc:'Washed, dried slow. Bergamot up front, settles into stone fruit.',
      tags:['Washed','Single origin'], price:19, swatch:'linear-gradient(180deg,#e0a447,#b1573b)',
      roastedDaysAgo:2
    },
    {
      id:'black-anchor', name:'Black Anchor', origin:'House Blend',
      style:'dark', desc:'Our darkest cut. Bittersweet cocoa, char, built for milk.',
      tags:['Dark roast','Blend'], price:17, swatch:'linear-gradient(180deg,#4a3527,#241812)',
      roastedDaysAgo:6
    },
    {
      id:'cordillera-blend', name:'Cordillera Blend', origin:'Colombia · Huila',
      style:'dark', desc:'Our house filter blend. Caramel, walnut, a clean quiet finish.',
      tags:['Medium roast','Blend'], price:16, swatch:'linear-gradient(180deg,#8a5a2f,#4a3527)',
      roastedDaysAgo:4
    },
    {
      id:'quiet-hour', name:'Quiet Hour Decaf', origin:'Colombia · Sugarcane process',
      style:'decaf', desc:'Decaffeinated without the flatness. Cocoa, dried plum, still worth the cup.',
      tags:['Decaf','Single origin'], price:18, swatch:'linear-gradient(180deg,#7c8a5f,#3f4630)',
      roastedDaysAgo:9
    }
  ];

  const cart = {}; // id -> qty

  function freshnessInfo(days){
    if(days <= 3) return {label:`Roasted ${days}d ago`, cls:'fresh'};
    if(days <= 7) return {label:`Roasted ${days}d ago`, cls:'turning'};
    return {label:`Roasted ${days}d ago`, cls:'resting'};
  }

  function renderGrid(filter='all'){
    const grid = document.getElementById('product-grid');
    grid.innerHTML = '';
    products
      .filter(p => filter === 'all' || p.style === filter)
      .forEach(p => {
        const f = freshnessInfo(p.roastedDaysAgo);
        const card = document.createElement('article');
        card.className = 'card';
        card.innerHTML = `
          <div class="card-top">
            <div class="swatch" style="background:${p.swatch}"></div>
            <div class="freshness"><span class="dot ${f.cls}"></span>${f.label}</div>
          </div>
          <div>
            <span class="origin">${p.origin}</span>
            <h3>${p.name}</h3>
          </div>
          <p class="desc">${p.desc}</p>
          <div class="tags">${p.tags.map(t=>`<span class="tag">${t}</span>`).join('')}</div>
          <div class="card-foot">
            <span class="price">$${p.price.toFixed(2)}</span>
            <button class="add-btn" data-id="${p.id}">Add to bag</button>
          </div>
        `;
        grid.appendChild(card);
      });

    grid.querySelectorAll('.add-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        addToCart(btn.dataset.id);
        btn.textContent = 'Added ✓';
        btn.classList.add('added');
        setTimeout(() => { btn.textContent = 'Add to bag'; btn.classList.remove('added'); }, 1100);
      });
    });
  }

  document.querySelectorAll('.filter-btn').forEach(btn=>{
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
      btn.classList.add('active');
      renderGrid(btn.dataset.filter);
    });
  });

  function addToCart(id){
    cart[id] = (cart[id] || 0) + 1;
    updateCartUI();
    showToast(`${products.find(p=>p.id===id).name} added to bag`);
  }
  function changeQty(id, delta){
    cart[id] = (cart[id] || 0) + delta;
    if(cart[id] <= 0) delete cart[id];
    updateCartUI();
  }
  function removeFromCart(id){
    delete cart[id];
    updateCartUI();
  }

  function updateCartUI(){
    const totalItems = Object.values(cart).reduce((a,b)=>a+b,0);
    document.getElementById('cart-count').textContent = totalItems;

    const container = document.getElementById('drawer-items');
    const ids = Object.keys(cart);
    if(ids.length === 0){
      container.innerHTML = '<p class="empty-cart">Your bag is empty. Add a lot from this week\'s roast.</p>';
    } else {
      container.innerHTML = ids.map(id => {
        const p = products.find(pr => pr.id === id);
        const qty = cart[id];
        return `
          <div class="line-item">
            <div class="swatch" style="background:${p.swatch}"></div>
            <div class="li-info">
              <h4>${p.name}</h4>
              <div class="mono">$${p.price.toFixed(2)} each</div>
              <div class="qty-row">
                <button class="qty-btn" data-action="dec" data-id="${id}" aria-label="Decrease quantity">–</button>
                <span class="mono">${qty}</span>
                <button class="qty-btn" data-action="inc" data-id="${id}" aria-label="Increase quantity">+</button>
              </div>
              <div><button class="li-remove" data-action="remove" data-id="${id}">Remove</button></div>
            </div>
            <span class="li-price">$${(p.price*qty).toFixed(2)}</span>
          </div>
        `;
      }).join('');
    }

    container.querySelectorAll('button').forEach(btn=>{
      btn.addEventListener('click', () => {
        const id = btn.dataset.id;
        if(btn.dataset.action === 'inc') changeQty(id, 1);
        if(btn.dataset.action === 'dec') changeQty(id, -1);
        if(btn.dataset.action === 'remove') removeFromCart(id);
      });
    });

    const subtotal = ids.reduce((sum,id) => sum + products.find(p=>p.id===id).price * cart[id], 0);
    document.getElementById('subtotal').textContent = `$${subtotal.toFixed(2)}`;
  }

  let toastTimer;
  function showToast(msg){
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(()=>t.classList.remove('show'), 1800);
  }

  const drawer = document.getElementById('drawer');
  const overlay = document.getElementById('overlay');
  function openDrawer(){ drawer.classList.add('open'); overlay.classList.add('open'); }
  function closeDrawer(){ drawer.classList.remove('open'); overlay.classList.remove('open'); }
  document.getElementById('cart-toggle').addEventListener('click', openDrawer);
  document.getElementById('close-drawer').addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);
  document.addEventListener('keydown', e => { if(e.key === 'Escape') closeDrawer(); });

  document.getElementById('checkout-btn').addEventListener('click', () => {
    if(Object.keys(cart).length === 0){ showToast('Your bag is empty'); return; }
    showToast('This is a demo — no real checkout yet');
  });

  // signature roast-clock: shows how far through the week's roast cycle "today" is
  (function initClock(){
    const days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    const today = new Date();
    const roastDay = 2; // Tuesday
    let diff = today.getDay() - roastDay;
    if(diff < 0) diff += 7;
    const progress = diff / 7; // 0 = just roasted, near 1 = about to roast again

    const circle = document.getElementById('dial-progress');
    const circumference = 553;
    circle.style.strokeDashoffset = circumference * (1 - progress);

    document.getElementById('dial-day').textContent = days[today.getDay()];
    const subEl = document.getElementById('dial-sub');
    if(diff === 0) subEl.textContent = 'roasting today';
    else subEl.textContent = `day ${diff} since roast`;
  })();

  renderGrid();
  updateCartUI();
</script>

</body>
</html> -->