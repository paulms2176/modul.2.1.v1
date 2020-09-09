#!/bin/bash

git add *
git config --global user.email "paul2176@djhhadsten.dk"
git config --global user.name "paulms2176"
echo Navn til commiten?
read commit
git commit -m $commit
git push
