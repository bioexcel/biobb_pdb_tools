from biobb_common.tools import test_fixtures as fx
from template.template import Template

class TestTemplate():
    def setUp(self):
        fx.test_setup(self,'template')

    def tearDown(self):
        fx.test_teardown(self)

    def test_editconf(self):
        returncode= Editconf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
