# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_pdb_tools.pdb_tools.biobb_pdb_keepcoord import biobb_pdb_keepcoord


class TestPdbKeepCoord():
    def setup_class(self):
        fx.test_setup(self, 'biobb_pdb_keepcoord')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_pdbkeepcoord(self):
        returncode = biobb_pdb_keepcoord(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
