# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2004-TODAY Nicolas Seinlet <http://www.seinlet.com>
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
##############################################################################

{
    'name' : 'modelisme',
    'version': '1.0',
    'summary': 'Un petit module de gestion de PR',
    'sequence': '19',
    'category': 'Tools',
    'complexity': 'easy',
    'description':
        """
Modelisme

Gerer les composant et le PR de modeles reduits
        """,
    'data': [
        'security/groups.xml',
        'data/picking.xml',
        'models/build.xml',
        'models/product_template.xml',
        'models/scale_op_wiz.xml',
        'models/stock.xml',
        'models/o2m.xml',
        'views/product_template.xml',
        'views/build.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
       ],
    'depends' : ['base_action_rule', 'stock', 'purchase'],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
