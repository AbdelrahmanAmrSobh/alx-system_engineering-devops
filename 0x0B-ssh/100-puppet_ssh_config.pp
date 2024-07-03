# ensure usage of private key and no password is required

file_line { 'ensure usage of private key':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
}

file_line { 'ensure no password is required':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}
