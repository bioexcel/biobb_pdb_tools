#!/usr/bin/env python3

"""Module containing the Pdbtidy class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu


class Pdbtidy(BiobbObject):
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

    def __init__(
        self, input_file_path: str, output_file_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())

    def run(self) -> None:
        """Execute the :class:`Pdbtidy <biobb_pdb_tools.pdb_tools.pdb_tidy>` object."""

        instructions = []
        if self.strict:
            instructions.append("-strict")
            fu.log("Appending optional boolean property",
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


biobb_pdb_tidy = launcher(Pdbtidy)


if __name__ == "__main__":
    Pdbtidy.main()
