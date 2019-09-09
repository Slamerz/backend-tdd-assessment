#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import unittest
import echo

testText = "Something to see here"


class TestEchoMethods(unittest.TestCase):
    def test_upper_method(self):
        self.assertEqual(echo.to_upper(testText), testText.upper())

    def test_lower_method(self):
        self.assertEqual(echo.to_lower(testText), testText.lower())

    def test_title_method(self):
        self.assertEqual(echo.to_title(testText), testText.title())

    def test_help_command(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
