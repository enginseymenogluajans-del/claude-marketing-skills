# A/B Test Metodolojisi

## ICE Puanlama Çerçevesi

### Formül
```
ICE Skoru = (Impact × Confidence × Ease) / 3
```

### Ölçekler

| Boyut | Ölçek | Açıklama |
|-------|-------|----------|
| **Impact** | 1–10 | Beklenen dönüşüm artışı. 10 = çok yüksek etki (>%20 lift), 1 = ihmal edilebilir |
| **Confidence** | 1–10 | Veriye/araştırmaya dayalı güven. 10 = güçlü kanıt var, 1 = saf tahmin |
| **Ease** | 1–10 | Uygulama kolaylığı. 10 = 1 saatte bitir, 1 = aylar sürer |

### Hızlı Kazanım Kriteri
- Ease **≥ 8** VE Impact **≥ 6** → Hızlı Kazanım ✅
- Toplamda en fazla 2 adet işaretle

### Öncelik Bandları
| ICE Skoru | Öncelik |
|-----------|---------|
| > 200 | Kritik — hemen test et |
| 100–200 | Yüksek |
| 50–100 | Orta |
| < 50 | Düşük |

---

## Test Kategorileri

### 1. Headlines (Başlıklar)
- H1, hero başlığı, değer önerisi metni
- Etki alanı: ilk izlenim, dikkat çekme, değer iletimi
- Örnek değişkenler: uzunluk, ton, fayda vs. özellik odaklı

### 2. CTAs (Harekete Geçirici Mesajlar)
- Buton metni, rengi, boyutu, konumu
- Etki alanı: tıklama oranı, form doldurma
- Örnek değişkenler: "Ücretsiz Dene" vs. "Hemen Başla", renk kontrastı

### 3. Layout (Düzen)
- Bölüm sıralaması, yukarı/aşağı katlama içeriği, ızgara yapısı
- Etki alanı: içerik okunurluğu, sıçrama oranı
- Örnek değişkenler: tek sütun vs. çift sütun, hero görseli konumu

### 4. Copy (Metin)
- Gövde metni, madde işaretleri, güven sinyalleri
- Etki alanı: anlayış, ikna
- Örnek değişkenler: uzun vs. kısa kopya, birinci vs. ikinci şahıs

### 5. Forms (Formlar)
- Alan sayısı, sıra, etiket metni, yer tutucu
- Etki alanı: form tamamlama oranı
- Örnek değişkenler: 5 alan vs. 2 alan, tek adım vs. çok adım

### 6. Social Proof (Sosyal Kanıt)
- Referanslar, derecelendirmeler, müşteri sayıları, logolar
- Etki alanı: güven, kaygı azaltma
- Örnek değişkenler: metin referansı vs. video referansı, konum (hero altı vs. form yanı)

---

## Hipotez Şablonu
```
Eğer [spesifik değişiklik yaparsak],
o zaman [ölçülebilir sonuç] elde ederiz
çünkü [psikolojik/davranışsal gerekçe].
```

## İstatistiksel Güç Gereksinimleri
- Minimum örneklem: her varyant için 1000 ziyaretçi
- Anlamlılık düzeyi: p < 0.05
- Minimum test süresi: 2 hafta (mevsimsel varyasyonu kapsayacak şekilde)
- MDE (Minimum Tespit Edilebilir Etki): %5 veya üzeri için güvenilir
