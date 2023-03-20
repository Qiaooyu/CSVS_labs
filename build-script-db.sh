#!/bin/bash

# First build database images from Dockerfiles
docker build --tag database -f Dockerfile .

# Second run script to reduce the size of the database image

/path/strip-cmd.sh

