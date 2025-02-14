import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest  # Importing unittest framework
import ft8_generator.crc as crc
import ft8_generator.ldpc as ldpc

__name__ = "__main__"

class TestLDPCGenerator(unittest.TestCase):
    def test_ldpc_generator(self):
        payload = np.array([0x1C, 0x3F, 0x8A, 0x6A, 0xE2, 0x07, 0xA1, 0xE3, 0x94, 0x51], dtype=np.uint8)
        a91_12bytes = crc.crc_generator(payload)
        codeword = ldpc.ldpc_generator(a91_12bytes)
        np.set_printoptions(formatter={'int': lambda x: format(x, '02X')})
        print(codeword)

if __name__ == '__main__':
    unittest.main()

