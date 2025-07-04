import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_pdb_tools",
    version="5.1.0",
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
    install_requires=["biobb_common==5.1.0"],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "biobb_pdb_chain = biobb_pdb_tools.pdb_tools.biobb_pdb_chain:main",
            "biobb_pdb_chainxseg = biobb_pdb_tools.pdb_tools.biobb_pdb_chainxseg:main",
            "biobb_pdb_delhetatm = biobb_pdb_tools.pdb_tools.biobb_pdb_delhetatm:main",
            "biobb_pdb_fetch = biobb_pdb_tools.pdb_tools.biobb_pdb_fetch:main",
            "biobb_pdb_fixinsert = biobb_pdb_tools.pdb_tools.biobb_pdb_fixinsert:main",
            "biobb_pdb_keepcord = biobb_pdb_tools.pdb_tools.biobb_pdb_keepcord:main",
            "biobb_pdb_merge = biobb_pdb_tools.pdb_tools.biobb_pdb_merge:main",
            "biobb_pdb_mkensemble = biobb_pdb_tools.pdb_tools.biobb_pdb_mkensemble:main",
            "biobb_pdb_reres = biobb_pdb_tools.pdb_tools.biobb_pdb_reres:main",
            "biobb_pdb_seg = biobb_pdb_tools.pdb_tools.biobb_pdb_seg:main",
            "biobb_pdb_selaltloc = biobb_pdb_tools.pdb_tools.biobb_pdb_selaltloc:main",
            "biobb_pdb_selchain = biobb_pdb_tools.pdb_tools.biobb_pdb_selchain:main",
            "biobb_pdb_selres = biobb_pdb_tools.pdb_tools.biobb_pdb_selres:main",
            "biobb_pdb_splitmodel = biobb_pdb_tools.pdb_tools.biobb_pdb_splitmodel:main",
            "biobb_pdb_splitseg = biobb_pdb_tools.pdb_tools.biobb_pdb_splitseg:main",
            "biobb_pdb_tidy = biobb_pdb_tools.pdb_tools.biobb_pdb_tidy:main",
            "biobb_pdb_tofasta = biobb_pdb_tools.pdb_tools.biobb_pdb_tofasta:main",
            "biobb_pdb_uniqname = biobb_pdb_tools.pdb_tools.biobb_pdb_uniqname:main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
)
