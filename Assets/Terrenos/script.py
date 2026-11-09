import numpy as np
from PIL import Image, ImageFilter

# 1. Abrir la elevacion
img = Image.open("Height Map PNG.png").convert("L")
img_2049 = img.resize((2049, 2049), Image.Resampling.BICUBIC)

# 2. Suavizado para eliminar terrazas (radius=2.0 a 2.5 funde escalones de 8 bits)
img_smooth = img_2049.filter(ImageFilter.GaussianBlur(radius=2.2))

# 3. Exportar a 16-bit
arr = np.array(img_smooth, dtype=np.float32)
arr = (arr - arr.min()) / (arr.max() - arr.min()) * 65535.0
arr_16 = arr.astype(np.uint16)

with open("RockyLand_2049_Grayscale.raw", "wb") as f:
    arr_16.astype("<u2").tofile(f)