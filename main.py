import os
import sys
from core.ui_helper import show_banner, get_color
from core.text_engine import generate_ascii_text, list_fonts
from core.image_engine import convert_image_to_ascii

def save_to_file(content, folder="output", prefix="ascii"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    import datetime
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{folder}/{prefix}_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        # Simpan teks murni tanpa kode warna terminal
        f.write(content)
    print(f"\n[✔] Hasil disimpan ke: {filename}")

def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        show_banner()
        
        print("Pilih Mode Generator:")
        print("1. Teks ASCII (Multi-Font & Warna)")
        print("2. Gambar ke ASCII (Image Converter)")
        print("3. Lihat Daftar Font Populer")
        print("0. Keluar")
        
        choice = input("\nMasukkan pilihan (0-3): ")

        if choice == "1":
            text = input("Masukkan teks: ")
            print(f"Font saran: {', '.join(list_fonts())}")
            font = input("Masukkan nama font (default 'slant'): ") or "slant"
            color = input("Pilih warna (red/green/blue/yellow/cyan/magenta/white): ") or "white"
            
            result = generate_ascii_text(text, font, color)
            print("\nHasil:\n" + result)
            
            save_opt = input("\nSimpan hasil ke file? (y/n): ")
            if save_opt.lower() == 'y':
                # Generate ulang tanpa warna untuk file teks
                raw_result = generate_ascii_text(text, font, "white")
                save_to_file(raw_result, prefix="text")

        elif choice == "2":
            img_path = input("Masukkan path/lokasi gambar (contoh: foto.jpg): ")
            width = input("Masukkan lebar karakter (default 100): ") or 100
            
            print("\nSedang memproses gambar...")
            ascii_img = convert_image_to_ascii(img_path, int(width))
            print("\nHasil:\n" + ascii_img)
            
            save_opt = input("\nSimpan hasil ke file? (y/n): ")
            if save_opt.lower() == 'y':
                save_to_file(ascii_img, prefix="image")

        elif choice == "3":
            print("\nDaftar Font Populer:")
            for f in list_fonts():
                print(f"- {f}")
            input("\nTekan Enter untuk kembali...")

        elif choice == "0":
            print("Sampai jumpa, Bos!")
            break
        
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Program ditutup.")
        sys.exit()
