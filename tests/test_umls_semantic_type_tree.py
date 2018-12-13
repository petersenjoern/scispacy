

import unittest

from SciSpaCy.umls_semantic_type_tree import construct_umls_tree_from_tsv

class TestUmlsSemanticTypeTree(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.tree = construct_umls_tree_from_tsv("tests/fixtures/test_umls_tree.tsv")

    def test_tree_can_be_read_from_file(self):

        correct_names = ["Activity", "Behavior", "Social Behavior", "Individual Behavior",
                         "Daily or Recreational Activity", "Event"]
        correct_ids = ['T052', 'T053', 'T054', 'T055', 'T056', 'T051']
        for node, name, umls_id in zip(self.tree.flat_nodes, correct_names, correct_ids):
            assert node.full_name == name
            assert node.type_id == umls_id

    def test_tree_can_collapse_nodes(self):
        new_mapping = self.tree.get_collapsed_type_id_map_at_level(2)
        assert new_mapping == {'T052': 'T052',
                               'T053': 'T052',
                               'T054': 'T052',
                               'T055': 'T052',
                               'T056': 'T052',
                               'T051': 'T051'}
        assert ["T052"] == self.tree.get_nodes_at_depth(2)
