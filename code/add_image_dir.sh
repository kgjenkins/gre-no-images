#!/bin/bash

#script to recursively travel the content directory and create 'images' subdirectories

function traverse() {   
    for file in $(ls "$1")
    do
        if [[ ! -d ${1}/${file} ]]; then
            echo " ${1}/${file} is a file"
        else
          if [ ${file} != "images" ]; then
            echo "entering recursion with: ${1}${file}"
            mkdir "${1}/${file}/images"
            traverse "${1}/${file}"
          fi
        fi
    done
}

function main() {
    traverse "$1"
}

main "$1"
