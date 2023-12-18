import os
import cv2
import numpy as np


def apply_filters(image, filter_type, density=None, sigma=None):
    if filter_type == 'bilateral':
        # Bilateral filter with density parameter
        denoised = cv2.bilateralFilter(image, 9, density, density)
    elif filter_type == 'laplacian':
        # Laplacian filter with density parameter
        denoised = cv2.Laplacian(image, cv2.CV_64F, ksize=5)
        denoised = np.uint8(np.absolute(denoised))
    elif filter_type == 'gaussian':
        # Gaussian filter with sigma parameter
        denoised = cv2.GaussianBlur(image, (5, 5), sigma)
    # elif filter_type == 'shearlet':
    #     # Shearlet filter
    #     denoised = shearlet.denoise(image, 0.5)
    else:
        raise ValueError(f"Invalid filter type: {filter_type}")

    return denoised


def main():
    input_folders = ['DS_NoisyImages/Normal', 'DS_NoisyImages/Med', 'DS_NoisyImages/RS']
    output_folders = ['DS_DeNoisyImages/Normarl', 'DS_DeNoisyImages/Med', 'DS_DeNoisyImages/RS']
    filter_params = {'bilateral': [50, 75, 100], 'laplacian': [1, 2, 3], 'gaussian': [1, 2, 3],
                     # 'shearlet': None
                     }

    for i, input_folder in enumerate(input_folders):
        output_folder = output_folders[i]

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                image_path = os.path.join(input_folder, filename)
                image = cv2.imread(image_path, cv2.IMREAD_COLOR)
                print(image_path)
                for filter_type, filter_params_list in filter_params.items():
                    if filter_params_list is not None:
                        for param in filter_params_list:
                            denoised = apply_filters(image, filter_type, param)
                            output_filename = f"{os.path.splitext(filename)[0]}_{filter_type}_{param}.png"
                            output_path = os.path.join(output_folder, output_filename)
                            cv2.imwrite(output_path, denoised)
                    else:
                        denoised = apply_filters(image, filter_type)
                        output_filename = f"{os.path.splitext(filename)[0]}_{filter_type}.png"
                        output_path = os.path.join(output_folder, output_filename)
                        cv2.imwrite(output_path, denoised)


if __name__ == "__main__":
    main()
