cat password.txt | while read pass;
do result=$(gpg --output 1.txt -d --batch --passphrase $pass secret.txt.gpg 2>/dev/null);
if [ $? -eq 0 ];
	then echo $pass;
fi;
	done
