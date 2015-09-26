from fabric.api import *

@task
def static():
    local("wget --recursive --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains localhost --no-parent http://localhost:8000/")


@task
def deploy():
    local("rsync -avz -e ssh localhost+8000/ 30029@simone.aldaran.org:/containers/30029/ncc4roma.it/ncc/static/preview/")
