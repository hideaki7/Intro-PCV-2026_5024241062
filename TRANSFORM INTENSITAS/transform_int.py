import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

def rapikan(nilai):
    """
    Pembulatan setengah ke atas: floor(x + 0.5)
    dan pemotongan rentang ke [0, 255].
    """
    dibulatkan = int(math.floor(nilai + 0.5))
    if dibulatkan < 0:
        return 0
    elif dibulatkan > 255:
        return 255
    return dibulatkan

def terapkan_lut(citra, lut):
    """
    Pemetaan tabel intensitas (LUT) manual menggunakan array indexing.
    """
    lut_arr = np.array(lut, dtype=np.uint8)
    return lut_arr[citra]

def lut_negatif(L=256):
    return [rapikan((L - 1) - r) for r in range(L)]

def lut_log(L=256):
    c = (L - 1) / math.log(L)
    return [rapikan(c * math.log(1 + r)) for r in range(L)]

def lut_gamma(gamma, L=256):
    return [rapikan((L - 1) * ((r / (L - 1)) ** gamma)) for r in range(L)]

def lut_contrast_stretching(r1=80, s1=20, r2=175, s2=240, L=256):
    lut = []
    m1 = s1 / r1
    m2 = (s2 - s1) / (r2 - r1)
    m3 = ((L - 1) - s2) / ((L - 1) - r2)
    
    for r in range(L):
        if r < r1:
            val = m1 * r
        elif r < r2:
            val = m2 * (r - r1) + s1
        else:
            val = m3 * (r - r2) + s2
        lut.append(rapikan(val))
    return lut

def lut_threshold(T=128, L=256):
    return [255 if r >= T else 0 for r in range(L)]

def ekualisasi_histogram(citra, L=256):
    total_piksel = citra.size  # M * N

    hist = [0] * L
    for r in citra.ravel():
        hist[r] += 1

    cdf = [0.0] * L
    kumulatif = 0.0
    for r in range(L):
        p_r = hist[r] / total_piksel
        kumulatif += p_r
        cdf[r] = kumulatif

    lut = [rapikan((L - 1) * cdf[r]) for r in range(L)]

    return terapkan_lut(citra, lut)

if __name__ == "__main__":
    nama_file = "ITS-berhasil-meraih-posisi-pertama-pada-bidang-Marine-Engineering-Product-and-Industrial-Design-Operation-Research-dan-Supply-Chain-Management-versi-EduRank.jpg"
    img_warna = cv2.imread(nama_file, cv2.IMREAD_COLOR)
    if img_warna is not None:
        img_warna = cv2.cvtColor(img_warna, cv2.COLOR_BGR2RGB)
    
    img = cv2.imread(nama_file, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Gambar tidak ditemukan! Pastikan nama file atau path sudah sesuai.")
    else:
        hasil_negatif = terapkan_lut(img, lut_negatif())
        hasil_log     = terapkan_lut(img, lut_log())
        hasil_gamma   = terapkan_lut(img, lut_gamma(gamma=0.5))
        hasil_stretch = terapkan_lut(img, lut_contrast_stretching())
        hasil_ekual   = ekualisasi_histogram(img, L=256)

        plt.figure(figsize=(14, 8))

        plt.subplot(2, 3, 1)
        plt.imshow(img_warna)
        plt.title("Citra Asli")
        plt.axis("off")

        daftar_tampilan = [
            ("Negatif", hasil_negatif),
            ("Logaritmik", hasil_log),
            ("Gamma (0.5)", hasil_gamma),
            ("Contrast Stretching", hasil_stretch),
            ("Ekualisasi Histogram", hasil_ekual)
        ]

        for i, (judul, gambar) in enumerate(daftar_tampilan, start=2):
            plt.subplot(2, 3, i)
            plt.imshow(gambar, cmap="gray")
            plt.title(judul)
            plt.axis("off")

        plt.tight_layout()
        plt.show()