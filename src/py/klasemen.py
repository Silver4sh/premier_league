from collections import defaultdict

def hitung_statistik(pertandingan):
    """Menghitung poin klasemen berdasarkan hasil pertandingan."""
    klasemen = defaultdict(int)

    for match in pertandingan:
        tim_kandang, tim_tandang = match["HomeTeam"], match["AwayTeam"]
        gol_kandang, gol_tandang = match["FTHG"], match["FTAG"]

        if gol_kandang > gol_tandang:
            klasemen[tim_kandang] += 3 
        elif gol_tandang > gol_kandang:
            klasemen[tim_tandang] += 3  
        else:
            klasemen[tim_kandang] += 1 
            klasemen[tim_tandang] += 1

    return dict(sorted(klasemen.items(), key=lambda x: x[1], reverse=True))

def update_klasemen_dengan_prediksi(klasemen, prediksi):
    """Mengupdate klasemen berdasarkan hasil prediksi pertandingan."""
    for match in prediksi:
        tim_kandang, tim_tandang = match["HomeTeam"], match["AwayTeam"]
        gol_kandang, gol_tandang = match["FTHG"], match["FTAG"]

        if gol_kandang > gol_tandang:
            klasemen[tim_kandang] += 3
        elif gol_tandang > gol_kandang:
            klasemen[tim_tandang] += 3
        else:
            klasemen[tim_kandang] += 1
            klasemen[tim_tandang] += 1

    return dict(sorted(klasemen.items(), key=lambda x: x[1], reverse=True))

def tampilkan_klasemen(klasemen):
    """Mengembalikan tabel klasemen sebagai string dengan format yang rapi."""
    result = "\n🏆 Klasemen Liga Inggris 🏆\n"
    result += "=" * 40 + "\n"
    result += f"{'Pos':<5}{'Tim':<20}{'Poin':<5}\n"
    result += "-" * 40 + "\n"

    for i, (tim, poin) in enumerate(klasemen.items(), 1):
        result += f"{i:<5}{tim:<20}{poin:<5}\n"

    result += "=" * 40 + "\n"
    return result
