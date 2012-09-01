from __future__ import with_statement
from fabric.api import settings, run, cd

def deploy():
    code_dir = '/srv/vhosts/education/'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:azpm/azpm-www-education.git %s" % code_dir)
            run("setfacl -m d:g:http_srv:rwx %slogs")

    with cd(code_dir):
        run("git pull")

    load_config()

def restart_site():
    working_dir = '/srv/vhosts/education/public'
    with cd(working_dir):
        run("touch run.wsgi")

def load_config(mode="production"):
    working_dir = '/srv/vhosts/'
    with cd(working_dir):
        run("cp deployment/{0:>s}/education/local_settings.py education/project/".format(mode))