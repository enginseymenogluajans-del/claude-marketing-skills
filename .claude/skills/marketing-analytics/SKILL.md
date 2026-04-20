---
name: marketing-analytics
description: Use when the user asks to analyze marketing data, upload a CSV for analysis, calculate marketing KPIs, review campaign performance, or generate a marketing report. Trigger keywords: marketing analytics, CSV analysis, KPI report, ROAS, CPA, CTR, campaign performance, channel analysis, marketing-analytics. Takes a CSV file and returns KPIs, channel/campaign rankings, anomaly detection, and top 5 actions.
---

# Pazarlama Analizleri

## Overview
Yüklenen bir CSV dosyasını alır, pazarlama KPI'larını hesaplar, kanal/kampanya bazında sıralar, anomalileri tespit eder ve eylem listesi üretir. ROAS < 1.2 veya CPA ani artışı gibi kritik eşikler için uyarı gösterir.

## Steps

1. **CSV Dosyasını Al** — Kullanıcıdan CSV dosyasını veya dosya yolunu al.

2. **Analiz Betiğini Çalıştır**:
   ```bash
   python3 .claude/skills/marketing-analytics/scripts/analyze.py <CSV_PATH>
   ```
   Çıktı: JSON veri paketi (genel bakış, kanal bazlı, kampanya bazlı, anomaliler, eylemler).

3. **Metrics Referansını Oku** — `references/metrics.md` dosyasını oku. Formülleri ve eşikleri içselleştir.

4. **Uyarıları Değerlendir** — Betik çıktısındaki uyarı listesini kontrol et:
   - ROAS < 1.2 → **🔴 Kırmızı Alarm: Verimsiz Harcama**
   - CPA 7 günlük ortalamaya göre %30+ artış → **⚠️ Dikkat: CPA'da Ani Artış**

5. **Markdown Rapor Üret** — Aşağıdaki şablona göre. Veri yoksa "veri yok" yaz, çıkarım yapma.

6. **Top 5 Eylem** — Veriden türetilmiş, gerekçeli 5 somut eylem öner.

## Output Format

```markdown
# Pazarlama Analiz Raporu
**Dönem:** [tarih aralığı]  **Oluşturma:** [tarih]

---

## ⚠️ Uyarılar
[Varsa kırmızı alarm ve dikkat mesajları buraya — yoksa bu bölümü atla]

---

## Özet KPI'lar
| Metrik | Değer |
|--------|-------|
| Toplam Harcama | ... |
| Toplam Gelir | ... |
| ROAS | ... |
| CTR | ...% |
| CPC | ... |
| CPA | ... |
| Dönüşüm Oranı | ...% |

---

## Kanal Performansı
| Kanal | Harcama | Gelir | ROAS | CPA | CTR |
|-------|---------|-------|------|-----|-----|
| ... | ... | ... | ... | ... | ... |

---

## Kampanya Performansı
| Kampanya | Kanal | Harcama | Gelir | ROAS | Dönüşümler |
|----------|-------|---------|-------|------|------------|
| ... | ... | ... | ... | ... | ... |

---

## Anomaliler
[Tespit edilen ani artış/düşüşler — yoksa "Anomali tespit edilmedi"]

---

## Top 5 Eylem
- [ ] **1.** [Eylem] — [Gerekçe, hangi veriye dayanıyor]
- [ ] **2.** ...
- [ ] **3.** ...
- [ ] **4.** ...
- [ ] **5.** ...
```

## Notes
- Eksik sütun varsa o metriği "veri yok" olarak işaretle, hesaplama yapma
- Tüm para birimleri CSV'deki birim ile tutarlı olmalı
- Anomali tespiti için en az 8 günlük veri gerekir; daha azında "yetersiz veri" yaz
- Uyarılar bölümü her zaman raporun en üstünde yer alır
