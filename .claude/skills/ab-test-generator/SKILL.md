---
name: ab-test-generator
description: Use when the user asks to generate A/B test ideas, create A/B tests, run CRO analysis, optimize a webpage, or produce a monthly A/B test report. Trigger keywords: A/B test, split test, CRO, conversion optimization, test hypothesis, ICE score, monthly report, aylık rapor, ab-test-generator. Given a URL, produces 5 prioritized test ideas with ICE scoring, hypotheses, and implementation steps. Also supports monthly sub-flow: past results summary + new suggestions + next sprint plan.
---

# AB Test Oluşturucu

## Overview
Verilen bir URL için yapılandırılmış hipotezler, ICE puanlaması ve uygulama adımlarıyla A/B test fikirleri üretir. Sayfayı kazır (veya özet ister), 5 test fikri oluşturur, ICE puanına göre sıralar ve 2 hızlı kazanımı işaretler.

## Steps

1. **URL Al** — Kullanıcıdan test edilecek URL'yi al.

2. **Sayfayı Analiz Et** — `scripts/scrape_page.py` betiğini çalıştır:
   ```bash
   python3 .claude/skills/ab-test-generator/scripts/scrape_page.py <URL>
   ```
   - Kazıma başarısız olursa kullanıcıdan sayfa içeriği özeti iste.
   - Çıktı: başlıklar, CTA'lar, formlar, görseller listesi.

3. **Methodology Oku** — `references/methodology.md` dosyasını oku. ICE formülünü ve test kategorilerini içselleştir.

4. **5 Test Fikri Üret** — Farklı kategorilerden (Headlines, CTAs, Layout, Copy, Forms, Social Proof) birer fikir üret.

5. **ICE Puanlama** — Her test için Impact, Confidence, Ease (1-10) puanla. ICE = (Impact × Confidence × Ease) / 3.

6. **Sırala ve İşaretle**:
   - ICE puanına göre yüksekten düşüğe sırala.
   - Ease ≥ 8 **ve** Impact ≥ 6 olan 2 testi "Hızlı Kazanım ✅" olarak işaretle.

7. **Varyant Başlıkları** — En yüksek puanlı test için en az 3 başlık/kopya varyantı yaz.

8. **Markdown Rapor Çıktısı** — Aşağıdaki şablonu kullan.

## Output Format

Her test için aşağıdaki yapıyı kullan:

```markdown
## Test [ID]: [Kısa İsim]
**Kategori:** [Headlines / CTAs / Layout / Copy / Forms / Social Proof]
**Hedef:** [Dönüşüm artışı / Tıklama oranı / vb.]

**Hipotez:**
> Eğer [X'i değiştirirsek], o zaman [Y sonucu] olur çünkü [Z gerekçesi].

| | Kontrol | Varyant |
|---|---|---|
| Açıklama | [mevcut] | [önerilen] |

**Uygulama Adımları:**
1. ...
2. ...
3. ...

**Ölçülecek KPI:** [metrik]
**Beklenen Etki:** ~[%X] artış
**ICE Puanı:** Impact=[X] × Confidence=[Y] × Ease=[Z] → **ICE = [sonuç]**
**Hızlı Kazanım:** [Evet ✅ / Hayır]
```

Tüm testlerden önce özet tablo ekle:

```markdown
| # | Test Adı | Kategori | ICE Puanı | Hızlı Kazanım |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |
```

## Notes
- ICE puanı 10 üzerinden değil, 1-1000 aralığında çıkabilir — formül: (I × C × E) / 3
- Kazıma başarısız olursa asla varsayım yapma; kullanıcıdan sayfa içeriği iste
- Test fikirleri birbirinden farklı kategorilerden olmalı

---

## Alt-Akış: Aylık Rapor

**Tetikleyici:** Kullanıcı "aylık rapor", "geçen ay sonuçları", "monthly report" veya benzer bir ifade kullandığında bu alt-akışı uygula.

### Aylık Rapor Adımları

1. **Geçen Ay Verilerini Al** — Kullanıcıdan şunları iste (yoksa "veri yok" yaz):
   - Hangi testler çalıştı? (test adı + süre)
   - Her test için sonuç: kazanan varyant, istatistiksel anlamlılık, lift %
   - Durdurulmuş veya erken sonlandırılmış testler ve sebebi

2. **Özet Üret** — Geçen ayın genel performansını 3-4 cümleyle özetle.

3. **Kazanan/Kaybeden Analizi** — Her test için karar + öğrenilen ders.

4. **Yeni 5 Test Öner** — Önceki ay sonuçlarından öğrenilenleri baz alarak yeni ICE puanlı 5 test fikri üret (standart Steps akışını uygula).

5. **Sonraki Sprint Planı** — Öncelik sırasına göre 2 haftalık sprint planı yaz.

### Aylık Rapor Çıktı Şablonu

```markdown
# Aylık A/B Test Raporu — [Ay Yıl]
**Site:** [URL] | **Tarih:** [YYYY-MM-DD]

---

## Özet
[Geçen ayın 3-4 cümlelik genel değerlendirmesi. Toplam test sayısı, kazanan oran, öne çıkan metrik.]

---

## Kazanan / Kaybeden Deneyler

| Test | Kategori | Sonuç | Lift | Öğrenilen |
|------|----------|-------|------|-----------|
| [Test Adı] | [Kategori] | ✅ Kazandı / ❌ Kaybetti / ⏸ Durdu | +X% / -X% / — | [1 cümle] |

---

## Sonraki Sprint Planı (2 Hafta)

**Hafta 1:**
- [ ] [Yüksek ICE test — uygulama başlat]
- [ ] [Hızlı kazanım — deploy et]

**Hafta 2:**
- [ ] [Orta ICE test — setup tamamla]
- [ ] [Önceki kazanandan türetilen test — hipotez yaz]

---

## Yeni Deney Önerileri
[Standart 5 test + ICE tablosu — önceki ay öğrenimlerine dayalı]
```

### Aylık Rapor Kuralları
- Sonuç verisi yoksa o satıra "veri yok" yaz — tahmin yapma
- Kazanan testlerin öğrenimini bir sonraki testin hipotezine yansıt
- Sprint planında en fazla 4 aktif test — paralel test sayısını sınırla
- Durdurulan testler için sebebi mutlaka yaz (trafik yetersizliği, teknik sorun, vb.)
