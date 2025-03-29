from setuptools import setup, find_packages

setup(
    name="firewall-tool",
    version="0.1",
    packages=find_packages(),
    install_requires=["python-iptables"],
    author="Adınız",
    description="Python ile yazılmış bir firewall aracı",
    url="https://github.com/zehrakolsuz/firewall",
)
