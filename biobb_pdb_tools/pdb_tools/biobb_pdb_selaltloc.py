#!/usr/bin/env python3

"""Module containing the Pdbselaltloc class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbToolsBase


class Pdbselaltloc(PdbToolsBase):
    """
    | biobb_pdb_tools Pdbselaltloc
    | Selects alternative locations from a PDB file.
    | By default, selects the label with the highest occupancy value for each atom, but the user can define a specific altloc label to select. Selecting by highest occupancy removes all altloc labels for all atoms. If the user provides an option (e.g. -A), only atoms with conformers with an altloc A are processed by the script.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/9INS.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): PDB file with selected alternative locations. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_selaltloc.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **altloc** (*string*) - (None) Specific alternative location label to select (e.g. "A").
            * **binary_path** (*str*) - ("pdb_selaltloc") Path to the pdb_selaltloc executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_selaltloc import biobb_pdb_selaltloc

            # Select the highest occupancy alternative locations
            biobb_pdb_selaltloc(input_file_path='/path/to/input.pdb',
                    output_file_path='/path/to/output.pdb')

            # Select a specific alternative location label
            prop = {
                'altloc': 'A'
            }
            biobb_pdb_selaltloc(input_file_path='/path/to/input.pdb',
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

    option_property = "altloc"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_selaltloc = launcher(Pdbselaltloc)

if __name__ == "__main__":
    Pdbselaltloc.main()
