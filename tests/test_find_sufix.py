# pragma: no cover
import unittest


class TestClass(unittest.TestCase):
    def test_find_rigth_path(self):
        retorno = find_by_sufix('/home/romulo/dev/gitlab/cocus_assignment', '.py')
        self.assertNotEqual(retorno,None)

    def test_find_rigth_wrong_path(self):
        retorno = find_by_sufix('/home/romulo/dev/gitlab/cocus_assignment', '.csv')
        self.assertEqual(retorno,None)


def find_by_sufix(path, suffix):
    import os
    path_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                path_list.append(os.path.join(root, file))
    if len(path_list) > 0:
        return path_list
    else:
        return None