from hashlib import sha1
import os


def get_sha1_from_file(f_name):
    try:
        with open(f_name) as file:
            f_context = file.read()
    except:
        return None

    hash_code = sha1(f_context).hexdigest()
    return hash_code
