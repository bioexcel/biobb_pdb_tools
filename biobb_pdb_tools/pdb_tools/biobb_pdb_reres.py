#!/usr/bin/env python3

"""Module containing the Pdbreres class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu


class Pdbreres(BiobbObject):
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

    def __init__(
        self, input_file_path, output_file_path, properties=None, **kwargs
    ) -> None:
        properties = properties or {}

        super().__init__(properties)
        self.locals_var_dict = locals().copy()
        self.io_dict = {
            "in": {"input_file_path": input_file_path},
            "out": {"output_file_path": output_file_path},
        }

        self.binary_path = properties.get("binary_path", "pdb_reres")
        self.number = properties.get("number")
        self.properties = properties

    def run(self) -> None:
        """Execute the :class:`Pdbreres <biobb_pdb_tools.pdb_tools.pdb_reres>` object."""

        instructions = []
        if self.number is not None:
            instructions.append("-" + str(self.number))
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


def biobb_pdb_reres(
    input_file_path: str,
    output_file_path: str,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`Pdbreres <biobb_pdb_tools.pdb_tools.pdb_reres>` class and
    execute the :meth:`launch() <biobb_pdb_tools.pdb_tools.pdb_reres.launch>` method."""

    return Pdbreres(**dict(locals())).launch()


biobb_pdb_reres.__doc__ = Pdbreres.__doc__
main = Pdbreres.get_main(biobb_pdb_reres, "Renumbers the residues of the PDB file starting from a given number (default 1).")

if __name__ == "__main__":
    main()
