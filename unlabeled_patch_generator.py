import os
import glob
import numpy as np
import cv2
import random
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Unlabeled Patch Generator')
    parser.add_argument('--dataset', type=str, required=True, help="Path to dataset folder.")
    parser.add_argument('--save_dir', type=str, required=True, help='Path to save folder.')
    parser.add_argument('--patch_width', type=int, default=64, help='Width of a patch image.')
    parser.add_argument('--patch_height', type=int, default=64, help='Height of a aptch image.')
    parser.add_argument('--num', type=int, required=True, help="The number of patch images.")
    opt = parser.parse_args()

    # Make an input images index and check it.
    input_paths = sorted(glob.glob(f"{opt.dataset}/*.*"))
    #print(input_paths)
    assert len(input_paths) > 0, "Cannot find input images!!"

    os.makedirs(opt.save_dir, exist_ok=False)
    os.makedirs(opt.save_dir+"/patches", exist_ok=False)
    os.makedirs(opt.save_dir+"/marked", exist_ok=False)

    # Loop for all images
    for i, path in enumerate(input_paths):
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img_marked = img.copy()

        height, width = img.shape[0], img.shape[1]
        half_p_width = opt.patch_width // 2
        half_p_height = opt.patch_height // 2
        corr_p_width = opt.patch_width % 2
        corr_p_height = opt.patch_height % 2

        # Create patch images
        for j in range(0, opt.num):
            # Select a pixel randomly
            px = random.randint(half_p_width + 1, width - half_p_width - corr_p_width)
            py = random.randint(half_p_height + 1, height - half_p_height - corr_p_height)
            # Extract a patch image
            p_img = img[
                            py-half_p_height : py+half_p_height+corr_p_height,
                            px-half_p_width : px+half_p_width+corr_p_width
                        ]
            # Put a rectangle marker on extracted area
            img_marked = cv2.rectangle(img_marked, (px-half_p_width, py-half_p_height), (px+half_p_width, py+half_p_height), (0, 0, 255), 1)
            # Save an image
            file_name, file_extension = os.path.splitext(os.path.basename(path))
            save_path = opt.save_dir + "/patches/" + file_name + "-" + str(j).zfill(5) + file_extension
            cv2.imwrite(save_path, p_img)
        # Save a marked image
        cv2.imwrite(opt.save_dir + "/marked/" + file_name + "-marked" + file_extension, img_marked)
    print('Done.')