import unittest

from ..schema.nena_sta_006_v3 import GIS_DATA_LAYERS_REGISTRY
from ..schema.schema_fgdb_v3 import FEATURE_CLASSES, TABLES, DOMAINS


class TestNENASchema(unittest.TestCase):

    def setUp(self):
        self.registry = list(GIS_DATA_LAYERS_REGISTRY.keys())
        self.verificationErrors = []

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def test_feature_classes_in_registry(self):
        """
        Tests the feature classes define in the NENA GIS Data Model are
        listed in Section 7.2 "GIS Data Layer Registry" of NENA-STA-006.x
        """
        feature_classes = [fc['out_name'] for fc in FEATURE_CLASSES]
        known_issues = ['ProvisioningPolygon']
        for feature_class in feature_classes:
            if feature_class not in known_issues:
                msg = f'{feature_class} not found in GIS Data Layers Registry'
                self.assertIn(feature_class, self.registry, msg)

    def test_tables_in_registry(self):
        """
        Tests the tables defined in the NENA GIS Data Model are listed
        in Section 7.2 "GIS Data Layer Registry" of NENA-STA-006.x
        """
        tables = [tbl['out_name'] for tbl in TABLES]
        known_issues = ['LandmarkNamePartTable']
        for table in tables:
            if table not in known_issues:
                msg = f'{table} not found in GIS Data Layers Registry'
                self.assertIn(table, self.registry, msg)


if __name__ == '__main__':
    unittest.main()
