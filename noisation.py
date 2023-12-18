import cv2
import numpy as np
import os

# Create a directory to store noisy images
noisy_folder_Normal = 'DS_NoisyImages/Normal'
noisy_folder_Med = 'DS_NoisyImages/Med'
noisy_folder_RS = 'DS_NoisyImages/RS'
os.makedirs(noisy_folder_Normal, exist_ok=True)
os.makedirs(noisy_folder_Med, exist_ok=True)
os.makedirs(noisy_folder_RS, exist_ok=True)


def add_salt_and_pepper_noise(image, density):
    row, col, z = image.shape
    number_of_pixels = int(density * image.size)
    noisy_image = np.copy(image)

    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = np.random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = np.random.randint(0, col - 1)

        # Color that pixel to white
        noisy_image[y_coord][x_coord] = 255

        # Randomly pick some pixels in
        # the image for coloring them black
        # Pick a random number between 300 and 10000
    number_of_pixels = np.random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = np.random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = np.random.randint(0, col - 1)

        # Color that pixel to black
        noisy_image[y_coord][x_coord] = 0

    return noisy_image


# Function to add Speckle noise to an image
def add_speckle_noise(image, variance):
    row, col, _ = image.shape
    gauss = np.random.randn(row, col, 3)
    noisy = image + image * gauss * variance
    return noisy


# Function to add Poisson noise to an image
def add_poisson_noise(image, scale):
    noisy = np.random.poisson(image * scale) / scale
    return noisy


# Function to add Gaussian noise to an image
def add_gaussian_noise(image, mean=0, sigma=25):
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy = image + gauss
    return noisy


# Function to apply filters to noisy images and save them
def apply_filters_and_save(original_name, noisy_images, folder_name, noise_type, density, filter_sizes):
    for size in filter_sizes:
        for i, noisy_image in enumerate(noisy_images):
            output_name = f"{original_name.split('.')[0]}_{noise_type}_density_{density[i]}_filter_size_{size}_image_{i + 1}.jpg"
            output_path = os.path.join(folder_name, output_name)
            print("folder " + folder_name + " path " + output_path)

            cv2.imwrite(output_path, noisy_image)


# Iterate through images in 'DS/Normal' folder
input_folder = 'DS/Normal'
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        image_path = os.path.join(input_folder, filename)
        original_image = cv2.imread(image_path)

        # Salt and Pepper noise
        salt_and_pepper_densities = [0.05, 0.1, 0.2, 0.4]
        salt_and_pepper_noisy_images = [add_salt_and_pepper_noise(original_image, density) for density in
                                        salt_and_pepper_densities]
        apply_filters_and_save(filename, salt_and_pepper_noisy_images, noisy_folder_Normal, 'salt_and_pepper',
                               salt_and_pepper_densities, [7])

        # Speckle noise
        speckle_variances = [0.0001, 0.0005, 0.001, 0.002]
        speckle_noisy_images = [add_speckle_noise(original_image, variance) for variance in speckle_variances]
        apply_filters_and_save(filename, speckle_noisy_images, noisy_folder_Normal, 'speckle', speckle_variances, [7])

        # Poisson noise
        poisson_scales = [0.1, 0.5, 1.0, 2.0]
        poisson_noisy_images = [add_poisson_noise(original_image, scale) for scale in poisson_scales]
        apply_filters_and_save(filename, poisson_noisy_images, noisy_folder_Normal, 'poisson', poisson_scales, [7])

        # Gaussian noise
        gaussian_densities = [1, 5, 10]
        gaussian_noisy_images = [add_gaussian_noise(original_image, sigma=density) for density in gaussian_densities]
        apply_filters_and_save(filename, gaussian_noisy_images, noisy_folder_Normal, 'gaussian', gaussian_densities,
                               [7])

print("Noisy images on Normal saved successfully.")

# Iterate through images in 'DS/Med' folder
input_folder = 'DS/Med'
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        image_path = os.path.join(input_folder, filename)
        original_image = cv2.imread(image_path)

        # Salt and Pepper noise
        salt_and_pepper_densities = [0.05, 0.1, 0.2, 0.4]
        salt_and_pepper_noisy_images = [add_salt_and_pepper_noise(original_image, density) for density in
                                        salt_and_pepper_densities]
        apply_filters_and_save(filename, salt_and_pepper_noisy_images, noisy_folder_Med + "Med", 'salt_and_pepper',
                               salt_and_pepper_densities, [7])

        # Speckle noise
        speckle_variances = [0.0001, 0.0005, 0.001, 0.002]
        speckle_noisy_images = [add_speckle_noise(original_image, variance) for variance in speckle_variances]
        apply_filters_and_save(filename, speckle_noisy_images, noisy_folder_Med, 'speckle', speckle_variances,
                               [7])

        # Poisson noise
        poisson_scales = [0.1, 0.5, 1.0, 2.0]
        poisson_noisy_images = [add_poisson_noise(original_image, scale) for scale in poisson_scales]
        apply_filters_and_save(filename, poisson_noisy_images, noisy_folder_Med, 'poisson', poisson_scales, [7])

        # Gaussian noise
        gaussian_densities = [1, 5, 10]
        gaussian_noisy_images = [add_gaussian_noise(original_image, sigma=density) for density in gaussian_densities]
        apply_filters_and_save(filename, gaussian_noisy_images, noisy_folder_Med, 'gaussian',
                               gaussian_densities, [7])

print("Noisy images on Med saved successfully.")

# Iterate through images in 'DS/RS' folder
input_folder = 'DS/RS'
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        image_path = os.path.join(input_folder, filename)
        original_image = cv2.imread(image_path)

        # Salt and Pepper noise
        salt_and_pepper_densities = [0.05, 0.1, 0.2, 0.4]
        salt_and_pepper_noisy_images = [add_salt_and_pepper_noise(original_image, density) for density in
                                        salt_and_pepper_densities]
        apply_filters_and_save(filename, salt_and_pepper_noisy_images, noisy_folder_RS, 'salt_and_pepper',
                               salt_and_pepper_densities, [7])

        # Speckle noise
        speckle_variances = [0.0001, 0.0005, 0.001, 0.002]
        speckle_noisy_images = [add_speckle_noise(original_image, variance) for variance in speckle_variances]
        apply_filters_and_save(filename, speckle_noisy_images, noisy_folder_RS, 'speckle', speckle_variances,
                               [7])

        # Poisson noise
        poisson_scales = [0.1, 0.5, 1.0, 2.0]
        poisson_noisy_images = [add_poisson_noise(original_image, scale) for scale in poisson_scales]
        apply_filters_and_save(filename, poisson_noisy_images, noisy_folder_RS, 'poisson', poisson_scales, [7])

        # Gaussian noise
        gaussian_densities = [1, 5, 10]
        gaussian_noisy_images = [add_gaussian_noise(original_image, sigma=density) for density in gaussian_densities]
        apply_filters_and_save(filename, gaussian_noisy_images, noisy_folder_RS, 'gaussian', gaussian_densities,
                               [7])

print("Noisy images on Rs saved successfully.")
