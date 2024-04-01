# Border0 AWX EE
This is a clone of the official AWX EE image with some modifications to enhance it with Border0

Upstream branches will be kept as they are and used as a base for our own branches.

## Changes
First of all we remove all the redhar fluff, and pretty much anything that's not required to build the image.

We add following changes to the EE image:
- Adding the `border0` cli tools to the image https://www.border0.com/download
- Adding ssh configuration to the image to allow for integraion with border0 tools

## AWX EE

The default Execution Environment for AWX.

### Build the image locally

First, [install ansible-builder](https://ansible-builder.readthedocs.io/en/stable/installation/).

Then run the following command from the root of this repo:

```bash
$ ansible-builder build -v3 -t quay.io/ansible/awx-ee # --container-runtime=docker # Is podman by default
```
