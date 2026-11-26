#!/usr/bin/env python3

"""Module containing the Pdbsplitmodel class and the command line interface."""

import glob
import os
import zipfile
from pathlib import Path
from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu


class Pdbsplitmodel(BiobbObject):
    """
    | biobb_pdb_tools Pdbsplitmodel
    | Splits a PDB file into several, each containing one MODEL.
    | This tool splits a PDB file into several, each containing one MODEL. It can be used to split a PDB file into several, each containing one MODEL.

    Args:
        input_file_path (str): Input PDB file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_splitmodel.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_file_path (str): ZIP file containing all PDB files splited by protein model. File type: output. `Sample file <https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_splitmodel.zip>`_. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **binary_path** (*str*) - ("pdb_splitmodel") Path to the pdb_splitmodel executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_pdb_tools.pdb_tools.biobb_pdb_splitmodel import biobb_pdb_splitmodel

            biobb_pdb_splitmodel(input_file_path='/path/to/input.pdb',
                    output_file_path='/path/to/output.zip)

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
        """Execute the :class:`Pdbsplitmodel <biobb_pdb_tools.pdb_tools.pdb_splitmodel>` object."""

        self.cmd = [
            "cd",
            self.stage_io_dict.get("unique_dir", ""),
            ";",
            self.binary_path,
            self.stage_io_dict["in"]["input_file_path"],
        ]

        fu.log(" ".join(self.cmd), self.out_log, self.global_log)

        fu.log(
            "Creating command line with instructions and required arguments",
            self.out_log,
            self.global_log,
        )
        self.run_biobb()

        stem = Path(self.stage_io_dict["in"]["input_file_path"]).stem
        pdb_files = glob.glob(
            os.path.join(self.stage_io_dict.get(
                "unique_dir", ""), stem + "_*.pdb")
        )

        if pdb_files:
            output_zip_path = self.sandbox_file("output_file_path")
            fu.log(
                "Saving %d pdb model files in a zip" % len(pdb_files),
                self.out_log,
                self.global_log,
            )
            with zipfile.ZipFile(output_zip_path, "w") as zipf:
                for pdb_file in pdb_files:
                    zipf.write(pdb_file, os.path.basename(pdb_file))
        else:
            fu.log("The given input file has no models.",
                   self.out_log, self.global_log)
            output_zip_path = self.sandbox_file("output_file_path")
            with zipfile.ZipFile(output_zip_path, "w") as zipf:
                zipf.write(
                    self.sandbox_file("input_file_path"),
                    os.path.basename(
                        self.sandbox_file("input_file_path")),
                )
            pass


biobb_pdb_splitmodel = launcher(Pdbsplitmodel)

if __name__ == "__main__":
    Pdbsplitmodel.main()
