#!/bin/bash

#script to recursively travel the content directory and make filenames lowercase

function traverse() {   
    for file in $(ls "$1")
    do
        if [[ ! -d ${1}/${file} ]]; then
            echo " ${1}/${file} is a file"
            file_lower="$(tr [A-Z] [a-z] <<< "$file")"
            echo "${file_lower}"
            mv "${1}/${file}" "${1}/${file_lower}"
        else
          if [ ${file} != "images" ]; then
            echo "entering recursion with: ${1}${file}"
            file_lower="$(tr [A-Z] [a-z] <<< "$file")"
            echo "${file_lower}"
            mv "${1}/${file}" "${1}/${file_lower}"
            traverse "${1}/${file}"
          fi
        fi
    done
}

function main() {
    traverse "$1"
}

main "$1"