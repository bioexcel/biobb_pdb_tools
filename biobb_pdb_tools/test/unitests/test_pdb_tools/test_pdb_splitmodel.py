# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_pdb_tools.pdb_tools.biobb_pdb_splitmodel import biobb_pdb_splitmodel


class TestPdbpdbsplitmodel():
    def setup_class(self):
        fx.test_setup(self, 'biobb_pdb_splitmodel')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_splitmodel(self):
        returncode = biobb_pdb_splitmodel(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
