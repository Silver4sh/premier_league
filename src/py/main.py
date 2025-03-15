import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from prediksi_pertandingan import train_model, prediksi_pertandingan
from pengambil_data import ambil_data_dari_csv
from klasemen import hitung_statistik, tampilkan_klasemen

class PremierLeagueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Premier League App")
        self.root.geometry("500x400")

        self.file_csv = None
        self.model = None
        self.label_encoder = None

        # Judul Aplikasi
        ttk.Label(root, text="⚽ Premier League Predictor ⚽", font=("Arial", 16)).pack(pady=10)

        # Tombol Pilih File CSV
        self.file_button = ttk.Button(root, text="📂 Pilih File CSV", command=self.load_csv)
        self.file_button.pack(pady=5)

        # Label Status File
        self.file_status_label = ttk.Label(root, text="⚠️ Belum ada file CSV yang dimuat!", foreground="red")
        self.file_status_label.pack(pady=5)

        # Menu Pilihan
        self.menu_frame = ttk.Frame(root)
        self.menu_frame.pack(pady=10)

        self.klasemen_button = ttk.Button(self.menu_frame, text="📊 Lihat Klasemen", command=self.show_klasemen, state="disabled")
        self.klasemen_button.grid(row=0, column=0, padx=10)

        self.prediksi_button = ttk.Button(self.menu_frame, text="🔮 Prediksi Pertandingan", command=self.show_prediksi, state="disabled")
        self.prediksi_button.grid(row=0, column=1, padx=10)

    def load_csv(self):
        """Memilih file CSV dan memuat data"""
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        self.file_csv = file_path
        df = ambil_data_dari_csv(file_path)

        if df is None:
            messagebox.showerror("Error", "Gagal membaca file CSV! Pastikan formatnya benar.")
            return

        # Latih model & muat tim
        self.model_away, self.model_home, self.label_encoder = train_model(df)

        self.file_status_label.config(text=f"✅ Data telah dimuat!", foreground="green")
        self.klasemen_button.config(state="normal")
        self.prediksi_button.config(state="normal")

    def show_klasemen(self):
        """Menampilkan klasemen dari CSV yang telah dimuat"""
        df = ambil_data_dari_csv(self.file_csv)
        if df is None:
            messagebox.showerror("Error", "Gagal membaca file CSV!")
            return
    
        klasemen_data = hitung_statistik(df.to_dict(orient="records"))
        
        klasemen_window = tk.Toplevel(self.root)
        klasemen_window.title("📊 Klasemen Premier League")
    
        ttk.Label(klasemen_window, text="🏆 Klasemen Saat Ini 🏆", font=("Arial", 14)).pack(pady=10)
    
        text_area = tk.Text(klasemen_window, height=15, width=50)
        text_area.pack(padx=10, pady=10)
    
        # Ambil hasil klasemen sebagai string dan masukkan ke Text widget
        klasemen_text = tampilkan_klasemen(klasemen_data)
        text_area.insert("end", klasemen_text)
        text_area.config(state="disabled")


    def show_prediksi(self):
        """Menampilkan menu prediksi pertandingan"""
        prediksi_window = tk.Toplevel(self.root)
        prediksi_window.title("🔮 Prediksi Pertandingan")
        prediksi_window.geometry("350x250")

        ttk.Label(prediksi_window, text="🏟️ Tim Kandang:").pack(pady=5)
        home_team_combobox = ttk.Combobox(prediksi_window, state="readonly")
        home_team_combobox.pack()

        ttk.Label(prediksi_window, text="🚀 Tim Tandang:").pack(pady=5)
        away_team_combobox = ttk.Combobox(prediksi_window, state="readonly")
        away_team_combobox.pack()

        # Mengisi dropdown dengan tim yang tersedia
        teams = list(self.label_encoder.classes_)
        home_team_combobox["values"] = teams
        away_team_combobox["values"] = teams

        def predict():
            home_team = home_team_combobox.get()
            away_team = away_team_combobox.get()

            if not home_team or not away_team:
                messagebox.showerror("Error", "Pilih tim kandang dan tandang!")
                return
            if home_team == away_team:
                messagebox.showerror("Error", "Tim tidak boleh sama!")
                return

            result = prediksi_pertandingan(self.model_away, self.model_home, self.label_encoder, home_team, away_team)
            result_label.config(text=f"🔮 Hasil: {result}", foreground="blue")

        # Tombol Prediksi
        predict_button = ttk.Button(prediksi_window, text="🔮 Prediksi Hasil", command=predict)
        predict_button.pack(pady=10)

        # Label Hasil Prediksi
        result_label = ttk.Label(prediksi_window, text="", font=("Arial", 12), foreground="blue")
        result_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PremierLeagueApp(root)
    root.mainloop()
