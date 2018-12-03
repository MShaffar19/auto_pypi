#!/Users/leisen/anaconda3/bin/python3
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-30 13:30
# * Last modified : 2018-11-30 13:30
# * Filename      : main.py
# * Description   : 
# *********************************************************

import sys
import os
import click
import subprocess
import shlex


HERE = os.path.dirname(os.path.abspath(__file__))


@click.command()
@click.option(
    'pkg_name', '--name', '-n',
    help="Specify the package name. ",
    required=True,
    prompt="Please specify package name",
)
@click.option(
    'pkg_version', '--version', '-v',
    help="Specify the package version number. ",
    required=True,
    prompt="Please specify (new) package version number",
)
@click.option(
    'real_pypi', '--real', '-r',
    default=False,
    is_flag=True,
    help="Use the real PyPi index (instead of test PyPi by default). ",
    required=False,
#    prompt='Are you sure you want to use real PyPi index (instead of test PyPi)? '
)
#@click.argument('pkg_dir', nargs=1, type=click.STRING, required=True)
@click.argument(
    'pkg_dir', 
    nargs=1, 
    type=click.Path(exists=True, file_okay=False, writable=True), 
    required=True, 
    default='./',
)
def main(pkg_dir, pkg_name, pkg_version, real_pypi):
    """
    Python command line tool to setup Python package automatically. 
    \b
    Example:
    \b
    \t $ autopypi your-package-root-directory -n package_name -v package_version -r
    \t 
    """
    if real_pypi:
        click.echo("")
        click.echo("! Using REAL PyPi index ! ")
    else:
        click.echo("")
        click.echo("! Using TEST PyPi index ! ")

    click.echo("  Setting up package: [{}]-v{} ".format(pkg_name, pkg_version))
    click.echo("")

    if real_pypi:
        command_script = "ls -l -a"
        process = subprocess.Popen(command_script, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(command_script)
        print(process.returncode)

        command_script = HERE + '/setup_new_pypi.sh' + ' ' + pkg_name
        subprocess.call(shlex.split(command_script))
        #twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
    else:
        subprocess.Popen(["bash", "./setup_new_pypi.sh"])
        #twine upload --repository-url https://test.pypi.org/legacy/ dist/*
