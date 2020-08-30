import unittest
from unittest import mock
from unittest import TestCase
import shortRunCostCurves

class TestShortRunCostCurves(unittest.TestCase):
	@mock.patch('shortRunCostCurves.input', create=True)
	def testReadTotalQuantity(self, mocked_input):
		mocked_input.side_effect = [0, -3, -12, 7]
		result = shortRunCostCurves.readTotalQuantity()
		self.assertEqual(result, 7)

	@mock.patch('shortRunCostCurves.input', create=True)
	def testReadPricePerUnit(self, mocked_input):
		mocked_input.side_effect = [-40, -33.0, 0, 0.0, 12]
		result = shortRunCostCurves.readPricePerUnit()
		self.assertEqual(result, 12.0)

	@mock.patch('shortRunCostCurves.input', create=True)
	def test_createVariableCosts(self, mocked_input):
		mocked_input.side_effect = [1.0, 2.0, 3.0, 4.0]
		result = shortRunCostCurves.createVariableCosts(4)
		self.assertEqual(result, [0.0, 1.0, 2.0, 3.0, 4.0])

if __name__ == '__main__':
	unittest.main()