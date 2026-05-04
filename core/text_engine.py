import pyfiglet
from core.ui_helper import get_color

def generate_ascii_text(text, font="slant", color="white"):
    try:
        # Generate ASCII menggunakan pyfiglet
        fig = pyfiglet.Figlet(font=font)
        ascii_art = fig.renderText(text)
        
        # Beri warna
        colored_art = f"{get_color(color)}{ascii_art}"
        return colored_art
    except Exception as e:
        return f"Error: {str(e)}"

def list_fonts():
    # Menampilkan beberapa font populer sebagai saran
    return ["slant", "block", "caligraphy", "doh", "isometric1", "alligator", "bubble"]
