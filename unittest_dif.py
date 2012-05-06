#!/usr/bin/env python2.7

#When used from the command line, the module can automatically discover tests.
#For example, the following command will search the test/ subdirectory for any importable test files named test*.py
#python -m unittest discover -s test

#The command supports some other new options:
#-b or --buffer will buffer the standard output and standard error streams during each test.
#-c or --catch will cause the control-C interrupt to be handled more gracefully. Instead of interrupting the test process immediately,
#   the currently running test will be completed and then the partial results up to the interruption will be reported.
#-f or --failfast makes test execution stop immediately when a test fails instead of continuing to execute further tests

import unittest

class T(unittest.TestCase):
    #Module- and class-level setup and teardown fixtures are now supported. 
    #Modules can contain setUpModule() and tearDownModule() functions. 
    #Classes can have setUpClass() and tearDownClass() methods that \
    #must be defined as class methods (using @classmethod or equivalent). 
    #These functions and methods are invoked when the test runner switches to a test case in a different module or class. 
    @classmethod
    def setUpClass(cls):
        #execute for one time
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #The assertRaises() method now returns a context handler when called without providing a callable object to run
    def test_raise_exception(self):
        d = dict(name='huo')
        with self.assertRaises(KeyError):
            d['xiaoyu']
    #
    #new methods added: assertIsNone/assertIsNotNone, assertIs/assertIsNot, assertIsInstance/assertNotIsInstance
    #                   assertGreater/assertGreaterEqual, assertLess/assertLessEqual
    #                   assertMultilineEqual
    #                   assertRegexpMatches/assertNotRegexpMatches
    #                   assertRaisesRegexp
    #                   assertInt/assertNotInt
    #                   assertItemsEqual
    #                   assertSetEqual/assertListEqual/assertTupleEqual/assertDictEqual
    #                   assertAlmostEqual/assertNotAlmostEqual


    #
    #new features added:
    #   we can extend the assertEqual() method to handle new data type
    #   unittest.main() now takes an optional exit argument. If False, main() doesnot call sys.exit(), 
    #       allowing main() to be used from the interactive interpreter

    def test_is_x(self):
        self.assertIsNone(None)
        self.assertIsNotNone('')

        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)
        self.assertIsNot(a, [1, 2, 3])

        self.assertIsInstance(a, list)
        self.assertNotIsInstance(a, tuple)
    
    def test_mutiline_equal(self):
        str_a = """Dou
        ban"""
        str_b = """Dou
        ban"""
        self.assertMultiLineEqual(str_a, str_b)

    def test_regexp_match(self):
        self.assertRegexpMatches('douban2012', r'.\d{4}')
        self.assertNotRegexpMatches('douban201', r'.\d{4}')

    def assert_container_equal(self):
        self.assertSetEqual(set([1,2,3]), set([3,2,1]))
        self.assertListEqual(list(1,2,3), list(3,2,1))
        self.assertTupleEqual((1,2,3), (3,2,1))
        self.assertDictEqual(dict(a=1, b=2), {"a":1, "b":2})
        
if __name__ == '__main__':
    unittest.main()
