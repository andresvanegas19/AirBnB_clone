#!/usr/bin/python3
""" Automate the service on the server """
from datetime import datetime
from fabric.api import (local, hide, settings, env, run, put, sudo)
from os.path import exists

env.hosts = ['35.196.255.60', '35.227.13.42']


def do_pack():
    """ generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone
    repo, using the function do_pack """
    # file is the name of the file it will compress
    with settings(warn_only=True):
        files = datetime.now().strftime("versions/web_static_%Y%m%d%H%M%S.tgz")
        try:
            with hide('output', 'running'):
                command = local('mkdir versions')

            print('Packing web_static to {} web_static'.format(files))

            # with hide('stdout', 'running'):
            command = local('tar -cvzf {} web_static'.format(files))

            with hide('output', 'running'):
                size = local("wc -c {}".format(files), capture=True)
                size = size.stdout.split()[0]

            print("web_static packed: {} -> {}Bytes".format(files, size))
            return files
        except:
            return None

def do_deploy(archive_path):
    """ distributes an archive to your web servers, using the function
    do_deploy """
    if not archive_path or not exists(archive_path):
        return False
    with settings(warn_only=True):
        # Upload the archive to the /tmp/ directory of the web server
        command = put(archive_path, '/tmp/')
        if not command.__dict__['succeeded']:
            return False
        # if len(archive_path.split('/')) == 2:
        # tener en cuenta condicional por si el
        # archvio comprimido esta en otro lugar
        archive_path = archive_path.split('/')[1]
        # create a path
        path = "/data/web_static/releases/{}/".format(archive_path[:-4])
        # Uncompress the archive to the folder

        command = sudo('mkdir -p {}'.format(path))
        if not command.__dict__['succeeded']:
            return False

        # Uncompress the archive to the folder
        command = sudo('tar -xvf /tmp/{} -C {}'.format(archive_path, path))
        if not command.__dict__['succeeded']:
            return False

        # Delete the archive from the web server
        command = sudo('rm /tmp/{}'.format(archive_path))
        if not command.__dict__['succeeded']:
            return False

        command = sudo('mv {}/web_static/*  {}'.format(path, path))
        if not command.__dict__['succeeded']:
            return False

        # Delete the symbolic link /data/web_static/current from the web server
        command = sudo('rm -rf {}/web_static'.format(path))
        if not command.__dict__['succeeded']:
            return False
        command = sudo('rm -rf /data/web_static/current')
        if not command.__dict__['succeeded']:
            return False

        command = sudo('ln -s {} /data/web_static/current'.format(path))
        if not command.__dict__['succeeded']:
            return False

        print('New version deployed!')
        return True


def deploy():
    """creates and distributes an archive to your web servers,
    using the function deploy"""
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
