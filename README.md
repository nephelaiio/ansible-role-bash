# nephelaiio.bash

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-bash.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-bash)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.bash-blue.svg)](https://galaxy.ansible.com/nephelaiio/bash/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/bash) to install and configure bash

## Local install

Execute the following from the command line shell

```
curl -s https://raw.githubusercontent.com/nephelaiio/ansible-role-docker/master/install.sh | bash
```


## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook

- hosts: localhost
  roles:
     - role: nephelaiio.bash


## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Focal
  * Ubuntu Bionic
  * Debian Stretch

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
