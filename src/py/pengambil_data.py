import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def ambil_data_dari_csv(file_csv):
    """Membaca data pertandingan dari file CSV."""
    if not os.path.exists(file_csv):
        logging.error(f"❌ File {file_csv} tidak ditemukan!")
        return None

    try:
        df = pd.read_csv(file_csv)
        logging.info(f"✅ Data berhasil dibaca dari {file_csv}")
        return df
    except Exception as e:
        logging.error(f"❌ Terjadi kesalahan saat membaca CSV: {e}")
        return None
