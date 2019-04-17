#::::::::::::::::::::::::::::::::::::::::::::::
#::          Arm Docker for Windows & Mac Test Suite
#::
#:: This script is intended to verify that various Arm 32-bit (arm32v7) and 64-bit (arm64v8)
#:: docker images run as expected on x86 Docker hosts, such as Docker for Windows and Docker on Linux.
#::

#::::::::::::::::::::
#:: Issue List
#:: 1) Volume mounts arn't working. Firewall issues.
#::          SET hostDir=%cd%
#::          echo %hostDir%
#::          docker run -it --rm --name python_test -v "%hostDir%":/usr/src/myapp -w /usr/src/myapp arm32v7/python:3 python hello_world_python.py







from subprocess import Popen, PIPE, STDOUT
import csv   



def get_platform_syntax(arch):
    if (arch=="x86"):
        platform=""
    elif arch=="arm32" or arch=="arm" or arch=="arm32v7":
        platform="--platform linux/arm"
    elif arch=="arm64" or arch=="aarch64" or arch=="arm64v8":
        platform="--platform linux/arm64"

    return platform



def docker_rmi(image,arch):
    cmd="docker rmi -f %s" %image
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()    # doesn't return until process is done
    if (p.returncode==0):
        # See if no image exists
        if ("No such image" in stderr):
            print "______Docker rmi %s inaction: image does not exist." %image
            return True
        else:
            print "______Docker rmi %s removed" %image
            return True
    else:
        print "!"*100
        print "______Docker rmi %s error:" %image
        print stderr
        return False



def docker_pull(image,arch):
    platform = get_platform_syntax(arch)

    cmd="docker pull %s %s" %(platform,image)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()    # doesn't return until process is done
    if(p.returncode==0):
        print "______Docker pull %s success" %image
        return True,cmd
    else:
        print "!"*100
        print "______Docker pull %s error:" %image
        print "Command: %s" %cmd
        print stderr
        return False,cmd


def docker_run(image,arch,options):
    platform = get_platform_syntax(arch)

    cmd="docker run %s %s %s" %(platform,image,options)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()    # doesn't return until process is done
    if(p.returncode==0
        ):
        print "______Docker run %s success. Output:" %image
        print stdout
        return True,cmd
    else:
        print "!"*100
        print "______Docker run %s error:" %image
        print "Command: %s" %cmd
        print stderr
        return False,cmd




def log_arch_run(csv_log,data):
    with open(csv_log, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)





csv_log="docker_run_log.csv"
# (image,cmd_to_run)
tests = [  ("hello-world",""),
            ("node:alpine","uname -a"),
            ("python:2-alpine","python -c 'import platform; print platform.machine()'"),
            ("python:3-alpine","python -c 'import platform; print(platform.machine())'"),
            ("openjdk:alpine","uname -a"),
            ("gcc","uname -a"),
            ("ruby:alpine","uname -a"),
            ("rust:slim","uname -a"),
            ("mcr.microsoft.com/dotnet/core/samples","uname -a"),
            ("golang:alpine","uname -a"),
            ("php:alpine","php --version")
         ]



log_arch_run(csv_log,["Image","Arch","Execution Commands","Pull Status","Run Status","Pull Command","Run Command"])
for run in tests:
    image=run[0]
    options=run[1]
    print "="*100
    for arch in ["x86","arm32","arm64"]:
        print "_"*70
        docker_rmi(image,arch)
        pull_status,pull_cmd = docker_pull(image,arch)
        run_status,run_cmd = docker_run(image,arch,options)
        docker_rmi(image,arch)

        log_arch_run(csv_log,[image,arch,options,pull_status,run_status,pull_cmd,run_cmd])
        









#docker pull $DESKTOP hello-world
#docker run $DESKTOP -it --rm --name hello hello-world
#docker rmi hello-world




'''
## declare an array variable
declare -a images=("hello-world" 
                "node:alpine"
                "python:2-alpine"
                "python:3-alpine"
                "openjdk:alpine"
                "gcc"
                "ruby:alpine"
                "rust:slim"
                "mcr.microsoft.com/dotnet/core/samples"
                "golang:alpine"
                "php:alpine"
                )


## now loop through the above array
for i in "${images[@]}"
do
   echo $ARM32 "$i"
   # or do whatever with individual element of the array
done

# You can access them using echo "${arr[0]}", "${arr[1]}" also
'''




'''



#:: hello-world
echo "----------------------" && echo "HelloWorld" && echo "----------------------"
docker pull $DESKTOP hello-world
docker run $DESKTOP -it --rm --name hello hello-world
docker rmi hello-world

docker pull $ARM32 hello-world
docker run $ARM32 -it --rm --name hello hello-world
docker rmi hello-world

docker pull $ARM64 hello-world
docker run $ARM64 -it --rm --name hello hello-world
docker rmi hello-world

docker system prune -f



#:: Javascript (NodeJS)
echo "----------------------" && echo "NodeJS" && echo "----------------------"
docker pull $DESKTOP node:alpine
docker run $DESKTOP -it --rm --name node node:alpine uname -a
docker rmi node:alpine

docker pull $ARM32 node:alpine
docker run $ARM32 -it --rm --name node node:alpine uname -a
docker rmi node:alpine

docker pull $ARM64 node:alpine
docker run $ARM64 -it --rm --name node node:alpine uname -a
docker rmi node:alpine



#:: Python 2
echo "----------------------" && echo "Python2" && echo "----------------------"
docker pull $DESKTOP python:2-alpine
docker run $DESKTOP -it --rm --name python2 python:2-alpine uname -a
docker rmi python:2-alpine

docker pull $ARM32 python:2-alpine
docker run $ARM32 -it --rm --name python2 python:2-alpine uname -a
docker rmi python:2-alpine

docker pull $ARM64 python:2-alpine
docker run $ARM64 -it --rm --name python2 python:2-alpine uname -a
docker rmi python:2-alpine


#:: Python 3
echo "----------------------" && echo "Python3" && echo "----------------------"
docker pull $DESKTOP python:3-alpine
docker run $DESKTOP -it --rm --name python3 python:3-alpine uname -a
docker rmi python:3-alpine

docker pull $ARM32 python:3-alpine
docker run $ARM32 -it --rm --name python3 python:3-alpine uname -a
docker rmi python:3-alpine

docker pull $ARM64 python:3-alpine
docker run $ARM64 -it --rm --name python3 python:3-alpine uname -a
docker rmi python:3-alpine





#:: Java (jdk)
echo "----------------------" && echo "Python3" && echo "----------------------"
docker pull $DESKTOP openjdk:alpine
docker run $DESKTOP -it --rm --name java openjdk:alpine uname -a
docker rmi openjdk:alpine

docker pull $ARM32 openjdk:alpine
docker run $ARM32 -it --rm --name java openjdk:alpine uname -a
docker rmi openjdk:alpine

docker pull $ARM64 openjdk:alpine
docker run $ARM64 -it --rm --name java openjdk:alpine uname -a
docker rmi openjdk:alpine





#:: Java (jdk)
docker run -it --rm --platform linux/arm/v7 --name java_test arm32v7/openjdk
	#:: ERROR = qemu: Unsupported syscall: 345
	#::		   Error occurred during initialization of Volume
	#:: 		   getcpu(2) system call not supported by kernel
docker run -it --rm --platform linux/arm/v8 --name java_test arm64v8/openjdk


#:: GCC (C and C++)
docker run -it --rm --platform linux/arm/v7 --name gcc_test arm32v7/gcc gcc --version
docker run -it --rm --platform linux/arm/v8 --name gcc_test arm64v8/gcc gcc --version
#::docker run -it --rm --platform linux/amd64 --name gcc_test amd64/gcc gcc --version


#:: Ruby
docker run -it --rm --platform linux/arm/v7 --name ruby_test arm32v7/ruby ruby --version
docker run -it --rm --platform linux/arm/v8 --name ruby_test arm64v8/ruby ruby --version


#:: .NET Core
docker run --rm mcr.microsoft.com/dotnet/core/samples
docker run -it --rm --platform linux/arm/v7 --name dotnetcore_test arm32v7/mcr.microsoft.com/dotnet/core/samples


#:: Golang 	Alpine 	1.12.2   
docker run -it --rm --platform linux/arm/v7 --name golang_test arm32v7/golang:alpine go version
docker run -it --rm --platform linux/arm/v8 --name golang_test arm64v8/golang:alpine go version


#:: Rust
docker run -it --rm --platform linux/arm/v7 --name rust_test arm32v7/rust cargo --version
docker run -it --rm --platform linux/arm/v8 --name rust_test arm64v8/rust cargo --version

#:: PHP
docker run -it --rm --platform linux/arm/v7 --name php_test arm32v7/php php --version
docker run -it --rm --platform linux/arm/v8 --name php_test arm64v8/php php --version
'''