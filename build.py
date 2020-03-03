#!/bin/env python
import os
import json
import subprocess
import sys
import shutil

class Debug:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def info(self, msg):
        print('[' + self.OKGREEN + 'info' + self.ENDC + '] ' + msg)

    def error(self, msg):
        print('[' + self.FAIL + 'error' + self.ENDC + '] ' + msg)


class Docker:
    def __init__(self, version, git_rev, distro, work_path):
        self.version = version
        self.git_rev = git_rev
        self.distro = distro
        self.dbg = Debug()
        self.work_path = work_path

        self.dbg.info('poller ' + self.dbg.OKBLUE + version + self.dbg.ENDC + '@' + self.dbg.OKBLUE
                 + git_rev + self.dbg.ENDC + ' on ' + self.dbg.OKBLUE + distro + self.dbg.ENDC)

        self.dbg.info('working dir : ' + self.dbg.OKBLUE + self.work_path + self.dbg.ENDC)

    def __launch(self, args_array):
        process = subprocess.Popen(args_array, stdout=subprocess.PIPE, universal_newlines=True)
        return_code = None
        while True:
            output = process.stdout.readline()
            print(output.strip())
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                # Process has finished, read rest of the output
                for output in process.stdout.readlines():
                    print(output.strip())
                break
        return return_code

    def build(self, name, deps):
        self.dbg.info('starting build phase for ' + self.dbg.OKBLUE + name + self.dbg.ENDC)

        os.chdir(self.work_path + '/' + name + '/build/' + self.distro)
        for dep in deps:
            src = self.work_path + '/packages/' + dep + '-' + self.version + '-r0.apk'
            dest = self.work_path + '/' + name + '/build/' + self.distro + '/' + dep + '-' + self.version + '-r0.apk'
            self.dbg.info('copy ' + self.dbg.OKBLUE + src + self.dbg.ENDC + ' to ' + self.dbg.OKBLUE + dest + self.dbg.ENDC)
            shutil.copyfile(src, dest)
        return_code = self.__launch(['docker', 'build', '-t', name + '-' + self.version + ':' + self.distro, '.'])
        os.chdir(self.work_path)

        if return_code == 0:
            self.dbg.info('build done')
            return True
        else:
            self.dbg.error('build fail with error code: ' + self.dbg.WARNING + str(return_code) + self.dbg.ENDC)
            return False

    def test(self, name):
        self.dbg.info('starting test phase for ' + self.dbg.OKBLUE + name + self.dbg.ENDC)

        os.chdir(self.work_path + '/' + name + '/test/' + self.distro)
        return_code = self.__launch(['docker', 'build', '-t', name + '-' + self.version + '-test:' + self.distro, '.'])
        os.chdir(self.work_path)

        if return_code == 0:
            self.dbg.info('build done')
            return True
        else:
            self.dbg.error('build fail with error code: ' + self.dbg.WARNING + str(return_code) + self.dbg.ENDC)
            return False

    def package(self, name, deps):
        self.dbg.info('starting package phase for ' + self.dbg.OKBLUE + name + self.dbg.ENDC)

        wdir = self.work_path + '/' + name + '/package/' + self.distro
        print(wdir)
        sys.path.append(wdir)
        import generate
        generate.generate_recipe(self.version, self.git_rev, wdir)
        del sys.modules["generate"]
        sys.path.remove(wdir)

        self.dbg.info('generate recipe ' + self.dbg.OKBLUE + "done" + self.dbg.ENDC)
        os.chdir(wdir)
        for dep in deps:
            src = self.work_path + '/packages/' + dep + '-' + self.version + '-r0.apk'
            dest = self.work_path + '/' + name + '/package/' + self.distro + '/' + dep + '-' + self.version + '-r0.apk'
            self.dbg.info('copy ' + self.dbg.OKBLUE + src + self.dbg.ENDC + ' to ' + self.dbg.OKBLUE + dest + self.dbg.ENDC)
            shutil.copyfile(src, dest)

        return_code = self.__launch(['docker', 'build', '-t', name + '-' + self.version + '-package:' + self.distro, '.'])
        return_code = return_code + self.__launch(['./get_files.sh', self.version])
        os.chdir(self.work_path)

        if return_code == 0:
            self.dbg.info('build done')
            return True
        else:
            self.dbg.error('build fail with error code: ' + self.dbg.WARNING + str(return_code) + self.dbg.ENDC)
            return False

if __name__ == '__main__':
    config = None
    with open('config.json', 'r') as f:
        config = json.load(f)

    dock = Docker(config['version'], config['git_tag'], config['distribution'], os.path.dirname(os.path.realpath(__file__)))

    for proj in config['build']:
        if proj['build'] == True:
            dock.build(proj['name'], proj['pkg_deps'])
        if proj['test'] == True:
            dock.test(proj['name'])
        if proj['package'] == True:
            dock.package(proj['name'], proj['pkg_deps'])
