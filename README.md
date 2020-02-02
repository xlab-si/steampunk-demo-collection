# Demo Ansible collection for testing CircleCI integration

This repository contains a minimalistic Ansible collection. Its main purpose
is to test the integration with CircleCI.


## Quickstart

This collection is, for obvious reasons, **not** available from Ansible
Galaxy, which means that we need to clone it to our workstation:

    $ mkdir -p ~/my_collections/ansible_collections/steampunk
    $ cd ~/my_collections/ansible_collections/steampunk
    $ git clone https://github.com/xlab-si/steampunk-demo-collection.git demo
    $ cd demo

To actually use this collection from Ansible, we need to add the
*~/my_collections* directory to Ansible's collection search path by running:

    $ export ANSIBLE_COLLECTIONS_PATHS=~/my_collections

Now we are ready to use the collection in a playbooks like this:

    ---
    - name: Demo playbook
      hosts: all

      tasks:
        - name: Place a marker file
          steampunk.demo.marker:
            path: /tmp/my-marker
            content: >
              THIS IS MY LOUD MARKER

And that is basically it.


## Running integration tests

Now, we need to create a virtual environment and install molecule in it:

    $ cd ~/my_collections/ansible_collections/steampunk/demo
    $ python3 -m venv venv
    $ . venv/bin/activate
    (venv) $ pip install -r integration.requirements

Once the dependencies are installed, we can run the integration tests:

    (venv) $ export ANSIBLE_COLLECTIONS_PATHS=$PWD/../../..
    (venv) $ cd tests/integration
    (venv) $ molecule -c base.yml test --all

Note that you do need to have *docker* installed and running in order to be
able to run the integration tests.
