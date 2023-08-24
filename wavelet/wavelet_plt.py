
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pywt

import os


def denoise_signal(filename):

    y = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            else: #
                y_value = line.split(",")[0]
                y.append(float(y_value))




    wavelet = "sym8"
    level = 3


    coeffs = pywt.wavedec(y, wavelet, level=level, mode="periodization")


    thresholded_coeffs = []
    for i in range(1, len(coeffs)):

        detail = coeffs[i]
        sigma = np.median(np.abs(detail)) / 0.6745
        threshold = sigma * np.sqrt(2 * np.log(len(detail)))
        thresholded_detail = pywt.threshold(detail, threshold, mode="soft")
        thresholded_coeffs.append(thresholded_detail)

    thresholded_coeffs.insert(0, coeffs[0])


    denoised_y = pywt.waverec(thresholded_coeffs, wavelet, mode="periodization")


    return denoised_y


filenames = []
for file in os.listdir("fake"):
    if file.endswith(".csv"):
        filenames.append(file)


rows = (len(filenames) - 1) // 4 + 1
cols = 4
fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))


for i, filename in enumerate(filenames):

    row = i // cols
    col = i % cols

    plt.sca(axes[row, col])

    denoised_y = denoise_signal(os.path.join("fake", filename))

    plt.plot(denoised_y)
    plt.title(filename)


plt.tight_layout()

plt.show()

data = denoise_signal("synthetic_data_0_new.csv")
plt.plot(data)
plt.show()
