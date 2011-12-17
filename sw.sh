#!/bin/sh

BEGIN=$(date +%s)
while true; do
    NOW=$(date +%s)
    let DIFF=$(($NOW - $BEGIN))
    let MINS=$(($DIFF / 60))
    let SECS=$(($DIFF % 60))
    printf "\rTime elapsed: %d:%02d" $MINS $SECS
    sleep 1
done
