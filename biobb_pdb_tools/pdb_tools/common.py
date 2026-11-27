"""Module containing the base classes shared by the pdb-tools building blocks."""

import glob
import zipfile
from pathlib import Path
from typing import ClassVar, Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu


class PdbToolsBase(BiobbObject):
    """Base of the pdb-tools blocks that go from the input file to the output file, the stdout of the tool."""

    #: Property whose value is the option of the tool (chain "A" gives ``-A``)
    option_property: ClassVar[Optional[str]] = None
    #: Boolean property that gives the option of its name (strict gives ``-strict``)
    flag_property: ClassVar[Optional[str]] = None
    #: The input can be a zip, whose PDB files the tool takes
    zip_input: ClassVar[bool] = False

    def input_files(self) -> list[str]:
        """Go from the input file to the files of the command: the input file, or the PDB files of
        a zip input (extracted in the sandbox, sorted by name, without the macOS ``._*`` files)."""
        input_file = self.sandbox_file("input_file_path")
        if not (self.zip_input and input_file and zipfile.is_zipfile(input_file)):
            return [self.stage_io_dict["in"]["input_file_path"]]
        with zipfile.ZipFile(input_file) as zip_file:
            zip_file.extractall(self.stage_io_dict["unique_dir"])
            names = zip_file.namelist()
        pdb_names = [name for name in names if name.lower().endswith(".pdb") and not Path(name).name.startswith("._")]
        return sorted(pdb_names, key=lambda name: Path(name).stem.upper())

    def run(self) -> None:
        """Run the tool with its option, the input files and the output file as its stdout."""
        self.cmd = [self.binary_path]
        value = getattr(self, self.option_property) if self.option_property else None
        if value is not None and value != "":
            self.cmd.append(f"-{value}")
        if self.flag_property and getattr(self, self.flag_property):
            self.cmd.append(f"-{self.flag_property}")
        self.cmd += [*self.input_files(), ">", self.stage_io_dict["out"]["output_file_path"]]
        self.run_biobb()


class PdbSplitBase(BiobbObject):
    """Base of the pdb-tools blocks that go from a PDB file to a zip with one PDB file per model or segment."""

    #: What the tool splits the input by ("model" or "segment"), for the log
    split_by: ClassVar[str] = ""

    def run(self) -> None:
        """Run the tool, which writes <input name>_<model or segment>.pdb where it runs, and zip
        those files: the input file if there are none."""
        input_file = self.stage_io_dict["in"]["input_file_path"]
        self.cmd = [self.binary_path, input_file]
        self.run_biobb()
        pdb_files = glob.glob(str(Path(self.stage_io_dict["unique_dir"]) / f"{Path(input_file).stem}_*.pdb"))
        if pdb_files:
            fu.log(f"Saving {len(pdb_files)} PDB files, one per {self.split_by}, in the zip", self.out_log, self.global_log)
        else:
            fu.log(f"The input file has no {self.split_by}s: saving the input file in the zip", self.out_log, self.global_log)
            pdb_files = [str(self.sandbox_file("input_file_path"))]
        fu.zip_list(str(self.sandbox_file("output_file_path")), pdb_files)
