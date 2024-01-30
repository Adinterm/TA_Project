import math
import cmath

def fft_image(image):
    # Convert the image to grayscale if it has multiple channels
    if len(image[0][0]) > 1:
        image = rgb_to_gray(image)
    
    # Get the dimensions of the image
    height, width = len(image), len(image[0])
    
    # Apply 2D FFT to the image
    fft_result = [[complex(0, 0) for _ in range(width)] for _ in range(height)]
    for y in range(height):
        fft_result[y] = fft(image[y])
    
    fft_result = transpose(fft_result)
    
    for x in range(width):
        fft_result[x] = fft(fft_result[x])
    
    fft_result = transpose(fft_result)
    
    # Shift the zero-frequency component to the center of the spectrum
    fft_shifted = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            fft_shifted[y][x] = fft_result[y - height // 2][x - width // 2]
    
    # Compute the magnitude spectrum
    magnitude_spectrum = [[abs(pixel) for pixel in row] for row in fft_shifted]
    
    return magnitude_spectrum

def fft(x):
    N = len(x)
    
    # Base case: if the input size is 1, return the input
    if N == 1:
        return x
    
    even = fft(x[0::2])  # Recursive call for even-indexed elements
    odd = fft(x[1::2])   # Recursive call for odd-indexed elements
    
    # Combine the results of the recursive calls
    result = [0] * N
    for k in range(N//2):
        t = cmath.exp(-2j*math.pi*k/N) * odd[k]
        result[k] = even[k] + t
        result[k + N//2] = even[k] - t
    
    return result

def rgb_to_gray(image):
    height, width = len(image), len(image[0])
    gray_image = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            r, g, b = image[y][x]
            gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
            gray_image[y][x] = gray
    
    return gray_image

def transpose(matrix):
    return list(map(list, zip(*matrix)))

# Example usage
image = [
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[128, 128, 128], [0, 0, 0], [255, 255, 255]]
]
magnitude_spectrum = fft_image(image)
print(magnitude_spectrum)
import matplotlib.pyplot as plt
plt.imshow(magnitude_spectrum, cmap='Greys')
plt.show()