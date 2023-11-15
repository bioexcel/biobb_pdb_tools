from biobb_common.tools import test_fixtures as fx
from biobb_pdb_tools.pdb_tools.biobb_pdb_chain import biobb_pdb_chain 

class TestPdbChain():
    def setup_class(self):
        fx.test_setup(self, 'biobb_pdb_chain')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_pdbchain(self):
        returncode= biobb_pdb_chain(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
