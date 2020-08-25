"""
Package providing various utilities for the Miraculix software

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""
import csv


def write_csv(file, data):
    """Write data to .csv file"""
    with open(file, "w+", newline='', encoding='utf-8') as outfile:
        file_writer = csv.writer(outfile, delimiter=';')
        for row in data:
            file_writer.writerow(row)


def read_csv(file):
    """Read data from .csv file"""
    data = csv.reader(open(file, encoding='utf-8'), delimiter=';')
    rows = list(data)
    return rows


def get_index_csv_data(data, entry_dict):
    """Get index of .csv header entries"""
    indices = {}
    for entry_key in entry_dict:
        indices[str(entry_key)] = data[0].index(entry_dict[entry_key])
    return indices


def db_table_exists(db_cursor, tbl_name):
    """Check if table exists in given sqlite database"""
    db_cursor.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", [tbl_name])
    if not db_cursor.fetchone()[0] == 1:
        return False
    else:
        return True
