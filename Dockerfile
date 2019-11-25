FROM continuumio/miniconda3

RUN apt-get update && \
    apt-get install -y openbabel g++ make && \
    conda install -c openbabel python=3.7 openbabel==2.4.1

# NAMS stuff
COPY nams /var/nams
WORKDIR /var/nams
RUN make
RUN cp nams /usr/local/bin/. 

#makenamsdb part
COPY makenamsdb /usr/local/bin/makenamsdb
ENV PATH="/usr/local/bin/makenamsdb:${PATH}"

COPY work /var/work
WORKDIR /var/work

CMD "/bin/bash"
