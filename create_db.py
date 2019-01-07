import numpy as np
import cv2
import scipy.io
import argparse
from tqdm import tqdm
from utils import get_meta


def get_args():
    parser = argparse.ArgumentParser(description="This script cleans-up noisy labels "
                                                 "and creates database for training.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--output", "-o", type=str, required=True,
                        help="path to output database mat file")
    parser.add_argument("--db", type=str, default="wiki",
                        help="dataset; wiki or imdb")
    parser.add_argument("--img_size", type=int, default=32,
                        help="output image size")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    output_path = args.output
    db = args.db
    img_size = args.img_size

    root_path = "data/{}_crop/".format(db)
    mat_path = root_path + "{}.mat".format(db)
    full_path, dob, age = get_meta(mat_path, db)

    out_ages = []
    out_imgs = []

    for i in tqdm(range(len(age))):
        if ~(0 <= age[i] <= 100):
            continue

        out_ages.append(age[i])
        img = cv2.imread(root_path + str(full_path[i][0]))
        out_imgs.append(cv2.resize(img, (img_size, img_size)))

    output = {"image": np.array(out_imgs), "age": np.array(out_ages),
              "db": db, "img_size": img_size}
    scipy.io.savemat(output_path, output)


if __name__ == '__main__':
    main()