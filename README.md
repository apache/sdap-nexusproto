# nexus-messages

This project contains the [protobuf](https://developers.google.com/protocol-buffers/) definition for a NexusTile. By compiling the protobuf specification, both Java and Python objects are generated.

# For Developers

## Prerequisites

This project is build using Gradle. This repository contains a Gradle wrapper so, if building from the repository, no further action is needed; however, the Gradle wrapper is not included in the source distribution. If building from the source distribution, you will need to [install Gradle manually](https://gradle.org/releases/).

## Developer Installation

1. Build source:

    - If building from repository: run `./gradlew clean build install`
    - If building from source distribution: run `gradle clean build install`

2. cd into `/build/python/nexusproto`

3. Setup a separate conda env or activate an existing one

    ````
    conda create --name nexus-messages python
    source activate nexus-messages
    ````

4. Install Conda dependencies

    ````
    conda install numpy
    ````

5. Run `python setup.py install`
