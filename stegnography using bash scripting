#!/bin/bash
echo "Encrypt(E) or Decrypt(D)"
read z
if  [ "$z" == "E" ]; then
    echo "Enter the file/text location : "
    read a
    echo "Enter the image location : "
    read b
    echo "Enter the Password to encrypt : "
    read c 
    echo "Executing...."
    sleep 4
    steghide embed -ef $a -cf $b -p $c
else
    echo "Enter the location of file to decypt : "
    read a
    steghide extract -sf $a -xf extracted.txt
    cat extracted.txt
fi
