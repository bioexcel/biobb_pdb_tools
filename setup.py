import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_pdb_tools",
    version="5.4.0",
    author="Biobb developers",
    author_email="agustin.garcia@irbbarcelona.org",
    description="Biobb_pdb_tools is a swiss army knife for manipulating and editing PDB files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_pdb_tools",
    project_urls={
        "Documentation": "http://biobb-pdb-tools.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/",
    },
    packages=setuptools.find_packages(exclude=["docs", "test"]),
    package_data={"biobb_pdb_tools": ["py.typed"]},
    install_requires=["biobb_common==5.4.0", "pdb-tools"],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "biobb_pdb_chain = biobb_pdb_tools.pdb_tools.biobb_pdb_chain:Pdbchain.main",
            "biobb_pdb_chainxseg = biobb_pdb_tools.pdb_tools.biobb_pdb_chainxseg:Chainxseg.main",
            "biobb_pdb_delhetatm = biobb_pdb_tools.pdb_tools.biobb_pdb_delhetatm:Delhetatm.main",
            "biobb_pdb_fetch = biobb_pdb_tools.pdb_tools.biobb_pdb_fetch:Pdbfetch.main",
            "biobb_pdb_fixinsert = biobb_pdb_tools.pdb_tools.biobb_pdb_fixinsert:Pdbfixinsert.main",
            "biobb_pdb_keepcoord = biobb_pdb_tools.pdb_tools.biobb_pdb_keepcoord:Pdbkeepcoord.main",
            "biobb_pdb_merge = biobb_pdb_tools.pdb_tools.biobb_pdb_merge:Pdbmerge.main",
            "biobb_pdb_mkensemble = biobb_pdb_tools.pdb_tools.biobb_pdb_mkensemble:Mkensemble.main",
            "biobb_pdb_reres = biobb_pdb_tools.pdb_tools.biobb_pdb_reres:Pdbreres.main",
            "biobb_pdb_seg = biobb_pdb_tools.pdb_tools.biobb_pdb_seg:Pdbseg.main",
            "biobb_pdb_selaltloc = biobb_pdb_tools.pdb_tools.biobb_pdb_selaltloc:Pdbselaltloc.main",
            "biobb_pdb_selchain = biobb_pdb_tools.pdb_tools.biobb_pdb_selchain:Pdbselchain.main",
            "biobb_pdb_selmodel = biobb_pdb_tools.pdb_tools.biobb_pdb_selmodel:Pdbselmodel.main",
            "biobb_pdb_selres = biobb_pdb_tools.pdb_tools.biobb_pdb_selres:Pdbselres.main",
            "biobb_pdb_splitmodel = biobb_pdb_tools.pdb_tools.biobb_pdb_splitmodel:Pdbsplitmodel.main",
            "biobb_pdb_splitseg = biobb_pdb_tools.pdb_tools.biobb_pdb_splitseg:Pdbsplitseg.main",
            "biobb_pdb_tidy = biobb_pdb_tools.pdb_tools.biobb_pdb_tidy:Pdbtidy.main",
            "biobb_pdb_tofasta = biobb_pdb_tools.pdb_tools.biobb_pdb_tofasta:Pdbtofasta.main",
            "biobb_pdb_uniqname = biobb_pdb_tools.pdb_tools.biobb_pdb_uniqname:Pdbuniqname.main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
)
