# BioBB PDB Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Biobb_pdb_chain
Modifies the chain identifier column of a PDB file.
### Get help
Command:
```python
biobb_pdb_chain -h
```
    usage: biobb_pdb_chain [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Modifies the chain identifier column of a PDB file.
    
    options:
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
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with selected modified chain. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_chain.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **chain** (*string*): (A) Modifies the chain identifier column of a PDB file..
* **binary_path** (*string*): (pdb_chain) Path to the pdb_chain executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_chain.yml)
```python
properties:
  chain: A

```
#### Command line
```python
biobb_pdb_chain --config config_biobb_pdb_chain.yml --input_file_path 1AKI.pdb --output_file_path ref_pdb_chain.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_chain.json)
```python
{
  "properties": {
    "chain": "A"
  }
}
```
#### Command line
```python
biobb_pdb_chain --config config_biobb_pdb_chain.json --input_file_path 1AKI.pdb --output_file_path ref_pdb_chain.pdb
```

## Biobb_pdb_chainxseg
Swaps the segment identifier for the chain identifier.
### Get help
Command:
```python
biobb_pdb_chainxseg -h
```
    usage: biobb_pdb_chainxseg [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Swaps the segment identifier for the chain identifier.
    
    options:
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
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with exchanged segment and string identifier. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_chainxseg.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_chainxseg) Path to the pdb_chainxseg executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_chainxseg.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
biobb_pdb_chainxseg --config config_biobb_pdb_chainxseg.yml --input_file_path 1AKI.pdb --output_file_path ref_pdb_chainxseg.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_chainxseg.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
biobb_pdb_chainxseg --config config_biobb_pdb_chainxseg.json --input_file_path 1AKI.pdb --output_file_path ref_pdb_chainxseg.pdb
```

## Biobb_pdb_delhetatm
Removes all HETATM records in the PDB file.
### Get help
Command:
```python
biobb_pdb_delhetatm -h
```
    usage: biobb_pdb_delhetatm [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Removes all HETATM records in the PDB file.
    
    options:
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
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with all HETATM records removed. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_delhetatm.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_delhetatm) Path to the pdb_delhetatm executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_delhetatm.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
biobb_pdb_delhetatm --config config_biobb_pdb_delhetatm.yml --input_file_path 1AKI.pdb --output_file_path ref_pdb_delhetatm.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_delhetatm.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
biobb_pdb_delhetatm --config config_biobb_pdb_delhetatm.json --input_file_path 1AKI.pdb --output_file_path ref_pdb_delhetatm.pdb
```

## Biobb_pdb_fetch
Downloads a structure in PDB format from the RCSB website.
### Get help
Command:
```python
biobb_pdb_fetch -h
```
    usage: biobb_pdb_fetch [-h] --config CONFIG --output_file_path OUTPUT_FILE_PATH
    
    Downloads a structure in PDB format from the RCSB website.
    
    options:
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
* **binary_path** (*string*): (pdb_fetch) Path to the pdb_fetch executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_fetch.yml)
```python
properties:
  biounit: false
  pdbid: 1nmr

```
#### Command line
```python
biobb_pdb_fetch --config config_biobb_pdb_fetch.yml --output_file_path ref_pdb_fetch.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_fetch.json)
```python
{
  "properties": {
    "pdbid": "1nmr",
    "biounit": false
  }
}
```
#### Command line
```python
biobb_pdb_fetch --config config_biobb_pdb_fetch.json --output_file_path ref_pdb_fetch.pdb
```

## Biobb_pdb_fixinsert
Deletes insertion codes and shifts the residue numbering of downstream residues.
### Get help
Command:
```python
biobb_pdb_fixinsert -h
```
    usage: biobb_pdb_fixinsert [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Deletes insertion codes and shifts the residue numbering of downstream residues.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            PDB file. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            PDB file with fixed insertion codes. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1IGY.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with fixed insertion codes. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_fixinsert.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **residues** (*string*): (None) Specific residues to delete insertion codes for, format: "A9,B12" (chain and residue number)..
* **binary_path** (*string*): (pdb_fixinsert) Path to the pdb_fixinsert executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_fixinsert.yml)
```python
properties:
  residues: B82

```
#### Command line
```python
biobb_pdb_fixinsert --config config_biobb_pdb_fixinsert.yml --input_file_path 1IGY.pdb --output_file_path ref_pdb_fixinsert.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_fixinsert.json)
```python
{
  "properties": {
    "residues": "B82"
  }
}
```
#### Command line
```python
biobb_pdb_fixinsert --config config_biobb_pdb_fixinsert.json --input_file_path 1IGY.pdb --output_file_path ref_pdb_fixinsert.pdb
```

## Biobb_pdb_keepcoord
Removes all non-coordinate records from the file.
### Get help
Command:
```python
biobb_pdb_keepcoord -h
```
    /bin/sh: 1: biobb_pdb_keepcoord: not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with only coordinate records. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_keepcoord.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_keepcoord) Path to the pdb_keepcoord executable binary..
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
    usage: biobb_pdb_merge [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Merges several PDB files into one.
    
    options:
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
* **input_file_path** (*string*): ZIP file of selected protein. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_merge.pdb). Accepted formats: ZIP
* **output_file_path** (*string*): PDB file with input PDBs merged. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_merge.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_merge) Path to the pdb_merge executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_merge.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
biobb_pdb_merge --config config_biobb_pdb_merge.yml --input_file_path input_pdb_merge.pdb --output_file_path ref_pdb_merge.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_merge.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
biobb_pdb_merge --config config_biobb_pdb_merge.json --input_file_path input_pdb_merge.pdb --output_file_path ref_pdb_merge.pdb
```

## Biobb_pdb_mkensemble
Merges several PDB files into one multi-model (ensemble) file.
### Get help
Command:
```python
biobb_pdb_mkensemble -h
```
    usage: biobb_pdb_mkensemble [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Merges several PDB files into one multi-model (ensemble) file.
    
    options:
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
* **input_file_path** (*string*): ZIP file of selected proteins. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_mkensemble.pdb). Accepted formats: ZIP
* **output_file_path** (*string*): Multi-model (ensemble) PDB file with input PDBs merged. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_mkensemble.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_mkensemble) Path to the pdb_mkensemble executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_mkensemble.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
biobb_pdb_mkensemble --config config_biobb_pdb_mkensemble.yml --input_file_path input_pdb_mkensemble.pdb --output_file_path ref_pdb_mkensemble.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_mkensemble.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
biobb_pdb_mkensemble --config config_biobb_pdb_mkensemble.json --input_file_path input_pdb_mkensemble.pdb --output_file_path ref_pdb_mkensemble.pdb
```

## Biobb_pdb_reres
Renumbers the residues of the PDB file starting from a given number (default 1).
### Get help
Command:
```python
biobb_pdb_reres -h
```
    usage: biobb_pdb_reres [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Renumbers the residues of the PDB file starting from a given number (default 1).
    
    options:
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
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb). Accepted formats: PDB
* **output_file_path** (*string*): Renumbered PDB file by number of redisue selected. File type: output. [Sample file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_reres.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **number** (*integer*): (4) Number of the protein residue..
* **binary_path** (*string*): (pdb_reres) Path to the pdb_reres executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_reres.yml)
```python
properties:
  number: 4

```
#### Command line
```python
biobb_pdb_reres --config config_biobb_pdb_reres.yml --input_file_path 1AKI.pdb --output_file_path ref_pdb_reres.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_reres.json)
```python
{
  "properties": {
    "number": 4
  }
}
```
#### Command line
```python
biobb_pdb_reres --config config_biobb_pdb_reres.json --input_file_path 1AKI.pdb --output_file_path ref_pdb_reres.pdb
```

## Biobb_pdb_seg
Modifies the segment identifier column of a PDB file.
### Get help
Command:
```python
biobb_pdb_seg -h
```
    usage: biobb_pdb_seg [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Modifies the segment identifier column of a PDB file.
    
    options:
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
* **binary_path** (*string*): (pdb_seg) Path to the pdb_seg executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_seg.yml)
```python
properties:
  segment: B

```
#### Command line
```python
biobb_pdb_seg --config config_biobb_pdb_seg.yml --input_file_path input_pdb_seg.pdb --output_file_path ref_pdb_seg.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_seg.json)
```python
{
  "properties": {
    "segment": "B"
  }
}
```
#### Command line
```python
biobb_pdb_seg --config config_biobb_pdb_seg.json --input_file_path input_pdb_seg.pdb --output_file_path ref_pdb_seg.pdb
```

## Biobb_pdb_selaltloc
Selects alternative locations from a PDB file.
### Get help
Command:
```python
biobb_pdb_selaltloc -h
```
    usage: biobb_pdb_selaltloc [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Selects alternative locations from a PDB file.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            PDB file. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            PDB file with selected alternative locations. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/9INS.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with selected alternative locations. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_selaltloc.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **altloc** (*string*): (None) Specific alternative location label to select (e.g. "A")..
* **binary_path** (*string*): (pdb_selaltloc) Path to the pdb_selaltloc executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Biobb_pdb_selchain
Extracts one or more chains from a PDB file.
### Get help
Command:
```python
biobb_pdb_selchain -h
```
    usage: biobb_pdb_selchain [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Extracts one or more chains from a PDB file.
    
    options:
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
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_selchain.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with selected chains. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_selchain.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **chains** (*string*): (A) Chain or list of chains (comma separated) to extract from the PDB file..
* **binary_path** (*string*): (pdb_selchain) Path to the pdb_selchain executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_selchain.yml)
```python
properties:
  chains: B

```
#### Command line
```python
biobb_pdb_selchain --config config_biobb_pdb_selchain.yml --input_file_path input_pdb_selchain.pdb --output_file_path ref_pdb_selchain.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_selchain.json)
```python
{
  "properties": {
    "chains": "B"
  }
}
```
#### Command line
```python
biobb_pdb_selchain --config config_biobb_pdb_selchain.json --input_file_path input_pdb_selchain.pdb --output_file_path ref_pdb_selchain.pdb
```

## Biobb_pdb_selres
Selects residues by their index, piecewise or in a range.
### Get help
Command:
```python
biobb_pdb_selres -h
```
    usage: biobb_pdb_selres [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Selects residues by their index, piecewise or in a range.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            PDB file. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            PDB file with selected residues. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1IGY.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with selected residues. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_selres.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **selection** (*string*): (None) Residue selection format: individual residues "1,2,4,6", range "1:10", multiple ranges "1:10,20:30", open ranges "1:", ":5", or intervals "::5", "1:10:5"..
* **binary_path** (*string*): (pdb_selres) Path to the pdb_selres executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_selres.yml)
```python
properties:
  selection: '1:10:2'

```
#### Command line
```python
biobb_pdb_selres --config config_biobb_pdb_selres.yml --input_file_path 1IGY.pdb --output_file_path ref_pdb_selres.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_selres.json)
```python
{
  "properties": {
    "selection": "1:10:2"
  }
}
```
#### Command line
```python
biobb_pdb_selres --config config_biobb_pdb_selres.json --input_file_path 1IGY.pdb --output_file_path ref_pdb_selres.pdb
```

## Biobb_pdb_splitmodel
Splits a PDB file into several, each containing one MODEL.
### Get help
Command:
```python
biobb_pdb_splitmodel -h
```
    usage: biobb_pdb_splitmodel [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Splits a PDB file into several, each containing one MODEL.
    
    options:
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
* **binary_path** (*string*): (pdb_splitmodel) Path to the pdb_splitmodel executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_splitmodel.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
biobb_pdb_splitmodel --config config_biobb_pdb_splitmodel.yml --input_file_path input_pdb_splitmodel.pdb --output_file_path ref_pdb_splitmodel.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_splitmodel.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
biobb_pdb_splitmodel --config config_biobb_pdb_splitmodel.json --input_file_path input_pdb_splitmodel.pdb --output_file_path ref_pdb_splitmodel.zip
```

## Biobb_pdb_splitseg
Splits a PDB file into several, each containing one segment.
### Get help
Command:
```python
biobb_pdb_splitseg -h
```
    usage: biobb_pdb_splitseg [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Splits a PDB file into several, each containing one segment.
    
    options:
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
* **binary_path** (*string*): (pdb_splitseg) Path to the pdb_splitseg executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_splitseg.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
biobb_pdb_splitseg --config config_biobb_pdb_splitseg.yml --input_file_path input_pdb_splitseg.pdb --output_file_path ref_pdb_splitseg.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_splitseg.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
biobb_pdb_splitseg --config config_biobb_pdb_splitseg.json --input_file_path input_pdb_splitseg.pdb --output_file_path ref_pdb_splitseg.zip
```

## Biobb_pdb_tidy
Modifies the file to adhere (as much as possible) to the format specifications.
### Get help
Command:
```python
biobb_pdb_tidy -h
```
    usage: biobb_pdb_tidy [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Modifies the file to adhere (as much as possible) to the format specifications.
    
    options:
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
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file modified according to the specifications. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_tidy.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **strict** (*boolean*): (False) Does not add TER on chain breaks..
* **binary_path** (*string*): (pdb_tidy) Path to the pdb_tidy executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_tidy.yml)
```python
properties:
  strict: false

```
#### Command line
```python
biobb_pdb_tidy --config config_biobb_pdb_tidy.yml --input_file_path 1AKI.pdb --output_file_path ref_pdb_tidy.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_tidy.json)
```python
{
  "properties": {
    "strict": false
  }
}
```
#### Command line
```python
biobb_pdb_tidy --config config_biobb_pdb_tidy.json --input_file_path 1AKI.pdb --output_file_path ref_pdb_tidy.pdb
```

## Biobb_pdb_tofasta
Extracts the residue sequence in a PDB file to FASTA format.
### Get help
Command:
```python
biobb_pdb_tofasta -h
```
    usage: biobb_pdb_tofasta [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Extracts the residue sequence in a PDB file to FASTA format.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path INPUT_FILE_PATH
                            Description for the first input file path. Accepted formats: pdb.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the output file path. Accepted formats: fasta.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb). Accepted formats: PDB
* **output_file_path** (*string*): FASTA file containing the aminoacids sequence. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_tofasta.pdb). Accepted formats: FASTA, FA
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **multi** (*boolean*): (True) Splits the different chains into different records in the FASTA file..
* **binary_path** (*string*): (pdb_tofasta) Path to the pdb_tofasta executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_tofasta.yml)
```python
properties:
  multi: true

```
#### Command line
```python
biobb_pdb_tofasta --config config_biobb_pdb_tofasta.yml --input_file_path 1AKI.pdb --output_file_path ref_pdb_tofasta.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_tofasta.json)
```python
{
  "properties": {
    "multi": true
  }
}
```
#### Command line
```python
biobb_pdb_tofasta --config config_biobb_pdb_tofasta.json --input_file_path 1AKI.pdb --output_file_path ref_pdb_tofasta.pdb
```

## Biobb_pdb_uniqname
Renames atoms sequentially (C1, C2, O1, ...) for each HETATM residue.
### Get help
Command:
```python
biobb_pdb_uniqname -h
```
    usage: biobb_pdb_uniqname [-h] --config CONFIG --input_file_path INPUT_FILE_PATH --output_file_path OUTPUT_FILE_PATH
    
    Removes all HETATM records in the PDB file.
    
    options:
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
* **input_file_path** (*string*): PDB file. File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb). Accepted formats: PDB
* **output_file_path** (*string*): PDB file with all HETATM atoms renamed. File type: output. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_delhetatm.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (pdb_uniqname) Path to the pdb_uniqname executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_uniqname.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
biobb_pdb_uniqname --config config_biobb_pdb_uniqname.yml --input_file_path 1AKI.pdb --output_file_path ref_pdb_delhetatm.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_pdb_tools/blob/master/biobb_pdb_tools/test/data/config/config_biobb_pdb_uniqname.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
biobb_pdb_uniqname --config config_biobb_pdb_uniqname.json --input_file_path 1AKI.pdb --output_file_path ref_pdb_delhetatm.pdb
```
