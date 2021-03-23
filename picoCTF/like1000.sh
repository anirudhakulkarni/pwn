#!/bin/bash

function extract(){
  tar -xvf ${1}
  rm $1 
  for tar in `find . -maxdepth 1 -iname `*.tar``; do
    extract $tar;
  done
}
extract '1000.tar'