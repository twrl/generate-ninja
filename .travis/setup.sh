#!/bin/bash

set -eufo pipefail

NINJA_VERSION="1.7.2"

source .travis/platform.sh

mkdir $HOME/bin

if [ "$PLATFORM" == "macosx" ]; then
  system="$system-darwin"
  NINJA_ZIP=ninja-mac.zip
  CC=clang
  CXX=clang++
elif [ "$PLATFORM" == "cygwin" ]; then
  system="$system-cygwin"
  NINJA_ZIP=ninja-win.zip
  CC=gcc
  CXX=g++
elif [ "$PLATFORM" == "linux" ]; then
  system="$system-linux"
  NINJA_ZIP=ninja-linux.zip
  CC=gcc
  CXX=g++

  add-apt-repository ppa:ubuntu-toolchain-r/test -y
  apt-get update -qq
  apt-get install -qq gcc-4.9 g++-4.9
  update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 60 --slave /usr/bin/g++ g++ /usr/bin/g++-4.9
  update-alternatives --install /usr/bin/cc cc /usr/bin/gcc 30
  update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++ 30
  update-alternatives --set cc /usr/bin/gcc
  update-alternatives --set c++ /usr/bin/g++
  update-alternatives --set gcc /usr/bin/gcc-4.9
fi

if [ -n "$NINJA_ZIP" ]; then
  wget https://github.com/ninja-build/ninja/releases/download/v$NINJA_VERSION/$NINJA_ZIP
  unzip -d $HOME/bin $NINJA_ZIP
  rm -f $NINJA_ZIP
fi

echo "$CC --version" && $CC --version
echo "$CXX --version" && $CXX --version
echo "ninja --version" && ninja --version
