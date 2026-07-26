#!/bin/bash

dir=$1

mkdir $dir && cd $dir && touch main.py main_test.py && cd ..
