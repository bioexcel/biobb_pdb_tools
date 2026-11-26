#!/usr/bin/env python3

"""Module containing the Pdbselchain class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbToolsBase


class Pdbselchain(PdbToolsBase):
    """
    | biobb_pdb_tools Pdbselchain
    | Extracts one or more chains from a PDB file.
    | This tool extracts a specific chain or list of chains from a PDB file, discarding all others.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_selchain.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): PDB file with selected chains. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_selchain.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **chains** (*str*) - ('A') Chain or list of chains (comma separated) to extract from the PDB file.
            * **binary_path** (*str*) - ("pdb_selchain") Path to the pdb_selchain executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_selchain import biobb_pdb_selchain

            prop = {
                'chains': 'A,B'
            }
            biobb_pdb_selchain(input_file_path='/path/to/input.pdb',
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

    option_property = "chains"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_selchain = launcher(Pdbselchain)

if __name__ == "__main__":
    Pdbselchain.main()
