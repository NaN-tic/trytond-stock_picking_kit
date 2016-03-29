#This file is part stock_picking_kit module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = [ 'ShipmentOutPacked']


class ShipmentOutPacked:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.packed'

    def transition_packed(self):
        Line = Pool().get('stock.shipment.out.picking.line')

        lines = self.picking.lines

        new_lines = []
        for line in lines:
            qty = line.quantity

            new_lines.append(line)
            if line.product.kit and line.product.explode_kit_in_sales:
                for l in line.product.kit_lines:
                    line = Line()
                    line.product = l.product
                    line.quantity = qty*l.quantity
                    new_lines.append(line)

        self.picking.lines = new_lines

        super(ShipmentOutPacked, self).transition_packed()
