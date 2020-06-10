import ehr_code_mappings as mappings
import pandas as pd
import unittest
import os


class CodesTest(unittest.TestCase):

    @staticmethod
    def test_load_entire_ccs():
        pd.testing.assert_frame_equal(
            mappings.load_mapping('ccs_icd10', version=1),
            pd.read_csv(os.path.join('..', 'ehr_code_mappings', 'mappings', 'ccs_icd10.v1.csv'))
        )

    def test_load_ccs_level(self):
        result = mappings.load_mapping('ccs_icd10', version=1)
        result = result[result['Level2'] == '2.15']

        self.assertEqual(
            result['Code'].values.tolist(),
            ['Z510', 'Z5111', 'Z5112']
        )

        # Just to make sure that the assertion on lists is correct
        self.assertNotEqual(
            result['Code'].values.tolist(),
            ['Z510', 'Z5111']
        )
        self.assertNotEqual(
            result['Code'].values.tolist(),
            ['Z510', 'Z5111', 'abc']
        )
