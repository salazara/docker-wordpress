import re, requests;

response = requests.get('https://api.wordpress.org/secret-key/1.1/salt/').text.strip()
content = open('/home/workspace/docker/wp-config-no-salt.php').read()
updated_content = re.sub('INSERT-SALT-HERE', response, content)
open('/home/workspace/docker/wp-config.php', 'w').write(updated_content)