"""
    tablereader.tests
    ~~~~~~~~~~~~~~~~~

    Unit tests

    :copyright: 12.2017 by Markus Ullmann, mail@markus-ullmann.de

    :license: BSD-3
"""

#
# python imports
from collections import OrderedDict
import unittest
import os.path
from os.path import join as pjoin

#
# environment imports

#
# local imports
import tablereader

#
# constants


class TablereaderTestCase(unittest.TestCase):

    maxDiff = 2048

    def setUp(self):
        self.samplefiles_directory = pjoin(os.path.dirname(os.path.abspath(__file__)), "sample_files")

    def test_test_simple_xlsx_file(self):
        reader = tablereader.TableReader(pjoin(self.samplefiles_directory, "test_simple.xlsx"))
        expected_result = [OrderedDict(
            {
                'Name': 'Beispiel',
                'Artikelnummer': "12345",
                'Preis': "2.35",
                'Gewicht': "0.125"
            }),
            OrderedDict({
                'Name': 'Beispiel2',
                'Artikelnummer': "23456",
                'Preis': "2.48",
                'Gewicht': "2.5"
            })
        ]
        actual_data = [row for row in reader]
        self.assertEqual(expected_result, actual_data)

    def test_test_simple_xls_file(self):
        reader = tablereader.TableReader(pjoin(self.samplefiles_directory, "test_simple.xls"))
        expected_result = [OrderedDict(
            {
                'Name': 'Beispiel',
                'Artikelnummer': "12345.0",
                'Preis': "2.35",
                'Gewicht': "0.125"
            }),
            OrderedDict({
                'Name': 'Beispiel2',
                'Artikelnummer': "23456.0",
                'Preis': "2.48",
                'Gewicht': "2.5"
            })
        ]
        actual_data = [row for row in reader]
        self.assertEqual(expected_result, actual_data)

    def test_test_simple_csv_german_file(self):
        reader = tablereader.TableReader(pjoin(self.samplefiles_directory, "test_simple_german.csv"))
        expected_result = [OrderedDict(
            {
                'Name': 'Beispiel',
                'Artikelnummer': "12345",
                'Preis': "2,35",
                'Gewicht': "0,125"
            }),
            OrderedDict({
                'Name': 'Beispiel2',
                'Artikelnummer': "23456",
                'Preis': "2,48",
                'Gewicht': "2,5"
            })
        ]
        actual_data = [row for row in reader]
        self.assertEqual(expected_result, actual_data)

    def test_test_simple_csv_usenglish_file(self):
        reader = tablereader.TableReader(pjoin(self.samplefiles_directory, "test_simple_usenglish.csv"), quotechar="'", delimiter=",")
        expected_result = [OrderedDict(
            {
                'Name': 'Beispiel',
                'Artikelnummer': "12345",
                'Preis': "2.35",
                'Gewicht': "0.125"
            }),
            OrderedDict({
                'Name': 'Beispiel2',
                'Artikelnummer': "23456",
                'Preis': "2.48",
                'Gewicht': "2.5"
            })
        ]
        actual_data = [row for row in reader]
        self.assertEqual(expected_result, actual_data)
