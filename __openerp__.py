# -*- coding: utf-8 -*-
#/#############################################################################
#
#    CaPham
#    Copyright (C) 2016-TODAY capham(<capham.vn@gmail.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################
{
    'name': 'Stop Phoning Home',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Tools',
    'description': """
        Remove Few Phoning home feature effect from Odoo.
    """,
    'author': 'Ca Pham',
    'website': 'www.carlpham.com',
    'depends': ["mail",'web'],
    'init_xml': [],
    'data': [
        "base_view.xml",
        "mail_data.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
        "static/src/xml/base.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
