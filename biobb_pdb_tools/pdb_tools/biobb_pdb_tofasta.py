#!/usr/bin/env python3

"""Module containing the Pdbtofasta class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_pdb_tools.pdb_tools.common import PdbToolsBase


class Pdbtofasta(PdbToolsBase):
    """
    | biobb_pdb_tofasta Pdbtofasta
    | Extracts the residue sequence in a PDB file to FASTA format.
    | This tool extracts the residue sequence in a PDB file to FASTA format. It can be used to extract the sequence of a PDB file to FASTA format.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): FASTA file containing the aminoacids sequence. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_tofasta.fasta>`_. Accepted formats: fasta (edam:format_1929), fa (edam:format_1929).
        properties (dic):
            * **multi** (*bool*) - (True) Splits the different chains into different records in the FASTA file.
            * **binary_path** (*str*) - ("pdb_tofasta") Path to the pdb_tofasta executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_tofasta import biobb_pdb_tofasta

            prop = {
                'multi': True
            }
            biobb_pdb_tofasta(input_file_path='/path/to/input.pdb',
                    output_file_path='/path/to/output.fasta',
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

    flag_property = "multi"

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())


biobb_pdb_tofasta = launcher(Pdbtofasta)

if __name__ == "__main__":
    Pdbtofasta.main()
