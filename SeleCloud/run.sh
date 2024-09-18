#!/usr/bin/env bash

# Check if a file was provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide a file as an argument"
  exit 1
fi

# Get the file name from the argument
FILE_NAME=$1

# Check if the file exists
if [ ! -f "$FILE_NAME" ]; then
  echo "File $FILE_NAME does not exist"
  exit 1
fi

# Execute your custom command with the file
docker-compose exec selenium python /workspace/$FILE_NAME