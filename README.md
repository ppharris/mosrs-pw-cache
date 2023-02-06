# mosrs-pw-cache
MOSRS password caching scripts for use at UKCEH.

* `mosrs-cache-password`: The original password caching script from the MOSRS
  wiki.  This is called (Bash `source`'d) by all of the GPG Agent setup scripts
  in this directory.
* `mosrs-setup-gpg-agent`: The original GPG Agent setup script from the MOSRS
  wiki.  This starts `gpg-agent` if it's not already running and then calls the
  password caching script.

* `mosrs-setup-gpg-agent-centos`: Version of `mosrs-setup-gpg-agent` that is
  more reliable on UKCEH CentOS 7 machines.
* `mosrs-setup-gpg-agent-rocky`: Version of `mosrs-setup-gpg-agent` that is
  needed on UKCEH Rocky 8 machines.  This is currently a crude prototype.

* `mosrs-env-checks`: Script to interrogate the user's environment and report
  various settings can be useful for diagnosing password caching problems.
