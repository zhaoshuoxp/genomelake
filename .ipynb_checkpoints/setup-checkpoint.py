from setuptools import setup, find_packages

setup(
    name="genomelake",
    version="0.2.0",
    description="Genomic data access from .hdf5 or .bigwig",
    author="Avanti Shrikumar, Kundaje lab; Quanyi Zhao, Thomas Quertermous lab",
    author_email="avanti@stanford.edu",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.0",
        "h5py",
        "scikit-learn",
        "pyfaidx",
        "pyBigWig",
        "zarr"
    ],
    python_requires=">=3.10",
)

