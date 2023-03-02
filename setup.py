from setuptools import setup

setup(
    name="mosrs-pw-cache",
    version="0.1.0",
    description="MOSRS password caching scripts for use at UKCEH",
    download_url="https://github.com/ppharris/mosrs-pw-cache",
    scripts=[
        "./mosrs-cache-password",
        "./mosrs-setup-gpg-agent",
        "./mosrs-setup-gpg-agent-centos",
        "./mosrs-setup-gpg-agent-rocky",
        "./mosrs-env-checks",
    ],
)
