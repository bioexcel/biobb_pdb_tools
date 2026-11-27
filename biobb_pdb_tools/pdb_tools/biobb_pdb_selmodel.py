#!/usr/bin/env python3

"""Module containing the Pdbselmodel class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbToolsBase


class Pdbselmodel(PdbToolsBase):
    """
    | biobb_pdb_tools Pdbselmodel
    | Extracts one or more models from a PDB file.
    | This tool extracts one or more models from a PDB file. If the PDB file has no MODEL records, returns the entire file.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_splitmodel.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): PDB file with selected models. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_selmodel.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **models** (*str*) - ('1') Model or list of models (comma separated) to extract from the PDB file.
            * **binary_path** (*str*) - ("pdb_selmodel") Path to the pdb_selmodel executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_selmodel import biobb_pdb_selmodel

            prop = {
                'models': '1,3'
            }
            biobb_pdb_selmodel(input_file_path='/path/to/input.pdb',
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

    option_property = "models"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_selmodel = launcher(Pdbselmodel)

if __name__ == "__main__":
    Pdbselmodel.main()
