class TestClass(object):  # pragma: no cover
    def test_find_rigth_path(self):
        retorno = find_by_sufix('/home/romulo/dev/gitlab/cocus_assignment', '.py')
        assert retorno is not None

    def test_find_rigth_wrong_path(self):
        retorno = find_by_sufix('/home/romulo/dev/gitlab/cocus_assignment', '.csv')
        assert retorno is None


def find_by_sufix(path, suffix):
    import os
    path_list = []   # pragma: no cover
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.endswith(suffix)):
                path_list.append(os.path.join(root, file))
    if len(path_list) > 0:  # pragma: no cover
        return path_list
    else:
        return None  # pragma: no cover
