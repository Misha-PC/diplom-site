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


def get_action(status):
    def status0(user_id, message, *args, **kwargs):
        print("status - ", status)
        print("args: ", [user_id, message, *args])

    def status1(user_id, message,*args, **kwargs):
        print("status - ", status)
        print("args: ", [user_id, message, *args])

    def status2(user_id, message,*args, **kwargs):
        print("status - ", status)
        print("args: ", [user_id, message, *args])

    def status3(user_id, message,*args, **kwargs):
        print("status - ", status)
        print("args: ", [user_id, message, *args])

    def status4(user_id, message,*args, **kwargs):
        print("status - ", status)
        print("args: ", [user_id, message, *args])

    def status5(user_id, message,*args, **kwargs):
        print("status - ", status)
        print("args: ", [user_id, message, *args])

    actions = {
        '0': status0,
        '1': status1,
        '2': status2,
        '3': status3,
        '4': status4,
        '5': status5,
    }

    status = str(status)

    if not status in actions.keys():
        print(f'Exception : {status} out of range')
        return None

    return actions[str(status)]


if __name__ == "__main__":
    for i in range(-2, 7):
        action = get_action(i)
        if action:
            action('1', 'text')
