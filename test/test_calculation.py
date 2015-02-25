import os
import unittest
from statistics import mean


class TestCalculation(unittest.TestCase):

    def test_aggregation(self):
        speech1 = [{"p":"A", "s":12}, {"p":"X", "s":10}, {"p":"G", "s":1}]
        speech2 = [{"p":"B", "s":10}, {"p":"Y", "s":8}, {"p":"H", "s":2}]
        speech3 = [{"p":"C", "s":9}, {"p":"Z", "s":7}, {"p":"I", "s":3}]

        speeches = [speech1, speech2, speech3]

        aggregated = []
        for s in speeches:
            phrase = ",".join([p["p"] for p in s])
            speed = mean([p["s"] for p in s])
            aggregated.append([phrase, speed])

        # write to file
        path = os.path.join(os.path.dirname(__file__), "./test_aggregation.txt")

        with open(path, "wb") as outfile:
            for a in aggregated:
                print(a)
                line = "\t".join([str(v) for v in a]) + "\n"
                outfile.write(line.encode("utf-8"))
