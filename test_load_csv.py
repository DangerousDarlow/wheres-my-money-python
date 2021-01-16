from csv import reader as CsvReader
from io import StringIO

from load_csv import buildFieldLookup



def test_field_names_have_leading_and_trailing_whitespace_trimmed():
    reader = CsvReader(StringIO(' header1, header 2  ,header3 '))
    fields = buildFieldLookup(reader)
    assert len(fields) == 3
    assert fields['header1'] == 0
    assert fields['header 2'] == 1
    assert fields['header3'] == 2

def test_field_names_are_all_lower_case():
    reader = CsvReader(StringIO('hEaDer'))
    fields = buildFieldLookup(reader)
    assert len(fields) == 1
    assert fields['header'] == 0

def test_leading_blank_lines_are_ignored():
    reader = CsvReader(StringIO("""
    
    header"""))
    fields = buildFieldLookup(reader)
    assert len(fields) == 1
    assert fields['header'] == 0