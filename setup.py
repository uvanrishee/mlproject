from setuptools import find_packages,setup
def get_req(file):
    with open(file) as obj:
        requirments=obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
        if '-e .' in requirments:
            requirments.remove('-e .')
        return requirments
setup(
    name="ml-u-proj",
    version="0.0.1",
    author="uvan rishee",
    author_email="uvanrishee123@gmail.com",
    packages=find_packages(),
    install_requires=get_req("requirments.txt")
) 