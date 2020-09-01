import unittest
from unittest import mock
from unittest import TestCase
import shortRunCostCurves

class TestShortRunCostCurves(unittest.TestCase):
	@mock.patch('shortRunCostCurves.input', create=True)
	def testReadTotalQuantity(self, mocked_input):
		mocked_input.side_effect = [0, -3, -12, "test", "useless string", " test2", 7]
		result = shortRunCostCurves.readTotalQuantity()
		self.assertEqual(result, 7)

	@mock.patch('shortRunCostCurves.input', create=True)
	def testReadPricePerUnit(self, mocked_input):
		mocked_input.side_effect = [-40, -33.0, "test", "useless string", " test2", 0, 0.0, 12]
		result = shortRunCostCurves.readPricePerUnit()
		self.assertEqual(result, 12.0)

	@mock.patch('shortRunCostCurves.input', create=True)
	def testReadFixedCost(self, mocked_input):
		mocked_input.side_effect = [0.0, -50, "test", "useless string", " test2", 30]
		result = shortRunCostCurves.readFixedCost()
		self.assertEqual(result, 30.0)

	@mock.patch('shortRunCostCurves.input', create=True)
	def testCreateVariableCosts(self, mocked_input):
		mocked_input.side_effect = [10, "useless string", 30, "test", 50, " test2", 70]
		result = shortRunCostCurves.createVariableCosts(4)
		self.assertEqual(result, [0.0, 10.0, 30.0, 50.0, 70.0])

	def testCreateTotalCosts(self):
		testQuantity = 5
		testVariableCosts = [70, 90, 130, 170, 190]
		testFixedCost = 40
		result = shortRunCostCurves.createTotalCosts(testFixedCost, testVariableCosts, testQuantity)
		self.assertEqual(result, [110.0, 130.0, 170.0, 210.0, 230.0])

if __name__ == '__main__':
	unittest.main()