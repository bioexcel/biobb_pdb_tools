#!/usr/bin/env python3

"""Module containing the Chainxseg class and the command line interface."""

import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger


class Chainxseg(BiobbObject):
    """
    | biobb_pdb_tools Pdbtidy
    | Swaps the segment identifier for the chain identifier.
    | This tool swaps the segment identifier for the chain identifier in a PDB file. It can be used to change the segment identifier of a PDB file or to remove the segment identifier from a PDB file.

    Args:
        input_file_path (str): PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): PDB file with exchanged segment and string identifier. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_chainxseg.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic):
            * **binary_path** (*str*) - ("pdb_chainxseg") Path to the pdb_chainxseg executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_chainxseg import biobb_pdb_chainxseg

            biobb_pdb_chainxseg(input_file_path='/path/to/input.pdb',
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

        self.binary_path = properties.get("binary_path", "pdb_chainxseg")
        self.properties = properties

        self.check_properties(properties)
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Chainxseg <biobb_pdb_tools.pdb_tools.pdb_chainxseg>` object."""

        if self.check_restart():
            return 0
        self.stage_files()

        self.cmd = [
            self.binary_path,
            self.stage_io_dict["in"]["input_file_path"],
            ">",
            self.io_dict["out"]["output_file_path"],
        ]

        fu.log(" ".join(self.cmd), self.out_log, self.global_log)

        fu.log(
            "Creating command line with instructions and required arguments",
            self.out_log,
            self.global_log,
        )

        self.run_biobb()

        self.copy_to_host()

        self.tmp_files.extend([self.stage_io_dict.get("unique_dir", "")])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def biobb_pdb_chainxseg(
    input_file_path: str,
    output_file_path: str,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create :class:`biobb_pdb_tools.pdb_tools.pdb_chainxseg>` class and
    execute the :meth:`launch() <biobb_pdb_tools.pdb_tools.pdb_chainxseg.launch>` method."""
    return Chainxseg(
        input_file_path=input_file_path,
        output_file_path=output_file_path,
        properties=properties,
        **kwargs,
    ).launch()


biobb_pdb_chainxseg.__doc__ = Chainxseg.__doc__


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(
        description="Swaps the segment identifier for the chain identifier.",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(
            prog, width=99999),
    )
    parser.add_argument("--config", required=True, help="Configuration file")

    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument(
        "--input_file_path",
        required=True,
        help="Description for the first input file path. Accepted formats: pdb.",
    )
    required_args.add_argument(
        "--output_file_path",
        required=True,
        help="Description for the output file path. Accepted formats: pdb.",
    )

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    biobb_pdb_chainxseg(
        input_file_path=args.input_file_path,
        output_file_path=args.output_file_path,
        properties=properties,
    )


if __name__ == "__main__":
    main()
