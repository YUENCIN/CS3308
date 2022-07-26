import gnupg

gpg = gnupg.GPG('/usr/local/bin/gpg')
filename = 'secret.txt.gpg'
outputPath = 'res.txt'
stream = open(filename, 'rb')
p = open('password.txt','r')

for line in p:
    data = gpg.decrypt_file(stream, always_trust=False, passphrase=line, output=outputPath)
    print('ok', data.ok)
    print('status', data.status)
    print(line)

