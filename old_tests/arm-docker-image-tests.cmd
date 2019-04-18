::::::::::::::::::::::::::::::::::::::::::::::::
::          Arm Docker for Windows Test Suite
::
:: This script is intended to verify that various Arm 32-bit (arm32v7) and 64-bit (arm64v8)
:: docker images run as expected on x86 Docker hosts, such as Docker for Windows and Docker on Linux.
::

::::::::::::::::::::
:: Issue List
:: 1) Volume mounts arn't working. Firewall issues.
::          SET hostDir=%cd%
::          echo %hostDir%
::          docker run -it --rm --name python_test -v "%hostDir%":/usr/src/myapp -w /usr/src/myapp arm32v7/python:3 python hello_world_python.py

::::::::::::::::::::
:: What to test:
:: 
	:: hello-world
	:: Javascript (NodeJS)
	:: Python2
	:: Python3
	:: Java
	:: GCC (C and C++)
	:: Ruby
	::.NET
	:: Golang
	:: Rust
	:: PHP



:: hello-world
docker run -it --rm --platform linux/arm/v7 --name hello_test arm32v7/hello-world	
docker run -it --rm --platform linux/arm/v8 --name hello_test arm64v8/hello-world	


:: Javascript (NodeJS)
docker run -it --rm --platform linux/arm/v7 --name node_test arm32v7/node
	:: ERROR = > qemu: Unsupported syscall: 397
docker run -it --rm --platform linux/arm/v8 --name node_test arm64v8/node
	:: ERROR = > qemu: Unsupported syscall: 291
::docker run -it --rm --name node_test node
	:: ERROR = > qemu: Unsupported syscall: 397
::docker run -it --rm --platform linux/amd64 --name node_test amd64/node:alpine
	:: Works


:: Python 2
docker run -it --rm --platform linux/arm/v7 --name python_test arm32v7/python:2 python -c "print 'arm32v7/python:2 SUCCESS'"
docker run -it --rm --platform linux/arm/v8 --name python_test arm64v8/python:2 python -c "print 'arm64v8/python:2 SUCCESS'"

:: Python 3
docker run -it --rm --platform linux/arm/v7 --name python_test arm32v7/python:3 python -c "print('arm32v7/python:3 SUCCESS')"
docker run -it --rm --platform linux/arm/v8 --name python_test arm64v8/python:3 python -c "print('arm64v8/python:3 SUCCESS')"


:: Java (jdk)
docker run -it --rm --platform linux/arm/v7 --name java_test arm32v7/openjdk
	:: ERROR = qemu: Unsupported syscall: 345
	::		   Error occurred during initialization of Volume
	:: 		   getcpu(2) system call not supported by kernel
docker run -it --rm --platform linux/arm/v8 --name java_test arm64v8/openjdk


:: GCC (C and C++)
docker run -it --rm --platform linux/arm/v7 --name gcc_test arm32v7/gcc gcc --version
docker run -it --rm --platform linux/arm/v8 --name gcc_test arm64v8/gcc gcc --version
::docker run -it --rm --platform linux/amd64 --name gcc_test amd64/gcc gcc --version


:: Ruby
docker run -it --rm --platform linux/arm/v7 --name ruby_test arm32v7/ruby ruby --version
docker run -it --rm --platform linux/arm/v8 --name ruby_test arm64v8/ruby ruby --version


:: .NET Core
docker run --rm mcr.microsoft.com/dotnet/core/samples
docker run -it --rm --platform linux/arm/v7 --name dotnetcore_test arm32v7/mcr.microsoft.com/dotnet/core/samples


:: Golang 	Alpine 	1.12.2   
docker run -it --rm --platform linux/arm/v7 --name golang_test arm32v7/golang:alpine go version
docker run -it --rm --platform linux/arm/v8 --name golang_test arm64v8/golang:alpine go version


:: Rust
docker run -it --rm --platform linux/arm/v7 --name rust_test arm32v7/rust cargo --version
docker run -it --rm --platform linux/arm/v8 --name rust_test arm64v8/rust cargo --version

:: PHP
docker run -it --rm --platform linux/arm/v7 --name php_test arm32v7/php php --version
docker run -it --rm --platform linux/arm/v8 --name php_test arm64v8/php php --version

