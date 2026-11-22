"""琢琥（ZHUOHU）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from zhuohu import Zhuohu


class TestZhuohu(unittest.TestCase):
    def setUp(self):
        self.op = Zhuohu()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "zhuohu")
        self.assertEqual(d["code"], "ZHUOHU")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_distill_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.distill(None)

    def test_profile_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.profile()


if __name__ == "__main__":
    unittest.main()
