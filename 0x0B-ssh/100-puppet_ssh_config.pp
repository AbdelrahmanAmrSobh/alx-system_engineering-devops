# puppet ssh configuration
exec { 'ensure no password is required':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  unless  => 'grep -q "PasswordAuthentication no" /etc/ssh/ssh_config'
}

exec { 'ensure to use private key school':
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  unless  => 'grep -q "IdentityFile ~/.ssh/school" /etc/ssh/ssh_config'
}
