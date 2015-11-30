# This file is part of the stock_picking_kit module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockPickingKitTestCase(ModuleTestCase):
    'Test Stock Picking Photo module'
    module = 'stock_picking_kit'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockPickingKitTestCase))
    return suite
