import argparse
from consts import *
from csv_utils import read_sld_bom, write_bom
from bom_utils import check_vendors, analyze_part


headers = ['part', 'sku', 'vendor', "quantity", 'material', 'first machine', 'second machine', 'third machine',
           'fourth machine', ]


def main():
    bom = read_sld_bom('bom.csv')
    new_bom = [headers]
    for line in bom:
        vendor = check_vendors(line[PART_NAME])
        if not vendor:
            part_sku, machines = analyze_part(line[PART_NAME])
            new_line = [line[PART_NAME], part_sku, 'inhouse', line[COUNT], ''] + machines
        else:
            part_sku, link, vendor_name = vendor
            new_line = [line[PART_NAME], part_sku, vendor_name, line[COUNT], link]
        new_bom += [new_line]
    write_bom('galaxia_bom.csv', new_bom)

class bominator_argparse():
    

if __name__ == '__main__':
    main()
