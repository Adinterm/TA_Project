import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and plot the data
plt.figure(figsize=(10, 6))  # Set the figure size (adjust as needed)
plt.plot(x, y, label='Example Data')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Example Plot')
plt.legend()

# Save the plot as a high-resolution image (e.g., PNG)
output_file = 'output_plot.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')  # Set the DPI (dots per inch) for high resolution

# Show the plot (optional)
plt.show()



import fft_conv, graph, img, img_fft, plot, save_data


import numpy as np
from scipy.fftpack import fft, ifft
import cv2

# Load an image
image = cv2.imread('image.jpg')

# Convert to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Extract hue, saturation, and value values as separate arrays
hue_values = hsv_image[:, :, 0].flatten()
saturation_values = hsv_image[:, :, 1].flatten()
value_values = hsv_image[:, :, 2].flatten()

# Apply FFT and filter low-frequency components
def low_pass_filter(time_series, cutoff_frequency):
    fft_coefficients = np.fft.fft(time_series)
    mask = np.abs(np.fft.fftfreq(time_series.shape[0])) < cutoff_frequency
    filtered_coefficients = fft_coefficients * mask
    filtered_time_series = np.fft.ifft(filtered_coefficients)
    return np.real(filtered_time_series)

smoothed_hue_values = low_pass_filter(hue_values, cutoff_frequency=0.01)
smoothed_saturation_values = low_pass_filter(saturation_values, cutoff_frequency=0.01)
smoothed_value_values = low_pass_filter(value_values, cutoff_frequency=0.01)

# Implement thresholding and detection logic based on the smoothed time series
# ...

# Visualize smoothed time series
import matplotlib.pyplot as plt

plt.plot(hue_values, label='Original Hue')
plt.plot(smoothed_hue_values, label='Smoothed Hue')
plt.legend()
plt.show()

plt.plot(saturation_values, label='Original Saturation')
plt.plot(smoothed_saturation_values, label='Smoothed Saturation')
plt.legend()
plt.show() 

plt.plot(value_values, label='Original Value')
plt.plot(smoothed_value_values, label='Smoothed Value')
plt.legend()
plt.show()
