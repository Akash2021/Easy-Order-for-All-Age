from scipy.io import loadmat
from datetime import datetime
import os


def calc_age(taken, dob):
    birth = datetime.fromordinal(max(int(dob) - 366, 1))
    # assume the photo was taken in the middle of the year
    if birth.month < 7:
        return taken - birth.year
    else:
        return taken - birth.year - 1


def get_meta(mat_path, db):
    meta = loadmat(mat_path)
    full_path = meta[db][0, 0]["full_path"][0]
    dob = meta[db][0, 0]["dob"][0]  # Matlab serial date number
    photo_taken = meta[db][0, 0]["photo_taken"][0]  # year
    age = [calc_age(photo_taken[i], dob[i]) for i in range(len(dob))]

    return full_path, dob, age


def load_data(mat_path):
    d = loadmat(mat_path)
    return d["image"], d["age"][0], d["db"][0], d["img_size"][0, 0]


def mk_dir(dir):
    try:
        os.mkdir( dir )
    except OSError:
        pass