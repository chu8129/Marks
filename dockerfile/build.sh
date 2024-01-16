

export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=0
for i in {1..1}; do docker build -f ./Dockerfile -t qw \
--build-arg http_proxy=http://178.16.0.122:7891 --build-arg https_proxy=http://178.16.0.122:7891 .; done
#   .; done

# --build-arg socks_proxy=socks5://178.16.0.122:7891 .;done

# DOCKER_BUILDKIT=1 docker build -f local.Dockerfile -t qw:tf291nightly .
