#!/bin/sh

MY_JARS=
for d in $(find $HOME/.m2/repository -name "*.jar"); do
    MY_JARS="$d:$MY_JARS"
done
for d in $(find `pwd` -name "*.jar"); do
    MY_JARS="$d:$MY_JARS"
done
MY_JARS=$MY_JARS:.

exec java -cp $MY_JARS $@
