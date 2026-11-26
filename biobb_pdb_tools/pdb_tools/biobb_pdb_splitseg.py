#!/usr/bin/env python3

"""Module containing the Pdbsplitseg class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbSplitBase


class Pdbsplitseg(PdbSplitBase):
    """
    | biobb_pdb_tools Pdbsplitseg
    | Splits a PDB file into several, each containing one segment.
    | This tool splits a PDB file into several, each containing one segment. It can be used to split a PDB file into several, each containing one segment.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_splitseg.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): ZIP file containing all PDB files splited by protein segment. File type: output. `Sample file <https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_splitseg.zip>`_. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **binary_path** (*str*) - ("pdb_splitseg") Path to the pdb_splitseg executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_splitseg import biobb_pdb_splitseg

            biobb_pdb_splitseg(input_file_path='/path/to/input.pdb',
                    output_file_path='/path/to/output.pdb')

    Info:
        * wrapped_software:
            * name: pdb_tools
            * version: >=2.5.0
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    split_by = "segment"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_splitseg = launcher(Pdbsplitseg)

if __name__ == "__main__":
    Pdbsplitseg.main()
