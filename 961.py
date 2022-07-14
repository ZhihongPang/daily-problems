"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Quora.
Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.
For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
"""
# research to better understand the problem
# notes: in Unix systems, "." refers to the current directory, and ".." refers to the previous directory
#        absolute path defines a path from the root of the file system, "C:\\" in windows, "/" in unix systems
#        standardized path/canonical path refers to the unique path 
#        os.path.realpath(path) solves this problem, but it is os bound
# rules: 1. path name begins with "/" as it is the root (in unix systems)
#        2. there must be a "/" between directory names
#        3. return the shortest standard path
#        4. consecutive "/" is the same as "."

import unittest

# solution assumes the path is for unix systems, no input check so special characters are accepted as directory names
def get_canonical_path(absolute_path):
    current_path = []                           # stores directory names
    absolute_path = absolute_path.split("/")    # creates a stream of tokens
    for path in absolute_path:
        if path == "." or path == "/":
            continue
        if path == "..":
            if len(current_path) > 0:
                current_path.pop()
            continue
        else:
            current_path.append(path)

    for path in current_path:
        if not path:
            current_path.remove(path)
    shortest_path = "/".join(current_path)
    return "/" + shortest_path

class Test(unittest.TestCase):
    def test_given(self):
        self.assertEqual(get_canonical_path("/usr/bin/../bin/./scripts/../"), "/usr/bin")
    def test_only_period(self):
        self.assertEqual(get_canonical_path("/./././././././././"), "/")
    def test_only_periods(self):
        self.assertEqual(get_canonical_path("/../../../../../../../"), "/")
    def test_mixed_periods(self):
        self.assertEqual(get_canonical_path("/./././../.././.././../"), "/")
    def test_periods_check(self):
        self.assertEqual(get_canonical_path("/home/././../"), "/")
    def test_period_check(self):
        self.assertEqual(get_canonical_path("/home/././"), "/home")
    def test_already_shortest_path(self):
        self.assertEqual(get_canonical_path("/home/usr/bin/"), "/home/usr/bin")
    def test_just_slash(self):
        self.assertEqual(get_canonical_path("/"), "/")
    def test_longer_path(self):
        self.assertEqual(get_canonical_path("/home/usr/bin/folder1/folder2/folder3/folder4/../../../../../"), "/home/usr")

if __name__ == "__main__":
    unittest.main()