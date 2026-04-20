# Pazarlama Metrik Tanımları ve Formüller

## Temel KPI Formülleri

| Metrik | Formül | Notlar |
|--------|--------|--------|
| **CTR** (Tıklama Oranı) | `tıklamalar / gösterimler × 100` | % olarak ifade edilir |
| **CPC** (Tıklama Başına Maliyet) | `maliyet / tıklamalar` | Para birimi |
| **CPA** (Edinim Başına Maliyet) | `maliyet / dönüşümler` | Para birimi |
| **ROAS** (Reklam Harcaması Getirisi) | `gelir / maliyet` | Çarpan (örn. 3.5x) |
| **Dönüşüm Oranı** | `dönüşümler / oturumlar × 100` | % olarak ifade edilir |
| **CPM** (Bin Gösterim Maliyeti) | `maliyet / gösterimler × 1000` | Para birimi |

---

## Gruplandırma Anahtarları

### Tarih Gruplandırması
- Günlük: `date` sütunu (YYYY-MM-DD formatı beklenir)
- Haftalık: 7 günlük pencere (Pazartesi başlangıç)
- Aylık: yıl-ay birleşimi

### Kanal Gruplandırması
- `channel` sütunu
- Beklenen değerler: `google`, `facebook`, `instagram`, `email`, `organic`, `direct`, vb.

### Kampanya Gruplandırması
- `campaign` sütunu
- Kanal + kampanya birleşimi ile hiyerarşik sıralama

---

## Beklenen CSV Sütunları

| Sütun | Tür | Zorunlu | Açıklama |
|-------|-----|---------|----------|
| `date` | date | ✅ | YYYY-MM-DD |
| `channel` | string | ✅ | Trafik kaynağı |
| `campaign` | string | ✅ | Kampanya adı |
| `impressions` | int | ❌ | Gösterim sayısı |
| `clicks` | int | ❌ | Tıklama sayısı |
| `cost` | float | ❌ | Harcama |
| `revenue` | float | ❌ | Gelir |
| `conversions` | int | ❌ | Dönüşüm sayısı |
| `sessions` | int | ❌ | Oturum sayısı |

---

## Uyarı Eşikleri

### 🔴 Kırmızı Alarm: Verimsiz Harcama
**Koşul:** `ROAS < 1.2`
**Anlamı:** Her 1 TL harcamaya karşılık 1.2 TL'den az gelir üretiliyor.
**Eylem:** Hemen harcamayı durdur veya hedeflemeyi gözden geçir.

### ⚠️ Dikkat: CPA Ani Artışı
**Koşul:** `CPA_bugün > CPA_7günlük_ortalama × 1.30`
**Anlamı:** Edinim maliyeti son 7 güne göre %30+ arttı.
**Eylem:** Teklif stratejisi ve kitle hedeflemesini kontrol et.

---

## Anomali Tespiti

### Yöntem: 7 Günlük Hareketli Ortalama
```
Anomali = |değer - 7g_ortalama| > 2 × 7g_standart_sapma
```
- Ani artış: değer > ortalama + 2σ
- Ani düşüş: değer < ortalama - 2σ

### Minimum Veri Gereksinimi
- Anomali tespiti için: en az **8 günlük** veri
- Güvenilir trend analizi için: en az **30 günlük** veri

---

## Performans Değerlendirme Rehberi

| Metrik | Kötü | Orta | İyi | Mükemmel |
|--------|------|------|-----|----------|
| ROAS | < 1.2 | 1.2–2.0 | 2.0–4.0 | > 4.0 |
| CTR (Google Ads) | < 1% | 1–3% | 3–5% | > 5% |
| Dönüşüm Oranı | < 1% | 1–3% | 3–5% | > 5% |
