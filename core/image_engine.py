from PIL import Image

# Karakter berdasarkan tingkat kegelapan pixel
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  # Penyesuaian aspek ratio karakter
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"Gagal membuka gambar: {e}"

    image = resize_image(image, new_width)
    image = grayify(image)
    
    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:(index + new_width)] for index in range(0, pixel_count, new_width)])
    
    return ascii_img
