p = r"d:\01. Chitopia\wireframe\index.html"
with open(p, "r", encoding="utf-8") as f:
    h = f.read()

target = """    <div class="grid g4 mt24">
      <div class="card center"><div class="ph" style="aspect-ratio:3/4"><span>CERTIFICATE IMG<br>(click to zoom)</span></div><h3 class="mt16">HACCP</h3><p class="small muted">[Issuer] · No. [ ]<br>Valid until [ ]</p></div>
      <div class="card center"><div class="ph" style="aspect-ratio:3/4"><span>CERTIFICATE IMG</span></div><h3 class="mt16">ISO 22000 / FSSC 22000</h3><p class="small muted">[Issuer] · No. [ ]<br>Valid until [ ]</p></div>
      <div class="card center"><div class="ph" style="aspect-ratio:3/4"><span>CERTIFICATE IMG</span></div><h3 class="mt16">[Cert 3]</h3><p class="small muted">[Issuer] · No. [ ]<br>Valid until [ ]</p></div>
      <div class="card center"><div class="ph" style="aspect-ratio:3/4"><span>CERTIFICATE IMG</span></div><h3 class="mt16">[Cert 4]</h3><p class="small muted">[Issuer] · No. [ ]<br>Valid until [ ]</p></div>
    </div>"""

replacement = """    <div class="grid g4 mt24">
      <div class="card center"><div class="ph" style="aspect-ratio:3/4;background:url('img/cert1.jpg') center/cover;"></div><h3 class="mt16">HACCP Certified</h3><p class="small muted" data-ko="식품의약품안전처 안전관리인증">Korea Food Safety Management</p></div>
      <div class="card center"><div class="ph" style="aspect-ratio:3/4;background:url('img/cert2.jpg') center/cover;"></div><h3 class="mt16">Quality & Hygiene</h3><p class="small muted" data-ko="제조시설 품질규격 인증">Manufacturing Standard Certification</p></div>
      <div class="card center"><div class="ph" style="aspect-ratio:3/4;background:url('img/brand_data.jpg') center/contain;background-repeat:no-repeat;background-color:#fff;"></div><h3 class="mt16">Brand Identity</h3><p class="small muted" data-ko="CHITOPIA 공식 상표 및 디자인">Official Trademark & Design</p></div>
      <div class="card center"><div class="ph" style="aspect-ratio:3/4;background:url('img/logo.png') center/contain;background-repeat:no-repeat;background-color:#fff;"></div><h3 class="mt16">LFL Korean Roots</h3><p class="small muted" data-ko="한국 본사 직영 제조 표준">LFL Korea Direct Standards</p></div>
    </div>"""

if target in h:
    h = h.replace(target, replacement)
    with open(p, "w", encoding="utf-8") as f:
        f.write(h)
    print("proof-certs replaced successfully")
else:
    print("Failed to match target")
