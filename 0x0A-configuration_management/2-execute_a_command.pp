# this manifest to kill killmenow task using pkill

exec {'pkill':
  command => '/usr/bin/pkill -9 killmenow',
  onlyif  => '/usr/bin/which pkill',
}
