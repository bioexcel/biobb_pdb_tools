# BioBB PDB Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Biobb_pdb_fetch
Downloads a structure in PDB format from the RCSB website.
### Get help
Command:
```python
biobb_pdb_fetch -h
```
    usage: biobb_pdb_fetch [-h] --config CONFIG --output_file_path OUTPUT_FILE_PATH
    
    Downloads a structure in PDB format from the RCSB website.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_file_path** (*string*): PDB file of the protein selected. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_fetch.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdbid** (*string*): (1aki) ID of the protein..
* **biounit** (*string*): (False) Allows downloading the (first) biological structure if selected..
* **binary_path** (*string*): (pdb_fetch) Downloads a structure in PDB format from the RCSB website..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_delhetatm
Removes all HETATM records in the PDB file.
### Get help
Command:
```python
biobb_pdb_delhetatm -h
```
    usage: biobb_pdb_delhetatm [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Removes all HETATM records in the PDB file.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_delhetatm.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with all HETATM records removed. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_delhetatm.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_delhetatm) Removes all HETATM records in the PDB file..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_tidy
Modifies the file to adhere (as much as possible) to the format specifications.
### Get help
Command:
```python
biobb_pdb_tidy -h
```
    usage: biobb_pdb_tidy [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Modifies the file to adhere (as much as possible) to the format specifications.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_tidy.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file modified according to the specifications. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_tidy.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **strict** (*string*): (strict) Does not add TER on chain breaks..
* **binary_path** (*string*): (pdb_tidy) Will remove all original TER/END statements from the file..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_chain
Modifies the chain identifier column of a PDB file.
### Get help
Command:
```python
biobb_pdb_chain -h
```
    usage: biobb_pdb_chain [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Modifies the chain identifier column of a PDB file.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_chain.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with selected modified chain. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_chain.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **chain** (*string*): (A) Chain identifier that is modified (default is an empty chain)..
* **binary_path** (*string*): (pdb_chain) Modifies the chain identifier column of a PDB file..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_seg
Modifies the segment identifier column of a PDB file.
### Get help
Command:
```python
biobb_pdb_seg -h
```
    usage: biobb_pdb_seg [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Modifies the segment identifier column of a PDB file.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_seg.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with segment identifier column modified. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_seg.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **segment** (*string*): (B) Default is an empty segment..
* **binary_path** (*string*): (pdb_seg) Modifies the segment identifier column of a PDB file..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_mkensemble
Merges several PDB files into one multi-model (ensemble) file.
### Get help
Command:
```python
biobb_pdb_mkensemble -h
```
    usage: biobb_pdb_mkensemble [-h] --config CONFIG --input_file_path1 INPUT_FILE_PATH1 --input_file_path2 INPUT_FILE_PATH2 --output_file_path OUTPUT_FILE_PATH
    
    Merges several PDB files into one multi-model (ensemble) file.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --input_file_path2 INPUT_FILE_PATH2
                            Description for the second input file path (optional). Accepted formats: pdb.
    
    required arguments:
      --input_file_path1 INPUT_FILE_PATH1
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path1** (*string*): PDB file of selected protein. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_mkensemble1.pdb). Accepted formats: PDB
* **input_file_path2** (*string*): PDB file for another selected protein. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_mkensemble2.pdb). Accepted formats: PDB
* **output_file_path** (*string*): Multi-model (ensemble) PDB file with input PDBs merged. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_mkensemble.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_mkensemble) Strips all HEADER information and adds REMARK statements with the provenance of each conformer..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_merge
Merges several PDB files into one.
### Get help
Command:
```python
biobb_pdb_merge -h
```
    usage: biobb_pdb_merge [-h] --config CONFIG --input_file_path1 INPUT_FILE_PATH1 --input_file_path2 INPUT_FILE_PATH2 --output_file_path OUTPUT_FILE_PATH
    
    Merges several PDB files into one.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --input_file_path2 INPUT_FILE_PATH2
                            Description for the second input file path (optional). Accepted formats: pdb.
    
    required arguments:
      --input_file_path1 INPUT_FILE_PATH1
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path1** (*string*): PDB file of selected protein. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_merge1.pdb). Accepted formats: PDB
* **input_file_path2** (*string*): PDB file for another selected protein. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_merge2.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with input PDBs merged. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_merge.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_merge) Example of executable binary property..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_reres
Renumbers the residues of the PDB file starting from a given number (default 1).
### Get help
Command:
```python
biobb_pdb_reres -h
```
    usage: biobb_pdb_reres [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Renumbers the residues of the PDB file starting from a given number (default 1).
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_reres.pdb). Accepted formats: PDB
* **output_file_path** (*string*): Renumbered PDB file by number of redisue selected. File type: output. [Sample file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_reres.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **number** (*string*): (4) Number of the protein residue..
* **binary_path** (*string*): (reres) Renumbers the residues of the PDB file starting from a given number (default 1)..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_splitseg
Splits a PDB file into several, each containing one segment.
### Get help
Command:
```python
biobb_pdb_splitseg -h
```
    usage: biobb_pdb_splitseg [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Splits a PDB file into several, each containing one segment.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_splitseg.pdb). Accepted formats: PDB
* **output_file_path** (*string*): ZIP file containing all PDB files splited by protein segment. File type: output. [Sample file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_splitseg.zip). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_splitseg) Splits a PDB file into several, each containing one segment..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_splitmodel
Splits a PDB file into several, each containing one MODEL.
### Get help
Command:
```python
biobb_pdb_splitmodel -h
```
    usage: biobb_pdb_splitmodel [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Splits a PDB file into several, each containing one MODEL.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_splitmodel.pdb). Accepted formats: PDB
* **output_file_path** (*string*): ZIP file containing all PDB files splited by protein model. File type: output. [Sample file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_splitmodel.zip). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_splitmodel) Splits a PDB file into several, each containing one MODEL..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_chainxseg
Swaps the segment identifier for the chain identifier.
### Get help
Command:
```python
biobb_pdb_chainxseg -h
```
    usage: biobb_pdb_chainxseg [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Swaps the segment identifier for the chain identifier.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_chainxseg.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with exchanged segment and string identifier. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_chainxseg.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_chainxseg) Swaps the segment identifier for the chain identifier..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON
