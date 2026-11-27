#!/usr/bin/env python3

"""Module containing the Pdbseg class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbToolsBase


class Pdbseg(PdbToolsBase):
    """
    | biobb_pdb_tools Pdbseg
    | Modifies the segment identifier column of a PDB file.
    | This tool modifies the segment identifier column of a PDB file. It can be used to change the segment identifier of a PDB file or to remove the segment identifier from a PDB file.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_seg.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): PDB file with segment identifier column modified. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_seg.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **segment** (*str*) - (None) Default is an empty segment.
            * **binary_path** (*str*) - ("pdb_seg") Path to the pdb_seg executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_seg import biobb_pdb_seg

            prop = {
                'segment': 'A'
            }
            biobb_pdb_seg(input_file_path='/path/to/input.pdb',
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

    option_property = "segment"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_seg = launcher(Pdbseg)

if __name__ == "__main__":
    Pdbseg.main()
