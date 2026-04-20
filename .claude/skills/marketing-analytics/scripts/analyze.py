#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analyze.py — Pazarlama CSV analiz betiği.
Kullanım: python3 analyze.py <CSV_PATH>
Çıktı: JSON veri paketi
"""

import sys
import io
import json
import csv
from collections import defaultdict

# Windows stdout encoding fix
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def safe_float(val, default=0.0):
    try:
        return float(val) if val not in (None, "", "N/A", "n/a") else default
    except (ValueError, TypeError):
        return default


def safe_int(val, default=0):
    try:
        return int(float(val)) if val not in (None, "", "N/A", "n/a") else default
    except (ValueError, TypeError):
        return default


def calc_metrics(impressions, clicks, cost, revenue, conversions, sessions):
    ctr = (clicks / impressions * 100) if impressions > 0 else None
    cpc = (cost / clicks) if clicks > 0 else None
    cpa = (cost / conversions) if conversions > 0 else None
    roas = (revenue / cost) if cost > 0 else None
    conv_rate = (conversions / sessions * 100) if sessions > 0 else None
    return {
        "impressions": impressions,
        "clicks": clicks,
        "cost": round(cost, 2),
        "revenue": round(revenue, 2),
        "conversions": conversions,
        "sessions": sessions,
        "CTR": round(ctr, 2) if ctr is not None else None,
        "CPC": round(cpc, 2) if cpc is not None else None,
        "CPA": round(cpa, 2) if cpa is not None else None,
        "ROAS": round(roas, 2) if roas is not None else None,
        "ConversionRate": round(conv_rate, 2) if conv_rate is not None else None,
    }


def load_csv(path):
    rows = []
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append({k.strip().lower(): v.strip() for k, v in row.items()})
    except FileNotFoundError:
        return None, f"Dosya bulunamadı: {path}"
    except Exception as e:
        return None, str(e)
    return rows, None


def detect_anomalies(daily_data):
    """7-day moving average anomaly detection."""
    anomalies = []
    metrics_to_check = ["CPA", "ROAS", "CTR"]
    dates_sorted = sorted(daily_data.keys())

    if len(dates_sorted) < 8:
        return [], "yetersiz_veri"

    for metric in metrics_to_check:
        values = [(d, daily_data[d].get(metric)) for d in dates_sorted if daily_data[d].get(metric) is not None]
        if len(values) < 8:
            continue

        for i in range(7, len(values)):
            window = [v for _, v in values[i-7:i]]
            avg = sum(window) / len(window)
            std = (sum((x - avg) ** 2 for x in window) / len(window)) ** 0.5
            date, current = values[i]

            if std > 0 and abs(current - avg) > 2 * std:
                direction = "artis" if current > avg else "dusus"
                pct_change = abs((current - avg) / avg * 100) if avg != 0 else 0
                anomalies.append({
                    "date": date,
                    "metric": metric,
                    "direction": direction,
                    "current": current,
                    "7d_avg": round(avg, 2),
                    "pct_change": round(pct_change, 1),
                })

    return anomalies, None


def analyze(path):
    rows, err = load_csv(path)
    if err:
        return {"error": err}

    if not rows:
        return {"error": "CSV dosyası boş veya okunamadı."}

    # Aggregators
    totals = defaultdict(float)
    by_channel = defaultdict(lambda: defaultdict(float))
    by_campaign = defaultdict(lambda: defaultdict(float))
    by_date = defaultdict(lambda: defaultdict(float))

    for row in rows:
        imp  = safe_int(row.get("impressions", 0))
        clk  = safe_int(row.get("clicks", 0))
        cost = safe_float(row.get("cost", 0))
        rev  = safe_float(row.get("revenue", 0))
        conv = safe_int(row.get("conversions", 0))
        sess = safe_int(row.get("sessions", 0))
        ch   = row.get("channel", "unknown")
        camp = row.get("campaign", "unknown")
        date = row.get("date", "unknown")

        for agg, key in [(totals, None), (by_channel[ch], None), (by_campaign[f"{ch}|{camp}"], None), (by_date[date], None)]:
            agg["impressions"] += imp
            agg["clicks"]      += clk
            agg["cost"]        += cost
            agg["revenue"]     += rev
            agg["conversions"] += conv
            agg["sessions"]    += sess

    # Overview
    t = totals
    overview = calc_metrics(t["impressions"], t["clicks"], t["cost"], t["revenue"], t["conversions"], t["sessions"])
    date_range = {"start": min(by_date.keys()), "end": max(by_date.keys())} if by_date else {}

    # By channel
    channels_out = {}
    for ch, d in by_channel.items():
        channels_out[ch] = calc_metrics(d["impressions"], d["clicks"], d["cost"], d["revenue"], d["conversions"], d["sessions"])

    # By campaign
    campaigns_out = {}
    for key, d in by_campaign.items():
        campaigns_out[key] = calc_metrics(d["impressions"], d["clicks"], d["cost"], d["revenue"], d["conversions"], d["sessions"])

    # Daily metrics for anomaly detection
    daily_metrics = {}
    for date, d in by_date.items():
        daily_metrics[date] = calc_metrics(d["impressions"], d["clicks"], d["cost"], d["revenue"], d["conversions"], d["sessions"])

    anomalies, anomaly_status = detect_anomalies(daily_metrics)

    # Alerts
    alerts = []

    # Overall ROAS check
    if overview.get("ROAS") is not None and overview["ROAS"] < 1.2:
        alerts.append({
            "level": "RED",
            "message": f"🔴 Kırmızı uyarı: verimsiz harcama — genel ROAS={overview['ROAS']} (esik: 1.2)"
        })

    # Per-channel ROAS check (only paid channels with cost > 0)
    for ch, m in channels_out.items():
        if m.get("cost", 0) > 0 and m.get("ROAS") is not None and m["ROAS"] <= 1.2:
            alerts.append({
                "level": "RED",
                "message": f"🔴 Kırmızı uyarı: verimsiz harcama — '{ch}' kanalı ROAS={m['ROAS']} (esik: 1.2)"
            })

    # CPA spike check (latest day vs 7d avg)
    sorted_dates = sorted(daily_metrics.keys())
    if len(sorted_dates) >= 8:
        last = sorted_dates[-1]
        prev_7 = sorted_dates[-8:-1]
        cpa_vals = [daily_metrics[d]["CPA"] for d in prev_7 if daily_metrics[d].get("CPA") is not None]
        cpa_today = daily_metrics[last].get("CPA")
        if cpa_vals and cpa_today is not None:
            avg_cpa = sum(cpa_vals) / len(cpa_vals)
            if avg_cpa > 0 and cpa_today > avg_cpa * 1.30:
                pct = round((cpa_today - avg_cpa) / avg_cpa * 100, 1)
                alerts.append({
                    "level": "WARNING",
                    "message": f"⚠️ Dikkat: CPA'da ani artış — bugun={cpa_today}, 7g_ort={round(avg_cpa, 2)}, artis=%{pct}"
                })

    # Top 5 actions (rule-based)
    actions = []
    # Sort channels by ROAS desc
    sorted_channels = sorted(channels_out.items(), key=lambda x: x[1].get("ROAS") or 0, reverse=True)
    if sorted_channels:
        best_ch = sorted_channels[0][0]
        worst_ch = sorted_channels[-1][0] if len(sorted_channels) > 1 else None
        if sorted_channels[0][1].get("ROAS", 0) > 2:
            actions.append(f"'{best_ch}' kanalı yüksek ROAS ({sorted_channels[0][1]['ROAS']}x) — bütçeyi artır.")
        if worst_ch and (sorted_channels[-1][1].get("ROAS") or 0) < 1.2:
            actions.append(f"'{worst_ch}' kanalı düşük ROAS ({sorted_channels[-1][1].get('ROAS')}) — harcamayı durdur veya gözden geçir.")

    # Sort campaigns by CPA asc (best performers)
    sorted_camps = sorted(
        [(k, v) for k, v in campaigns_out.items() if v.get("CPA") is not None],
        key=lambda x: x[1]["CPA"]
    )
    if sorted_camps:
        best_camp_key = sorted_camps[0][0].split("|")[-1]
        actions.append(f"En düşük CPA'lı kampanya '{best_camp_key}' — benzer kampanyaları çoğalt.")

    if overview.get("CTR") and overview["CTR"] < 1.0:
        actions.append("Genel CTR %1'in altında — reklam yaratıcılarını ve hedeflemeyi test et.")

    if overview.get("ConversionRate") and overview["ConversionRate"] < 1.0:
        actions.append("Dönüşüm oranı %1'in altında — açılış sayfası A/B testi önceliklendir.")

    while len(actions) < 5:
        actions.append("Ek veri toplayarak analizi derinleştir.")

    return {
        "date_range": date_range,
        "overview": overview,
        "by_channel": channels_out,
        "by_campaign": campaigns_out,
        "anomalies": anomalies,
        "anomaly_status": anomaly_status,
        "alerts": alerts,
        "top_actions": actions[:5],
        "row_count": len(rows),
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "CSV yolu gerekli. Kullanım: python3 analyze.py <CSV_PATH>"}))
        sys.exit(1)

    result = analyze(sys.argv[1])

    # Print alerts at the very top before JSON
    if result.get("alerts"):
        print("\n" + "=" * 60)
        for a in result["alerts"]:
            print(a["message"])
        print("=" * 60 + "\n")

    print(json.dumps(result, ensure_ascii=False, indent=2))
