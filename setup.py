import os
import sys
import glob
import fnmatch
from setuptools import setup,Extension
import distutils.command.install_data
def opj(*args):
        path = os.path.join(*args)
        return os.path.normpath(path)
class wx_smart_install_data(distutils.command.install_data.install_data):
        def run(self):
                install_cmd = self.get_finalized_command('install')
                self.install_dir = getattr(install_cmd, 'install_lib')
                return distutils.command.install_data.install_data.run(self)
def find_data_files(srcdir, *wildcards, **kw):
        OMIT=['.c','.pyc','.egg-info','.so']
        def walk_helper(arg, dirname, files):
                if '.svn' in dirname or 'CVS' in dirname:
                        return
                names = []
                lst, wildcards = arg
                for wc in wildcards:
                        wc_name = opj(dirname, wc)
                        for f in files:
                                filename = opj(dirname, f)
                                if not any(filename.endswith(x) for x in OMIT):
                                        if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                                                names.append(filename)
                if names:
                        lst.append( (dirname, names ) )
        file_list = []
        recursive = kw.get('recursive', True)
        if recursive:
                os.path.walk(srcdir, walk_helper, (file_list, wildcards))
        else:
                walk_helper((file_list, wildcards),
                                        srcdir,
                                        [os.path.basename(f) for f in glob.glob(opj(srcdir, '*'))])
        return file_list
files = find_data_files('vapeplot/', '*.*')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name = "vapeplot",
    version = "0.0.2",
    author = "Danny Antaki",
    author_email = "dantaki@ucsd.edu",
    description = ("matplotlib extension for vaporwave aesthetics"),
    license = "GPLv2",
    keywords = "vaporwave matplotlib",
    url = "https://github.com/dantaki/vapeplot/",
    packages=['vapeplot'],
    package_dir={'vapeplot':'vapeplot/'},
    package_data= { 'vapeplot': ['vapeplot/aesthetics.json'] },
    data_files = files,
    long_description=read('README.md'),
    include_package_data=True,
    install_requires=['matplotlib'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Topic :: Multimedia :: Graphics',
    ],
    cmdclass = {'install_data': wx_smart_install_data},
)

