# puppet ssh configuration
exec { 'ensure no password is required':
  path    => '/bin',
  command => 'echo "PasswordAuthentication no" >> ~/.ssh/config',
  unless  => 'grep -q "PasswordAuthentication no" ~/.ssh/config'
}

exec { 'ensure to use private key school':
  path    => '/bin',
  command => 'echo "IdentityFile ~/.ssh/school" >> ~/.ssh/config',
  unless  => 'grep -q "IdentityFile ~/.ssh/school" ~/.ssh/config'
}
