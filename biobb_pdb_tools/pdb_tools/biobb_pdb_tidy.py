#!/usr/bin/env python3

"""Module containing the Pdbtidy class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbToolsBase


class Pdbtidy(PdbToolsBase):
    """
    | biobb_pdb_tools Pdbtidy
    | Modifies the file to adhere (as much as possible) to the format specifications.
    | This tool modifies the file to adhere (as much as possible) to the format specifications. It can be used to fix a PDB file that does not adhere to the format specifications.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): PDB file modified according to the specifications. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_tidy.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **strict** (*bool*) - (False) Does not add TER on chain breaks.
            * **binary_path** (*str*) - ("pdb_tidy") Path to the pdb_tidy executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_tidy import biobb_pdb_tidy

            prop = {
                'strict': False
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

    flag_property = "strict"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_tidy = launcher(Pdbtidy)


if __name__ == "__main__":
    Pdbtidy.main()
