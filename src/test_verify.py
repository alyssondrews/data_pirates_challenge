import unittest
import constants
from get_cep import get_data, build_info, create_and_write_document
class VerifyTests(unittest.TestCase):
    def test_number_of_UF(self):
        list_uf = constants.UF_LIST
        list_uf = len(list_uf)
        total_uf = 27
        self.assertEquals(list_uf, total_uf)
    ##test if data is returning
    def test_get_data(self):
        pass
    def test_build_info(self):
        pass
    def test_create_doc(self):
        pass