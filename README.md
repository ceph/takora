Takora
======

Puppet modules for deploying a Ceph cluster

How to add a new Puppet module
------------------------------

First you have to install [bade](https://github.com/paramite/bade), a utility
for managing Puppet modules using GIT subtrees.

    git clone https://github.com/paramite/bade
    cd bade
    python setup.py develop

Then create a [fork of the Takora repository](https://help.github.com/articles/fork-a-repo/)
and [create a local clone of it](https://help.github.com/articles/fork-a-repo/#step-2-create-a-local-clone-of-your-fork).

    git clone git@github.com:YOUR_USERNAME/takora.git
    cd takora

Now create a new [branch](http://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) in your local clone.

    git checkout -b NAME_OF_THE_MODULE

Afterwards add the new Puppet module, `puppetlabs-ntp` in this example.

    bade add --upstream https://github.com/puppetlabs/puppetlabs-ntp.git --hash 060c453a9bbd87d1bf229db70ee6367033a2910e --commit

Finally add some more details (e.g. why you want to add this Puppet module)
to the commit message, push the branch and [initiate a pull request](https://help.github.com/articles/using-pull-requests/#initiating-the-pull-request).

    git commit --amend
    git push --set-upstream origin ntp

Packaging
=========

To create a debian package, run `dpkg-buildpackage -us -uc`. You will find the
packages in the parent directory of your current working directory.
