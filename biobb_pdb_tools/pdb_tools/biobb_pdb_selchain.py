#!/usr/bin/env python3

"""Module containing the Pdbselchain class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu


class Pdbselchain(BiobbObject):
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

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())

    def run(self) -> None:
        """Execute the :class:`Pdbselchain <biobb_pdb_tools.pdb_tools.pdb_selchain>` object."""

        instructions = []
        if self.chains:
            instructions.append("-" + str(self.chains))
            fu.log("Appending chains to select", self.out_log, self.global_log)

        self.cmd = [
            self.binary_path,
            " ".join(instructions),
            self.stage_io_dict["in"]["input_file_path"],
            ">",
            self.stage_io_dict["out"]["output_file_path"],
        ]

        fu.log(" ".join(self.cmd), self.out_log, self.global_log)

        fu.log(
            "Creating command line with instructions and required arguments",
            self.out_log,
            self.global_log,
        )

        self.run_biobb()


biobb_pdb_selchain = launcher(Pdbselchain)

if __name__ == "__main__":
    Pdbselchain.main()
