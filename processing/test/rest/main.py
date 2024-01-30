import numpy as np
import sys
import os 
from etc import img, graph
os.chdir('/Users/User_Linux/OneDrive/Documents/Programs Code/Python/FT_Analysis')
sys.path.append(os.path.dirname(os.getcwd())+'/FT_Analysis/etc')
sys.path.append(os.path.dirname(os.getcwd())+'/FT_Analysis/images')
import matplotlib.pyplot as plt


import cv2
import numpy as np

# Read the HSV image
hsv_image = cv2.imread('IMG_9922.JPG', cv2.IMREAD_COLOR)
hsv_image = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)

# Select a specific hue value (e.g., 120 for green) or saturation value (e.g., 255 for fully saturated pixels)
hue_value = 120
saturation_value = 255

# Set the other components (saturation and value) to a fixed value or keep them as is
# 1. Keep saturation and value as is, discard hue
gray_like_image_hue = np.zeros_like(hsv_image)
gray_like_image_hue[:, :, 1:] = hsv_image[:, :, 1:]

# 2. Keep hue and value as is, set saturation to a fixed value
gray_like_image_saturation = np.copy(hsv_image)
gray_like_image_saturation[:, :, 1] = saturation_value

# Convert the gray-like images back to BGR (if needed)
gray_like_image_hue_bgr = cv2.cvtColor(gray_like_image_hue, cv2.COLOR_HSV2BGR)
gray_like_image_saturation_bgr = cv2.cvtColor(gray_like_image_saturation, cv2.COLOR_HSV2BGR)
#plt.imshow(gray_like_image_hue_bgr)
plt.imshow(gray_like_image_saturation)
plt.show()
# Display the results
cv2.imshow('Gray-like Image (Hue)', gray_like_image_hue_bgr)
cv2.imshow('Gray-like Image (Saturation)', gray_like_image_saturation_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()


sys.exit()
# Load the first and second images
image1 = np.array(cv2.imread('IMG_9829.JPG', cv2.IMREAD_COLOR))
image2 = np.array(cv2.imread('IMG_9838.JPG', cv2.IMREAD_COLOR))

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Image Preprocessing
image = cv2.imread('IMG_9829.JPG', 0)  # Read the image in grayscale
image = cv2.resize(image, (256, 256))  # Resize the image to a power of two if needed

# Step 2: Apply the FFT
fft = np.fft.fft2(image)
fft_shift = np.fft.fftshift(fft)

# Step 3: Analyze the Spectrum
magnitude_spectrum = np.abs(fft_shift)
log_magnitude_spectrum = np.log1p(magnitude_spectrum)  # Apply logarithm for better visualization

# Step 4: Detect Object Edges
# Create a high-pass filter mask
rows, cols = image.shape
center_row, center_col = rows // 2, cols // 2
mask = np.ones((rows, cols), np.uint8)
mask[center_row-30:center_row+30, center_col-30:center_col+30] = 0  # Customize filter size

filtered_spectrum = fft_shift * mask
filtered_image = np.fft.ifft2(np.fft.ifftshift(filtered_spectrum)).real

# Step 5: Statistical Analysis
gradient_x = cv2.Sobel(filtered_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(filtered_image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Thresholding to obtain binary image
threshold = 50  # Adjust the threshold value as needed
edges_binary = np.uint8(gradient_magnitude > threshold) * 255

# Display the results
plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.axis('off')

plt.subplot(2, 2, 2), plt.imshow(log_magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.axis('off')

plt.subplot(2, 2, 3), plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image'), plt.axis('off')

plt.subplot(2, 2, 4), plt.imshow(edges_binary, cmap='gray')
plt.title('Detected Edges'), plt.axis('off')

plt.tight_layout()
plt.show()


sys.exit()

# Find the differing pixel coordinates
coordinates = np.argwhere(np.any(image1 != image2, axis=2))

# Create a copy of the second image with the differing pixel set to black
modified_image2 = np.copy(image2)
for y, x in coordinates:
    modified_image2[y, x] = [0, 0, 0]  # Set the differing pixel to black (0, 0, 0)

# Create a mask for the differing pixels in the first image
mask = np.zeros_like(image1)
mask[coordinates[:, 0], coordinates[:, 1]] = [1, 0, 0]  # Set the differing pixel to red (1, 0, 0)

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot the first image with the differing pixel highlighted in red
axs[0].imshow(image1)
axs[0].imshow(mask, alpha=0.5)
axs[0].set_title('Image 1')

# Plot the modified second image with the differing pixel set to black
axs[1].imshow(modified_image2)
axs[1].set_title('Modified Image 2')

# Adjust spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()

sys.exit()

# Display the highlighted image
cv2.imshow("Highlighted Image", highlighted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


sys.exit()

# Convert images to float32 for calculations
first_img_float = first_img.astype(np.float32)
second_img_float = second_img.astype(np.float32)

# Normalize the second image using the first image
normalized_second_img = second_img_float / first_img_float

# Clip the pixel values to the valid range [0, 255]
normalized_second_img = np.clip(normalized_second_img, 0, 255).astype(np.uint8)

# Display the original and normalized images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(second_img, cv2.COLOR_BGR2RGB))
plt.title('Second Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(normalized_second_img, cv2.COLOR_BGR2RGB))
plt.title('Normalized Second Image')

plt.tight_layout()
plt.show()

sys.exit()

# Load the before and after dawn HSV images
before_dawn_img = cv2.imread('IMG_9829.JPG', cv2.IMREAD_COLOR)
after_dawn_img = cv2.imread('IMG_9922.JPG', cv2.IMREAD_COLOR)

# Convert images to HSV color space
before_dawn_hsv = cv2.cvtColor(before_dawn_img, cv2.COLOR_BGR2HSV)
after_dawn_hsv = cv2.cvtColor(after_dawn_img, cv2.COLOR_BGR2HSV)

# Extract the Value (V) channel
before_dawn_value = before_dawn_hsv[:,:,2]
after_dawn_value = after_dawn_hsv[:,:,2]

# Apply thresholding to detect the first sunlight emergence
threshold = 150
before_dawn_thresholded = cv2.threshold(before_dawn_value, threshold, 255, cv2.THRESH_BINARY)[1]
after_dawn_thresholded = cv2.threshold(after_dawn_value, threshold, 255, cv2.THRESH_BINARY)[1]

# Calculate the statistics for the before dawn thresholded image
before_dawn_stats = cv2.connectedComponentsWithStats(before_dawn_thresholded)

# Retrieve the area and intensity values for each detected region
before_dawn_areas = before_dawn_stats[2][:, cv2.CC_STAT_AREA]
before_dawn_intensities = before_dawn_value[before_dawn_thresholded > 0]

# Perform statistical analysis (e.g., mean, median, standard deviation, etc.) on the area and intensity values
mean_area = np.mean(before_dawn_areas)
median_intensity = np.median(before_dawn_intensities)
std_intensity = np.std(before_dawn_intensities)

# Display the statistical results
print(f"Mean area: {mean_area}")
print(f"Median intensity: {median_intensity}")
print(f"Standard deviation of intensity: {std_intensity}")

# Visualize the thresholded images
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(before_dawn_img, cv2.COLOR_BGR2RGB))
plt.title('Before Dawn')

plt.subplot(2, 2, 2)
plt.imshow(before_dawn_thresholded, cmap='gray')
plt.title('Before Dawn Thresholded')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(after_dawn_img, cv2.COLOR_BGR2RGB))
plt.title('After Dawn')

plt.subplot(2, 2, 4)
plt.imshow(after_dawn_thresholded, cmap='gray')
plt.title('After Dawn Thresholded')

plt.tight_layout()
plt.show()



sys.exit()
#image = img.get_rgb('IMG_9829.JPG')
image = img.get_rgb('IMG_9922.JPG')
img_data = image.get_r()
c = graph.get_graph(img_data)

#get_hist (hist, bins)
#get_freq (freq_cols_pos, mag_spect)
#d, e = c.get_hist()
c.get_freq()


sys.exit()




def save_data(self):
        data = np.column_stack((freq_cols_pos, magnitude_spectrum_pos.mean(axis=0)))
        np.savetxt('fft_data.csv', data, delimiter=',', header='Frequency,Magnitude', comments='')


anly = analyze("test.png",1)
anly.freq_mag2()


def save_data(self):
        data = np.column_stack((freq_cols_pos, magnitude_spectrum_pos.mean(axis=0)))
        np.savetxt('fft_data.csv', data, delimiter=',', header='Frequency,Magnitude', comments='')


anly = analyze("test.png",1)
anly.freq_mag2()

sys.exit()

if __name__ == "__main__":

    #   img.py
    c = img.get_rgb('rgb.png')
    c = c.get_b()
    import matplotlib.pyplot as plt
    print(c)
    plt.imshow(c)
    plt.show()

    sys.exit()

