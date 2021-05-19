# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.gstr1.tests.test_gstr1 import suite  # noqa: E501
except ImportError:
    from .test_gstr1 import suite

__all__ = ['suite']
