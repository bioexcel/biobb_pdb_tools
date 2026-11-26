#!/usr/bin/env python3

"""Module containing the Pdbreres class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbToolsBase


class Pdbreres(PdbToolsBase):
    """
    | biobb_pdb_tools Pdbreres
    | Renumbers the residues of the PDB file starting from a given number (default 1).
    | This tool renumbers the residues of the PDB file starting from a given number (default 1). It can be used to renumber the residues of a PDB file starting from a given number.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): Renumbered PDB file by number of redisue selected. File type: output. `Sample file <https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_reres.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **number** (*int*) - (None) Number of the protein residue.
            * **binary_path** (*str*) - ("pdb_reres") Path to the pdb_reres executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_reres import biobb_pdb_reres

            prop = {
                'number': 4
            }
            biobb_pdb_reres(input_file_path='/path/to/input.pdb',
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

    option_property = "number"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_reres = launcher(Pdbreres)

if __name__ == "__main__":
    Pdbreres.main()
