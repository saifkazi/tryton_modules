# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.analytic_sale.tests.test_analytic_sale import suite
except ImportError:
    from .test_analytic_sale import suite

__all__ = ['suite']
