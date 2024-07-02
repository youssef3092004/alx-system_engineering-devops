# This Puppet Create The School File
file { '/tmp/school':
  ensure  => 'present',
  mode    => '044',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
