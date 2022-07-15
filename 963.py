"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
# research
# notes: implement a data structure that records integer ids
# rules: must use record(order_id) and get_last(i)

import unittest

# n doesn't matter since python has built in list/queue data structure, if in c++ then n can be used to define size of char buffer or vector
class OrderLogData:
    def __init__(self) -> None:
        self._log = []
    
    def record(self, order_id: int) -> None:
        self._log.append(order_id)

    def get_last(self, i: int) -> int:
        return self._log[-i]

class Test(unittest.TestCase):
    def test_case(self):
        log = OrderLogData()
        for i in range(100):
            log.record(i)
        self.assertEqual(log.get_last(50), 50)
        self.assertEqual(log.get_last(20), 80)

if __name__ == "__main__":
    unittest.main()