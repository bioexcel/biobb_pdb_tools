# biobb_pdb_tools

## Introduction
biobb_pdb_tools is TODO
The latest documentation of this package can be found in our readthedocs site:
[latest API documentation](http://biobb-pdb-tools.readthedocs.io/en/latest/).

### Version
v4.1.0 2023.4

### Installation
Using PIP:

> **Important:** PIP only installs the package. All the dependencies must be installed separately. To perform a complete installation, please use ANACONDA, DOCKER or SINGULARITY.

* Installation:


        pip install "biobb_pdb_tools>=4.1.0"


* Usage: [Python API documentation](https://biobb-pdb-tools.readthedocs.io/en/latest/modules.html)

Using ANACONDA:

* Installation:


        conda install -c bioconda "biobb_pdb_tools>=4.1.0"


* Usage: With conda installation BioBBs can be used with the [Python API documentation](https://biobb-pdb-tools.readthedocs.io/en/latest/modules.html) and the [Command Line documentation](https://biobb-pdb-tools.readthedocs.io/en/latest/command_line.html)

Using DOCKER:

* Installation:


        docker pull quay.io/biocontainers/biobb_pdb_tools:4.1.0--pyhdfd78af_0


* Usage:


        docker run quay.io/biocontainers/biobb_pdb_tools:4.1.0--pyhdfd78af_0 <command>

Using SINGULARITY:

**MacOS users**: it's strongly recommended to avoid Singularity and use **Docker** as containerization system.

* Installation:


        singularity pull --name biobb_pdb_tools.sif https://depot.galaxyproject.org/singularity/biobb_pdb_tools:4.1.0--pyhdfd78af_0


* Usage:


        singularity exec biobb_pdb_tools.sif <command>

The command list and specification can be found at the [Command Line documentation](https://biobb-pdb-tools.readthedocs.io/en/latest/command_line.html).

### Copyright & Licensing
This software has been developed in the [MMB group](http://mmb.irbbarcelona.org) at the [BSC](http://www.bsc.es/) & [IRB](https://www.irbbarcelona.org/) for the [European BioExcel](http://bioexcel.eu/), funded by the European Commission (EU H2020 [823830](http://cordis.europa.eu/projects/823830), EU H2020 [675728](http://cordis.europa.eu/projects/675728)).

* (c) 2015-2023 [Barcelona Supercomputing Center](https://www.bsc.es/)
* (c) 2015-2023 [Institute for Research in Biomedicine](https://www.irbbarcelona.org/)

Licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), see the file LICENSE for details.

![](https://bioexcel.eu/wp-content/uploads/2019/04/Bioexcell_logo_1080px_transp.png "Bioexcel")