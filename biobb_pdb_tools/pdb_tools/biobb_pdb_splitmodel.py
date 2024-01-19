#!/usr/bin/env python3

"""Module containing the Pdbsplitmodel class and the command line interface."""
import argparse
from pathlib import Path
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
import os
import glob
import zipfile


class Pdbsplitmodel(BiobbObject):
    """
    | biobb_pdb_tools Pdbsplitmodel
    | Splits a PDB file into several, each containing one MODEL.

    Args:
        input_file_path (str): PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_splitmodel.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): ZIP file containing all PDB files splited by protein model. File type: output. `Sample file <https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_splitmodel.zip>`_. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **binary_path** (*str*) - ("pdb_splitmodel") Path to the pdb_splitmodel executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_splitmodel import biobb_pdb_splitmodel

            biobb_pdb_splitmodel(input_file_path='/path/to/input.pdb',
                    output_file_path='/path/to/output.zip)

    Info:
        * wrapped_software:
            * name: pdb_tools
            * version: >=2.5.0
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_file_path, output_file_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        super().__init__(properties)
        self.locals_var_dict = locals().copy()
        self.io_dict = {
            'in': {'input_file_path': input_file_path},
            'out': {'output_file_path': output_file_path}
        }

        self.binary_path = properties.get('binary_path', 'pdb_splitmodel')
        self.properties = properties

        self.check_properties(properties)
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Pdbsplitmodel <biobb_pdb_tools.pdb_tools.pdb_splitmodel>` object."""

        if self.check_restart():
            return 0
        self.stage_files()

        self.cmd = ['cd', self.stage_io_dict.get("unique_dir"), ';', self.binary_path, self.stage_io_dict['in']['input_file_path']]

        fu.log(self.cmd, self.out_log, self.global_log)

        fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)
        self.run_biobb()

        stem = Path(self.stage_io_dict['in']['input_file_path']).stem
        pdb_files = glob.glob(os.path.join(self.stage_io_dict.get("unique_dir"), stem + '_*.pdb'))

        if len(pdb_files) > 1:
            output_zip_path = os.path.join(self.stage_io_dict.get("unique_dir"), self.stage_io_dict['out']['output_file_path'])
            fu.log('Saving %d pdb model files in a zip' % len(pdb_files), self.out_log, self.global_log)
            with zipfile.ZipFile(output_zip_path, 'w') as zipf:
                for pdb_file in pdb_files:
                    zipf.write(pdb_file, os.path.basename(pdb_file))
        else:
            fu.log('The given input file has no models.', self.out_log, self.global_log)
            output_zip_path = os.path.join(self.stage_io_dict.get("unique_dir"), self.stage_io_dict['out']['output_file_path'])
            with zipfile.ZipFile(output_zip_path, 'w') as zipf:
                zipf.write(self.stage_io_dict['in']['input_file_path'], os.path.basename(self.stage_io_dict['in']['input_file_path']))
            pass

        self.copy_to_host()
        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir")
        ])
        self.remove_tmp_files()
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def biobb_pdb_splitmodel(input_file_path: str, output_file_path: str, properties: dict = None, **kwargs) -> int:
    """Create :class:`Pdbsplitmodel <biobb_pdb_tools.pdb_tools.pdb_splitmodel>` class and
    execute the :meth:`launch() <biobb_pdb_tools.pdb_tools.pdb_splitmodel.launch>` method."""

    return Pdbsplitmodel(input_file_path=input_file_path, output_file_path=output_file_path, properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description='Splits a PDB file into several, each containing one MODEL.', formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=True, help='Configuration file')

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_file_path', required=True, help='Description for the first input file path. Accepted formats: pdb.')
    required_args.add_argument('--output_file_path', required=True, help='Description for the output file path. Accepted formats: zip.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    biobb_pdb_splitmodel(input_file_path=args.input_file_path, output_file_path=args.output_file_path, properties=properties)


if __name__ == '__main__':
    main()
