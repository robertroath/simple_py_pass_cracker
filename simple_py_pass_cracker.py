import sys
import crypt

passfile=open('rockyou.txt','r')
for word in passfile.readlines();
  if (crypt.crypt(word.strip()."MS")==sys.argv[1]);
    print "password is "+word

