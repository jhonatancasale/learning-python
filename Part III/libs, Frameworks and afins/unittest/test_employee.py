'''from https://www.youtube.com/watch?v=6tNS--WetLI'''


import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\nsetUpClass')


    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')


    def setUp(self):
        print('\nsetUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)


    def tearDown(self):
        print('\ntearDown')
        pass


    def test_email(self):
        print('\ntest_email')
        self.assertEqual(self.emp_1.email, 'corey.schafer@email.com')
        self.assertEqual(self.emp_2.email, 'sue.smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'john.schafer@email.com')
        self.assertEqual(self.emp_2.email, 'jane.smith@email.com')


    def test_full_name(self):
        print('\ntest_full_name')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')


    def test_apply_raise(self):
        print('\ntest_apply_raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


    def test_monthly_schedule(self):
        print('\ntest_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')


            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad response!')
