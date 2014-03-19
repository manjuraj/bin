#!/bin/sh

find . -name target -type d | xargs -I {} rm -rf {}
