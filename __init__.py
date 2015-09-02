#This file is part stock_picking_kit module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *

def register():
    Pool.register(
        ShipmentOutPacked,
        module='stock_picking_kit', type_='wizard')
