#!/usr/bin/env python3

"""Module containing the Pdbfixinsert class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu


class Pdbfixinsert(BiobbObject):
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

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())

    def run(self) -> None:
        """Execute the :class:`Pdbfixinsert <biobb_pdb_tools.pdb_tools.pdb_fixinsert>` object."""

        instructions = []
        if self.residues:
            instructions.append("-" + str(self.residues))
            fu.log("Appending specific residues to delete insertion codes for",
                   self.out_log, self.global_log)

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


biobb_pdb_fixinsert = launcher(Pdbfixinsert)

if __name__ == "__main__":
    Pdbfixinsert.main()
