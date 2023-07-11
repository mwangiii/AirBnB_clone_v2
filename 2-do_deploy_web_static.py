#!/usr/bin/python3
"""Deploys web_static on the servers listed"""
from fabric.api import run, put, env, with_settings


env.hosts = ['18.204.5.65', '100.25.28.239']


@with_settings(warn_only=True)
def do_deploy(archive_path):
    """ships and unpacks the .tgv file"""
    file_name = archive_path.split('/')[-1]
    folder_extract = file_name.replace(".tgz", "")

    put(archive_path, '/tmp')
    run('mkdir -p /data/web_static/releases/{}'.format(folder_extract))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(file_name, folder_extract))

    run('rm /tmp/{}'.format(file_name))
    run('mv -f /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}'.format(folder_extract, folder_extract))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_extract))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_extract))
