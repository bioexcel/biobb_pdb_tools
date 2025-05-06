# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_pdb_tools.pdb_tools.biobb_pdb_selaltloc import biobb_pdb_selaltloc


class TestPdbSelAltLoc():
    def setup_class(self):
        fx.test_setup(self, 'biobb_pdb_selaltloc')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_pdbselaltloc(self):
        returncode = biobb_pdb_selaltloc(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
