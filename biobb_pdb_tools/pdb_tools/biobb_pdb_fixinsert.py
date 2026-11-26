#!/usr/bin/env python3

"""Module containing the Pdbfixinsert class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbToolsBase


class Pdbfixinsert(PdbToolsBase):
    """
    | biobb_pdb_tools Pdbfixinsert
    | Deletes insertion codes and shifts the residue numbering of downstream residues.
    | Works by deleting an insertion code and shifting the residue numbering of downstream residues. Allows for picking specific residues to delete insertion codes for.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1IGY.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): PDB file with fixed insertion codes. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_fixinsert.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **residues** (*string*) - (None) Specific residues to delete insertion codes for, format: "A9,B12" (chain and residue number).
            * **binary_path** (*str*) - ("pdb_fixinsert") Path to the pdb_fixinsert executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_fixinsert import biobb_pdb_fixinsert

            # Delete specific insertion codes
            prop = {
                'residues': 'A9,B12'
            }
            biobb_pdb_fixinsert(input_file_path='/path/to/input.pdb',
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

    option_property = "residues"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_fixinsert = launcher(Pdbfixinsert)

if __name__ == "__main__":
    Pdbfixinsert.main()
