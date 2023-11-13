#!/usr/bin/env python3

"""Module containing the Pdbtidy class and the command line interface."""
import argparse
import shutil
from pathlib import PurePath
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger

class Pdbtidy(BiobbObject):
    """
    | biobb_pdb_tools Pdbtidy
    | Modifies the file to adhere (as much as possible) to the format specifications.
    
    Args:        
        input_file_path (str): Description for the first input file path. File type: input. `Sample file <https://urlto.sample>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): Description for the output file path. File type: output. `Sample file <https://urlto.sample>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **strict** (*string*) - ('strict') Does not add TER on chain breaks.
            * **binary_path** (*str*) - ("pdb_tidy") Will remove all original TER/END statements from the file.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_tidy import Pdbtidy

            prop = { 
                'binary_path': pdb_tidy,
                'strict': strict 
            }
            biobb_pdb_tidy(input_file_path='/path/to/input.pdb',
                    output_file_path='/path/to/output.pdb',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: pdb_tools
            * version: >=2.5.0
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_file_path, output_file_path, 
                 properties = None, **kwargs) -> None:
        properties = properties or {}

        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        self.io_dict = { 
            'in': { 'input_file_path': input_file_path }, 
            'out': { 'output_file_path': output_file_path } 
        }

        self.binary_path = properties.get('binary_path', 'pdb_tidy')
        self.strict = properties.get('strict', False)
        self.properties = properties

        self.check_properties(properties)
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Pdbtidy <biobb_pdb_tools.pdb_tools.pdb_tidy>` object."""

        if self.check_restart(): return 0
        self.stage_files()

        self.tmp_folder = fu.create_unique_dir()
        fu.log('Creating %s temporary folder' % self.tmp_folder, self.out_log)
        shutil.copy(self.io_dict['in']['input_file_path'], self.tmp_folder)

        instructions = []
        if self.strict:
            instructions.append('-'+ str(self.strict))
            fu.log('Appending optional boolean property', self.out_log, self.global_log)

        self.cmd = [self.binary_path,
                ' '.join(instructions),
                self.io_dict['in']['input_file_path'],
                '>',
                self.io_dict['out']['output_file_path']
        ]

        print(self.cmd)
        
        fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)

        self.run_biobb()
        self.copy_to_host()

        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            self.tmp_folder
        ])
        self.remove_tmp_files()
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code

def biobb_pdb_tidy(input_file_path: str, output_file_path: str,  properties: dict = None, **kwargs) -> int:
    """Create :class:`Pdbtidy <biobb_pdb_tools.pdb_tools.pdb_tidy>` class and
    execute the :meth:`launch() <biobb_pdb_tools.pdb_tools.pdb_tidy.launch>` method."""

    return Pdbtidy(input_file_path=input_file_path,output_file_path=output_file_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description='Modifies the file to adhere (as much as possible) to the format specifications.', formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=True, help='Configuration file')

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_file_path', required=True, help='Description for the first input file path. Accepted formats: pdb.')
    required_args.add_argument('--output_file_path', required=True, help='Description for the output file path. Accepted formats: pdb.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    biobb_pdb_tidy(input_file_path=args.input_file_path, 
            output_file_path=args.output_file_path, 
            properties=properties)

if __name__ == '__main__':
    main()