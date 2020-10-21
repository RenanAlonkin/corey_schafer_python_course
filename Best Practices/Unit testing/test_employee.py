import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Set Up Class')

    @classmethod
    def tearDownClass(cls):
        print('Tear Down Class')

    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 10000)
        self.emp_2 = Employee('Viviane', 'Silva', 20000)

        print('Set Up')

    def tearDown(self):
        print('Tear Down')


    def test_email(self):

        print('Test Email')

        self.assertEqual(self.emp_1.email, 'corey.schafer@company.com') 
        self.assertEqual(self.emp_2.email, 'viviane.silva@company.com')

        self.emp_1.first = 'Carlos'
        self.emp_2.first = 'Vivizinha'

        self.assertEqual(self.emp_1.email, 'carlos.schafer@company.com') 
        self.assertEqual(self.emp_2.email, 'vivizinha.silva@company.com')

    def test_fullname(self):

        print('Test Fullname')

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer') 
        self.assertEqual(self.emp_2.fullname, 'Viviane Silva')

        self.emp_1.first = 'Carlos'
        self.emp_2.first = 'Vivizinha'

        self.assertEqual(self.emp_1.fullname, 'Carlos Schafer') 
        self.assertEqual(self.emp_2.fullname, 'Vivizinha Silva')

    def test_apply_raise(self):

        print('Test Raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 10500) 
        self.assertEqual(self.emp_2.pay, 21000)

    def test_monthly_schedule(self):

        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
        
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')

            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
        
            schedule = self.emp_2.monthly_schedule('August')
            mocked_get.assert_called_with('http://company.com/Silva/August')

            self.assertEqual(schedule, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()