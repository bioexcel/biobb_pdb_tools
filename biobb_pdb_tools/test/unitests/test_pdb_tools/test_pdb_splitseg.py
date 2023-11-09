from biobb_common.tools import test_fixtures as fx
from pdb_tools.biobb_pdb_splitseg import biobb_pdb_splitseg 

class TestPdbpdbsplitseg():
    def setup_class(self):
        fx.test_setup(self, 'pdb_splitseg')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_splitseg(self):
        returncode= biobb_pdb_splitseg(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
