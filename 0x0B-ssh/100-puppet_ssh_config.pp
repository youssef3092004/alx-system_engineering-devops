#!usr/bin/env bash
#use puppet to make changes to my config files
file { '/etc/ssh/ssh_config':
        ensure => present,
content => "
Include /etc/ssh/ssh_config.d/*.conf
Host *
    IdentityFile ~/.ssh/school
    passwordAuthentication no
",
}
