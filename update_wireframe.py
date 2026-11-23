import os

p = r"d:\01. Chitopia\wireframe\index.html"
with open(p, "r", encoding="utf-8") as f:
    h = f.read()

# 1. Logo replacement
h = h.replace('<a href="#home" class="logo">LOGO</a>', '<a href="#home" class="logo" style="border:none;padding:0;"><img src="img/logo.png" alt="CHITOPIA" style="height:38px;object-fit:contain;"></a>')
h = h.replace('<div class="logo">LOGO</div>', '<div class="logo" style="border:none;padding:0;"><img src="img/logo.png" alt="CHITOPIA" style="height:38px;object-fit:contain;"></div>')

# 2. Hero banner image
h = h.replace('<div class="ph"><span>BG VIDEO / IMAGE — 치킨 클로즈업 푸드샷 (자동재생 루프, 음소거)</span></div>', '<div class="ph" style="background-image:url(\'img/menu_classic_chicken.jpg\');background-size:cover;background-position:center;"><span style="background:rgba(0,0,0,0.65);color:#fff;border-radius:4px;padding:6px 12px;font-size:13px;">CHITOPIA Authentic Korean Chicken</span></div>')

# 3. Signature Menu in Home
h_menu_orig = """      <div class="grid g4 mt40">
        <div class="card"><div class="ph" style="aspect-ratio:1"><span>MENU IMG 1</span></div><h3 class="mt16">[Menu Name 1]</h3><div class="line w80"></div><div class="line w60"></div></div>
        <div class="card"><div class="ph" style="aspect-ratio:1"><span>MENU IMG 2</span></div><h3 class="mt16">[Menu Name 2]</h3><div class="line w80"></div><div class="line w60"></div></div>
        <div class="card"><div class="ph" style="aspect-ratio:1"><span>MENU IMG 3</span></div><h3 class="mt16">[Menu Name 3]</h3><div class="line w80"></div><div class="line w60"></div></div>
        <div class="card"><div class="ph" style="aspect-ratio:1"><span>MENU IMG 4</span></div><h3 class="mt16">[Menu Name 4]</h3><div class="line w80"></div><div class="line w60"></div></div>
      </div>"""

h_menu_new = """      <div class="grid g4 mt40">
        <div class="card">
          <div class="ph" style="aspect-ratio:1;background:url('img/menu_classic_chicken.jpg') center/cover;"></div>
          <div class="row mt16"><span class="tag">Signature</span></div>
          <h3 class="mt8" data-ko="클래식 프라이드 치킨">Classic Fried Chicken</h3>
          <p class="small muted" data-ko="바삭한 튀김옷의 황금빛 순살 치킨 & 그레이비">Golden boneless chicken with crisp coating & gravy</p>
        </div>
        <div class="card">
          <div class="ph" style="aspect-ratio:1;background:url('img/menu_creamy_onion.jpg') center/cover;"></div>
          <div class="row mt16"><span class="tag">Best Seller</span></div>
          <h3 class="mt8" data-ko="크리미 어니언 치킨">Creamy Onion Chicken</h3>
          <p class="small muted" data-ko="신선한 양파 슬라이스와 부드러운 화이트 크림 소스">Crispy chicken topped with fresh sliced onions & white cream sauce</p>
        </div>
        <div class="card">
          <div class="ph" style="aspect-ratio:1;background:url('img/menu_takoyaki.jpg') center/cover;"></div>
          <div class="row mt16"><span class="tag">K-Street Combo</span></div>
          <h3 class="mt8" data-ko="치킨 & 타코야키 콤보">Chicken & Takoyaki Combo</h3>
          <p class="small muted" data-ko="바삭한 치킨과 고소한 타코야키의 환상 조합">Crispy chicken bites and savory takoyaki in one meal</p>
        </div>
        <div class="card">
          <div class="ph" style="aspect-ratio:1;background:url('img/menu_tteokbokki.jpg') center/cover;"></div>
          <div class="row mt16"><span class="tag">K-Food</span></div>
          <h3 class="mt8" data-ko="빠사시 쌀 떡볶이">Classic Rice Tteokbokki</h3>
          <p class="small muted" data-ko="특제 소스로 맛을 낸 쫄깃한 쌀떡볶이">Chewy Korean rice cakes with special signature sauce</p>
        </div>
      </div>"""

if h_menu_orig in h:
    h = h.replace(h_menu_orig, h_menu_new)
    print("Home signature menus replaced successfully")
else:
    print("WARNING: Home signature menu block mismatch")

# 4. Proven in Korea images
h_kr_orig = """        <div class="grid g-21" style="gap:12px">
          <div class="ph" style="grid-row:span 3;min-height:320px"><span>KOREA STORE — MAIN</span></div>
          <div class="ph"><span>STORE 2</span></div>
          <div class="ph"><span>STORE 3</span></div>
          <div class="ph"><span>STORE 4</span></div>
        </div>"""

h_kr_new = """        <div class="grid g-21" style="gap:12px">
          <div class="ph" style="grid-row:span 3;min-height:320px;background:url('img/store_kr1.jpg') center/cover;"><span style="background:rgba(0,0,0,0.6);color:#fff;border-radius:3px;">Korea Store #1</span></div>
          <div class="ph" style="background:url('img/store_kr2.jpg') center/cover;"><span style="background:rgba(0,0,0,0.6);color:#fff;border-radius:3px;">Store #2</span></div>
          <div class="ph" style="background:url('img/store_kr3.jpg') center/cover;"><span style="background:rgba(0,0,0,0.6);color:#fff;border-radius:3px;">Store #3</span></div>
          <div class="ph" style="background:url('img/store_kr4.jpg') center/cover;"><span style="background:rgba(0,0,0,0.6);color:#fff;border-radius:3px;">Store #4</span></div>
        </div>"""

if h_kr_orig in h:
    h = h.replace(h_kr_orig, h_kr_new)
    print("Home korea store photos replaced")
else:
    print("WARNING: Home korea store block mismatch")

# 5. Factory photo
h = h.replace('<div class="ph" style="aspect-ratio:16/9"><span>▶ FACTORY VIDEO (YouTube embed)</span></div>', '<div class="ph" style="aspect-ratio:16/9;background:url(\'img/factory.jpg\') center/cover;"><span style="background:rgba(0,0,0,0.65);color:#fff;padding:6px 12px;border-radius:4px;">LFL Own Ingredient & Sauce Factory in Korea</span></div>')
h = h.replace('<div class="ph" style="aspect-ratio:16/9"><span>▶ FACTORY TOUR VIDEO</span></div>', '<div class="ph" style="aspect-ratio:16/9;background:url(\'img/factory.jpg\') center/cover;"><span style="background:rgba(0,0,0,0.65);color:#fff;padding:6px 12px;border-radius:4px;">LFL Own Ingredient & Sauce Factory in Korea</span></div>')

# 6. Certifications
h_certs_orig = """      <div class="grid g4 mt24">
        <div class="card center"><div class="ph" style="aspect-ratio:3/4"><span>CERTIFICATE IMG<br>(click to zoom)</span></div><h3 class="mt16">HACCP</h3><p class="small muted">[Issuer] · No. [ ]<br>Valid until [ ]</p></div>
        <div class="card center"><div class="ph" style="aspect-ratio:3/4"><span>CERTIFICATE IMG</span></div><h3 class="mt16">ISO 22000 / FSSC 22000</h3><p class="small muted">[Issuer] · No. [ ]<br>Valid until [ ]</p></div>
        <div class="card center"><div class="ph" style="aspect-ratio:3/4"><span>CERTIFICATE IMG</span></div><h3 class="mt16">[Cert 3]</h3><p class="small muted">[Issuer] · No. [ ]<br>Valid until [ ]</p></div>
        <div class="card center"><div class="ph" style="aspect-ratio:3/4"><span>CERTIFICATE IMG</span></div><h3 class="mt16">[Cert 4]</h3><p class="small muted">[Issuer] · No. [ ]<br>Valid until [ ]</p></div>
      </div>"""

h_certs_new = """      <div class="grid g4 mt24">
        <div class="card center"><div class="ph" style="aspect-ratio:3/4;background:url('img/cert1.jpg') center/cover;"></div><h3 class="mt16">HACCP Certified</h3><p class="small muted" data-ko="식품의약품안전처 안전관리인증">Korea Food Safety Management</p></div>
        <div class="card center"><div class="ph" style="aspect-ratio:3/4;background:url('img/cert2.jpg') center/cover;"></div><h3 class="mt16">Quality & Hygiene</h3><p class="small muted" data-ko="제조시설 품질규격 인증">Manufacturing Standard Certification</p></div>
        <div class="card center"><div class="ph" style="aspect-ratio:3/4;background:url('img/brand_data.jpg') center/contain;background-repeat:no-repeat;background-color:#fff;"></div><h3 class="mt16">Brand Identity</h3><p class="small muted" data-ko="CHITOPIA 공식 상표 및 디자인">Official Trademark & Design</p></div>
        <div class="card center"><div class="ph" style="aspect-ratio:3/4;background:url('img/logo.png') center/contain;background-repeat:no-repeat;background-color:#fff;"></div><h3 class="mt16">LFL Korean Roots</h3><p class="small muted" data-ko="한국 본사 직영 제조 표준">LFL Korea Direct Standards</p></div>
      </div>"""

if h_certs_orig in h:
    h = h.replace(h_certs_orig, h_certs_new)
    print("Certifications replaced")
else:
    print("WARNING: certs block mismatch")

# 7. Brand Story text from LFL plan
h = h.replace('<h2 data-ko="[브랜드 스토리 헤드라인]">[Brand Story Headline]</h2>', '<h2 data-ko="한국의 맛을 필리핀 식탁에">Korean Flavors for Filipino Tables</h2>')
h = h.replace('<p class="small muted mt8" data-ko="창업 연도, 창업 배경, 한국 성장 과정 (3~4문단)">Founding year, origin, growth in Korea (3–4 paragraphs)</p>', '<p class="small muted mt8" data-ko="치토피아는 한국 본사 LFL이 전개하는 K-푸드 프랜차이즈 브랜드입니다. 한국에서 두 개의 성공적인 외식 브랜드와 소스·파우더 등 원부자재를 생산하는 자체 직영 제조 공장을 운영해왔습니다.">CHITOPIA is a Korean food franchise brand developed by LFL. In Korea, LFL operates two established restaurant brands and its own manufacturing facility producing sauces, coating mixes, and core ingredients.</p>')
h = h.replace('<div class="ph" style="aspect-ratio:4/3"><span>FOUNDER / HERITAGE IMAGE</span></div>', '<div class="ph" style="aspect-ratio:4/3;background:url(\'img/brand_data.jpg\') center/contain;background-repeat:no-repeat;background-color:#fff;"></div>')

# 8. Store PH note (Under construction)
h_store_ph_note = """        <div class="store on" data-pin="1">
          <span class="tag" style="background:#fff3cd;color:#856404;border-color:#ffeeba;" data-ko="오픈 준비 중 (현재 공사 진행)">Under Construction</span>
          <h3 class="mt8" data-ko="치토피아 마켓! 마켓! – 푸드코트 4층 (몰 내부)">CHITOPIA Market! Market! – 4F Food Court (Inside Mall)</h3>
          <p class="small muted">Market! Market! Food Court, 4th Floor, Bonifacio Global City, Taguig</p>
          <p class="small mt8" data-ko="🚧 현재 인테리어 공사 중이며, 오픈 일정은 확정 후 공지됩니다.">🚧 Currently under store fit-out. Opening date will be announced soon.</p>
          <div class="row mt8"><span class="tag">Food Court Format</span><span class="tag">Dine-in / Take-out</span></div>
        </div>
        <div class="store" data-pin="2">
          <span class="tag" style="background:#fff3cd;color:#856404;border-color:#ffeeba;" data-ko="오픈 준비 중 (현재 공사 진행)">Under Construction</span>
          <h3 class="mt8" data-ko="치토피아 마켓! 마켓! – 1층 (몰 외부)">CHITOPIA Market! Market! – G/F (Outside Mall)</h3>
          <p class="small muted">Ground Floor (Outside Mall Entrance), Market! Market!, Bonifacio Global City, Taguig</p>
          <p class="small mt8" data-ko="🚧 현재 인테리어 공사 중이며, 오픈 일정은 확정 후 공지됩니다.">🚧 Currently under store fit-out. Opening date will be announced soon.</p>
          <div class="row mt8"><span class="tag">Street Level</span><span class="tag">Take-out / Delivery</span></div>
        </div>"""

h_store_orig = """        <div class="store on" data-pin="1">
          <span class="tag" data-ko="영업 중">Open Now</span>
          <h3 class="mt8" data-ko="[브랜드] 마켓! 마켓! – 몰 내부 4층">[Brand] Market! Market! – 4F (Inside Mall)</h3>
          <p class="small muted">[Unit No. TBD], 4th Floor, Market! Market!, Bonifacio Global City, Taguig</p>
          <p class="small mt8">🕘 [10:00 – 22:00] · 📞 [ ]</p>
          <div class="row mt8"><span class="tag" data-ko="매장 식사">Dine-in</span><span class="tag" data-ko="포장">Take-out</span><span class="tag" data-ko="배달">Delivery</span></div>
          <div class="row mt16"><a class="btn sm" data-ko="길찾기">Directions</a><a class="btn sm" data-ko="전화">Call</a><a class="btn sm">GrabFood</a></div>
        </div>
        <div class="store" data-pin="2">
          <span class="tag" data-ko="영업 중">Open Now</span>
          <h3 class="mt8" data-ko="[브랜드] 마켓! 마켓! – 몰 외부 1층">[Brand] Market! Market! – G/F (Outside Mall)</h3>
          <p class="small muted">[Unit No. TBD], Ground Floor (outside), Market! Market!, Bonifacio Global City, Taguig</p>
          <p class="small mt8">🕘 [10:00 – 22:00] · 📞 [ ]</p>
          <div class="row mt8"><span class="tag" data-ko="매장 식사">Dine-in</span><span class="tag" data-ko="포장">Take-out</span><span class="tag" data-ko="배달">Delivery</span></div>
          <div class="row mt16"><a class="btn sm" data-ko="길찾기">Directions</a><a class="btn sm" data-ko="전화">Call</a><a class="btn sm">GrabFood</a></div>
        </div>"""

if h_store_orig in h:
    h = h.replace(h_store_orig, h_store_ph_note)
    print("Store PH under construction applied")
else:
    print("WARNING: store PH block mismatch")

# 9. Menu grid generator in JS update
menu_js_orig = """// ---------- Menu placeholder grid ----------
const grid = document.getElementById('menuGrid');
for (let i = 1; i <= 8; i++) {
  grid.insertAdjacentHTML('beforeend',
    `<div class="card"><div class="ph" style="aspect-ratio:1"><span>MENU IMG ${i}</span></div>
     <div class="row mt16">${i<=2?'<span class="tag">Best Seller</span>':''}<span class="tag">🌶 ${i%4}/3</span></div>
     <h3 class="mt8">[Menu Name ${i}]</h3><p class="small muted">[한글 메뉴명]</p>
     <div class="line w80"></div><div class="line w60"></div></div>`);
}"""

menu_js_new = """// ---------- Menu Real Items Grid ----------
const menuData = [
  { name: 'Classic Fried Chicken', ko: '클래식 프라이드 치킨', tag: 'Signature', spice: 0, img: 'img/menu_classic_chicken.jpg', desc: '황금빛 겉바속촉 순살 치킨과 라이스 & 그레이비' },
  { name: 'Creamy Onion Chicken', ko: '크리미 어니언 치킨', tag: 'Best Seller', spice: 0, img: 'img/menu_creamy_onion.jpg', desc: '신선한 양파 슬라이스와 특제 화이트 크리미 소스' },
  { name: 'Soy Garlic Gangjeong', ko: '소이 갈릭 닭강정', tag: 'Popular', spice: 1, img: 'img/menu_soy_chicken.jpg', desc: '단짠 소이 소스로 코팅된 한국 정통 닭강정' },
  { name: 'Cheese Rolling Gangjeong', ko: '치즈 굴림 강정', tag: 'Kids Favorite', spice: 0, img: 'img/menu_cheese_chicken.jpg', desc: '눈꽃 치즈 시즈닝이 듬뿍 뿌려진 달콤고소한 치킨' },
  { name: 'Chicken & Takoyaki Combo', ko: '치킨 & 타코야키 콤보', tag: 'Combo Meal', spice: 0, img: 'img/menu_takoyaki.jpg', desc: '치킨 4조각 + 타코야키 4개 + 밥으로 구성된 실속 콤보' },
  { name: 'Classic Rice Tteokbokki', ko: '빠사시 쌀 떡볶이', tag: 'K-Street Food', spice: 2, img: 'img/menu_tteokbokki.jpg', desc: '쫀득한 쌀떡과 한국 직송 특제 매콤달콤 소스' },
  { name: 'Kimchi Fried Rice Bowl', ko: '돌솥 김치 볶음밥', tag: 'Rice Meal', spice: 2, img: 'img/menu_fried_rice.jpg', desc: '새콤한 김치와 고소한 밥의 조화로운 한국식 한 끼' },
  { name: 'Cup Gangjeong & Tteokbokki', ko: '컵강정 & 컵떡볶이 세트', tag: 'Snack Set', spice: 1, img: 'img/menu_cup_combo.jpg', desc: '간편하게 길거리에서 즐기는 컵 치킨과 컵 떡볶이 세트' }
];

const grid = document.getElementById('menuGrid');
menuData.forEach(m => {
  grid.insertAdjacentHTML('beforeend',
    `<div class="card">
       <div class="ph" style="aspect-ratio:1;background:url('${m.img}') center/cover;"></div>
       <div class="row mt16">
         <span class="tag">${m.tag}</span>
         <span class="tag">${'🌶 '.repeat(m.spice) || 'Mild'}</span>
       </div>
       <h3 class="mt8" data-ko="${m.ko}">${m.name}</h3>
       <p class="small muted" data-ko="${m.desc}">${m.desc}</p>
     </div>`);
});"""

if menu_js_orig in h:
    h = h.replace(menu_js_orig, menu_js_new)
    print("Menu grid JS replaced successfully")
else:
    print("WARNING: menu_js_orig mismatch")

with open(p, "w", encoding="utf-8") as f:
    f.write(h)

print("index.html fully updated!")
