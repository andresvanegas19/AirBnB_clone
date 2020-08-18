#!/usr/bin/python3
""" Automate the service on the server """
from datetime import datetime
from fabric.api import (local, hide, settings)



def do_pack():
    """ generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone
    repo, using the function do_pack """
    # file is the name of the file it will compress
    with settings(warn_only=True):
        files = datetime.now().strftime("versions/web_static_%Y%m%d%H%M%S.tgz")
        with hide('output', 'running'):
            command = local('mkdir versions')
            if command.return_code != 0:
                return None

        print('Packing web_static to {} web_static'.format(files))

        # with hide('stdout', 'running'):
        command = local('tar -cvzf {} web_static'.format(files))
        if command.return_code != 0:
            return None

        with hide('output', 'running'):
            size = local("wc -c {}".format(files), capture=True)
            if size.return_code != 0:
                return None
            size = size.stdout.split()[0]

        print("web_static packed: {} -> {}Bytes".format(files, size))
        return files
