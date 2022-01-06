
def find_by_sufix(suffix, path):
    import os
    """
    Find all files within a path, with a given file name suffix. Note that a path may contain further
    subdirectories and those subdirectories may also contain further subdirectories. There is no limit
    to the depth of the subdirectories.
    Arguments:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system
    Returns:
        a list of paths and file names that match the suffix
    """
    path_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.endswith(suffix)):
                # print(os.path.join(root, file))
                path_list.append(os.path.join(root, file))
    return path_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "/home/romulo/dev/gitlab/cocus_assignment"
    suffix = ".py"
    # print(find_by_sufix(suffix, path))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
