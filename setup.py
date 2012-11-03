from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['test_rotx.py']
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        raise SystemExit(pytest.main(self.test_args))


setup(
    name='rotx',
    license='MIT',
    tests_require=[
        'pytest>=2.3.2',
    ],
    cmdclass={'test': PyTest},
)
