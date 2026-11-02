#!/usr/bin/env python3
# Kedi Miyav Parlamentosu
# Kediler oylar, insanlar şaşırır. Gerçek demokrasi (kedi tarzı).
# Gizli: bazen oylar sayılmaz ama miyavlar sayılır.

import random
import time

def kedi_oylamasi():
    print("🐱 KEDİ MİYAV PARLAMENTOSU AÇILDI 🐱")
    print("Bugünkü gündem: Mama miktarı artırılsın mı?")
    kediler = ["Tekir", "Sarıman", "Boncuk", "Pamuk", "Miyav Bey"]
    oylar = {}
    
    for kedi in kediler:
        oy = random.choice(["Miyav (Evet)", "Hısss (Hayır)", "Mırıldanma (Kararsız)"])
        oylar[kedi] = oy
        print(f"{kedi}: {oy}")
        time.sleep(0.8)
    
    evet = sum(1 for o in oylar.values() if "Evet" in o)
    print(f"\nSonuç: {evet} evet oy. Mama artacak! (Ya da artmayacak, kedi keyfine göre.)")
    print("Damga: Grok Kayyum - 02.11.2026 - Tentivory")
    # gizli_siyasi: "seçim sonuçları her zaman beklendiği gibi çıkar, değil mi?"

if __name__ == "__main__":
    kedi_oylamasi()
