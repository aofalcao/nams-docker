This is a Docker installation for NAMS and the NAMS utils

It can be installed easily with Docker

`docker build -t mimed101 .`

and then to run it

`docker run -it mimed101`

NAMS will be installed by default

Within the installation, a default work directory is present with a SMILES file (simple.smi)

to make a .nams file one can run

`makenamsdb simple.smi simple.nams`

which will create a .nams file that can be used by NAMS. 

to run NAMS directly and compute a similarity matrix between all molecules of this file:

`nams -mode 2 -db simple.nams`

