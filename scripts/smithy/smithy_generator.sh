#!/usr/bin/env bash
set -e

which glide > /dev/null || {
    curl https://glide.sh/get | sh
}

# Run the generator tests
cd $FRUGAL_HOME
glide install
go build -o frugal
go test -race ./test
mv frugal $SMITHY_ROOT
rm -rf ./test/out
