"""琢琥（ZHUOHU）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_distill_profile(self):
        out = self.op.distill({"name": "算子甲", "params": 1000})
        self.assertEqual(out["params"], 500)
        self.assertEqual(self.op.profile()["runs"], 1)
        with self.assertRaises(ValueError):
            self.op.distill("非模型")


if __name__ == "__main__":
    unittest.main()
