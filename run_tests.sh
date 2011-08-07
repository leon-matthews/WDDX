#!/bin/bash


echo "Python2 Doctest README.txt"
echo "=========================="
python2.7 -m unittest discover -v
echo

echo "Python3 Doctest README.txt"
echo "=========================="
python3.2 -m doctest -v README.txt
echo

echo "Python2 Unit tests"
echo "=================="
python2.7 -m doctest -v README.txt
echo

echo "Python3 Unit tests"
echo "=================="
python3.2 -m unittest -v
echo
