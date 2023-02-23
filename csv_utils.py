import csv


def read_sld_bom(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        parts = [line for line in reader]
        return parts


def write_bom(file_name, bom_info):
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(bom_info)
