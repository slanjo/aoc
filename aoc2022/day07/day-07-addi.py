Here is my code that works somehow :), I'll need to clean it up for better reading


#!/bin/python3

fs = dict()
dir_pointer = list()

def get_dir(dir_pointer: list):
    dir = fs
    while len(dir_pointer) > 0:
        dir_base = dir_pointer.pop(0)
        if dir_base not in dir.keys():
            dir[dir_base] = {"name": dir_base, "size": 0}
        dir = dir[dir_base]

    return dir

def update_parent_dir(dir_ptr, file_size):
    # Size for current location has been set already.
    dir_ptr.pop()
    fs_ptr = fs
    while len(dir_ptr) > 0:
        dir_base = dir_ptr.pop(0)
        if dir_base in fs_ptr.keys():
            fs_ptr[dir_base]["size"] += file_size
        fs_ptr = fs_ptr[dir_base]

def get_total_size(dir: dict) -> int:
    total_size = 0

    if "size" in dir.keys() and dir["size"] <= 100000:
        total_size += dir["size"]

    for item in dir.values():
        if type(item) == dict:
            total_size += get_total_size(item)

    return total_size



def get_smallest_dir_size_req(dir: dict, min_size_req: int, max_size_req) -> int:
    return_value = max_size_req

    for item in dir.values():
        print(item)
        if type(item) == dict and "size" in item.keys() and item["size"] >= min_size_req and item["size"] <= max_size_req:
            return_value = item["size"]

            for sub_item in item.values():
                print(sub_item)
                if type(sub_item) == dict:

                    return_value = get_smallest_dir_size_req(item, min_size_req, return_value)

    return return_value


# Create the read-only file handler in_file for input.txt.
with open("input.txt", "r") as in_file:
    cnt = 0
    fs_dir = {}
    for line in in_file.read().splitlines():
        line_set = line.split()
        if line_set[0] == "$":
            if line_set[1] == "cd" and line_set[2] == "..":
                dir_pointer.pop()
                fs_dir = get_dir(dir_pointer.copy())
            elif line_set[1] == "cd":
                dir_pointer.append(line_set[2])
                fs_dir = get_dir(dir_pointer.copy())
            elif line_set[1] == "ls":
                pass

        elif line_set[0] == "dir":
            pass
        else:
            fs_dir["size"] += int(line_set[0])
            update_parent_dir(dir_pointer.copy(), int(line_set[0]))
            pass

    # print(f"Total size: {get_total_size(fs)}")

    FS_SIZE = 70000000
    USED_SPACE = fs["/"]["size"]
    UNUSED_SPACE = FS_SIZE - USED_SPACE
    UPDATE_REQ = 30000000
    SIZE_REQ = UPDATE_REQ - UNUSED_SPACE

    print("SPACE UNUSED: ", UNUSED_SPACE)
    print("SPACE USED: ", USED_SPACE)
    print("SPACE REQ: ", SIZE_REQ)

    print(f"Smallest directory: {get_smallest_dir_size_req(fs, SIZE_REQ, USED_SPACE)}")
