import unittest
import constants
from get_cep import get_data
class VerifyTests(unittest.TestCase):
    def test_number_of_UF(self):
        list_uf = constants.UF_LIST
        list_uf = len(list_uf)
        total_uf = 27
        self.assertEquals(list_uf, total_uf)