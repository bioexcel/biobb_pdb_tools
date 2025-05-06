# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_pdb_tools.pdb_tools.biobb_pdb_selres import biobb_pdb_selres


class TestPdbSelres():
    def setup_class(self):
        fx.test_setup(self, 'biobb_pdb_selres')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_pdb_selres(self):
        returncode = biobb_pdb_selres(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
    