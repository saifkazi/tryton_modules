# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import gstr1

__all__ = ['register']


def register():
    Pool.register(
        gstr1.CreateGSTR,
        module='gstr1', type_='model')
    Pool.register(
        gstr1.GSTR1Report,
        module='gstr1', type_='wizard')
    Pool.register(
        gstr1.GSTR1EXCEL,
        module='gstr1', type_='report')
