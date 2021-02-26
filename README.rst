**********************
Molecule Inspec Plugin
**********************

.. image:: https://badge.fury.io/py/molecule-inspec.svg
   :target: https://badge.fury.io/py/molecule-inspec
   :alt: PyPI Package

.. image:: https://github.com/ansible-community/molecule-inspec/workflows/tox/badge.svg
   :target: https://github.com/ansible-community/molecule-inspec/actions

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/python/black
   :alt: Python Black Code Style

.. image:: https://img.shields.io/badge/Code%20of%20Conduct-Ansible-silver.svg
   :target: https://docs.ansible.com/ansible/latest/community/code_of_conduct.html
   :alt: Ansible Code of Conduct

.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: LICENSE
   :alt: Repository License

Molecule Inspec Plugin is designed to allow use of inspec as a verifier.
The initialization of a role or scenario with the inspec verifier configures a
Verify playbook which installs inspec, copies the tests, and executes inspec on
the instance.

Documentation
=============

.. _installation-and-usage:

Installation and Usage
======================

Install molecule-inspec and pre-requisites:

.. code-block::

   pip install molecule molecule-inspec

Create a new role with molecule using the inspec verifier:

.. code-block::

   molecule init role <role_name> --verifier-name inspec

Configure ``<role_name>/molecule/default/tests/`` with the desired inspec
tests. A simple default test is provided:

.. code-block::

   # frozen_string_literal: true

   # Molecule managed

   describe file('/etc/hosts') do
   its('owner') { should eq 'root' }
   its('group') { should eq 'root' }
   its('mode') { should cmp '0644' }
   end

Execute `test` or `verify` on the role or scenario to run the Verify playbook

.. code-block::

   /inspec-role/molecule/default/molecule.yml.
   INFO     default scenario test matrix: verify
   INFO     Running default > verify
   INFO     Executing Inspec tests found in
   /inspec-role/molecule/default/tests/...
   INFO     Sanity checks: 'docker'

   PLAY [Verify] ******************************************************************

   TASK [Gathering Facts] *********************************************************
   ok: [instance]

   TASK [Setting variables (CentOS 7 / RHEL 7 / Amazon Linux 2)] ******************
   ok: [instance]

   TASK [Download Inspec] *********************************************************
   changed: [instance]

   TASK [Install Inspec (yum)] ****************************************************
   changed: [instance]

   TASK [Create inspec test directory] ********************************************
   changed: [instance]

   TASK [Copy inspec test directories] ********************************************
   skipping: [instance] => (item={'root':
   '/inspec-role/molecule/default/tests/', 'path': 'test_default.rb', 'state': 'file',
   'src': '/inspec-role/molecule/default/tests/test_default.rb', 'uid': 501, 'gid': 20,
   'owner': 'abtreece', 'group': 'staff', 'mode': '0644', 'size': 194,
   'mtime': 1609387140.054121, 'ctime': 1609387140.054233})

   TASK [Copy inspec test files] **************************************************
   changed: [instance] => (item={'root':
   '/inspec-role/molecule/default/tests/', 'path': 'test_default.rb', 'state': 'file',
   'src': '/inspec-role/molecule/default/tests/test_default.rb', 'uid': 501, 'gid': 20,
   'owner': 'abtreece', 'group': 'staff', 'mode': '0644', 'size': 194,
   'mtime': 1609387140.054121, 'ctime': 1609387140.054233})

   TASK [Execute Inspec tests] ****************************************************
   changed: [instance]

   TASK [Display details about the Inspec results] ********************************
   ok: [instance] => {
      "msg": [
         "",
         "Profile: tests from /tmp/molecule/inspec (tests from .tmp.molecule.inspec)",
         "Version: (not specified)",
         "Target:  local://",
         "",
         "  File /etc/hosts",
         "\u001b[38;5;41m     ✔  owner should eq \"root\"\u001b[0m",
         "\u001b[38;5;41m     ✔  group should eq \"root\"\u001b[0m",
         "\u001b[38;5;41m     ✔  mode should cmp == \"0644\"\u001b[0m",
         "",
         "Test Summary: \u001b[38;5;41m3 successful\u001b[0m, 0 failures, 0 skipped"
      ]
   }

   TASK [Fail when tests fail] ****************************************************
   skipping: [instance]

   PLAY RECAP *********************************************************************
   instance: ok=8    changed=5    unreachable=0    failed=0    skipped=7    rescued=0
   ignored=0

   INFO     Verifier completed successfully.

.. _get-involved:

Get Involved
============

* Join us in the ``#ansible-molecule`` channel on `Freenode`_.
* Join the discussion in `molecule-users Forum`_.
* Join the community working group by checking the `wiki`_.
* Want to know about releases, subscribe to `ansible-announce list`_.
* For the full list of Ansible email Lists, IRC channels see the
  `communication page`_.

.. _`Freenode`: https://freenode.net
.. _`molecule-users Forum`: https://groups.google.com/forum/#!forum/molecule-users
.. _`wiki`: https://github.com/ansible/community/wiki/Molecule
.. _`ansible-announce list`: https://groups.google.com/group/ansible-announce
.. _`communication page`: https://docs.ansible.com/ansible/latest/community/communication.html

.. _authors:

Authors
=======

Molecule Inspec Plugin was created by Sorin Sbarnea based on code from Molecule.

.. _license:

License
=======

The `MIT`_ License.

.. _`MIT`: https://github.com/ansible/molecule/blob/master/LICENSE

The logo is licensed under the `Creative Commons NoDerivatives 4.0 License`_.

If you have some other use in mind, contact us.

.. _`Creative Commons NoDerivatives 4.0 License`: https://creativecommons.org/licenses/by-nd/4.0/
