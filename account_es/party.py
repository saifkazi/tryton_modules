# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    es_province_code = fields.Char("Spanish Province Code", size=2,
        help="Set 99 for non Spanish parties.")

    @fields.depends('addresses', 'es_province_code')
    def on_change_addresses(self):
        if not self.es_province_code:
            for address in self.addresses:
                country = getattr(address, 'country', None)
                zip_ = getattr(address, 'zip', None)
                if country and zip_ and country.code == 'ES':
                    self.es_province_code = zip_[:2]
                    break


class Identifier(metaclass=PoolMeta):
    __name__ = 'party.identifier'

    def es_country(self):
        if self.type == 'eu_vat':
            return self.code[:2]
        if self.type in {'es_cif', 'es_dni', 'es_nie', 'es_nif'}:
            return 'ES'

    def es_code(self):
        if self.type == 'eu_vat':
            return self.code[2:]
        return self.code
