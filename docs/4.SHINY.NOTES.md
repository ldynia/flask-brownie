1. Set Up Proxy

    ```bash
    rm -rf app/data;
    rm -rf app/templates;
    rm -rf app/*.py;
    rm -rf app/*.txt;
    mv app/static app/;
    ```

1. End-to-End testing with bash

    tests/e2e.sh

    ```bash
    #!/usr/bin/env bash

    ENDPOINT=/
    FAILED=1
    REGEX='skill'
    SUCCESS=0

    function test_response_code() {
      TEST_NAME="Test status code"
      STATUS_CODE=$(curl localhost:5000$1 \
        --head \
        --output /dev/null \
        --silent \
        --write-out '%{http_code}\n'
      )

      if [ $STATUS_CODE == $2 ]; then
        echo "$TEST_NAME : Success"
        return $SUCCESS
      else
        echo "$TEST_NAME : Failed"
        return $FAILED
      fi
    }

    function test_body_content() {
      TEST_NAME="Test body content"
      MATCH=$(curl --silent localhost:5000$1 | grep -E $2 | xargs echo -n)
      if [ ! -z "$MATCH" ]; then
        echo "$TEST_NAME : Success"
        return $SUCCESS
      else
        echo "$TEST_NAME : Failed"
        return $FAILED
      fi
    }

    # Run tests
    test_response_code $ENDPOINT 200
    test_body_content $ENDPOINT $REGEX
    ```

1. Refactor to docker compose

    devops/docker/api.Dockerfile

    ```yaml
    version: '3.9'
    services:
      app:
        container_name: brownie-frontend
        image: brownie_frontend
        build:
          context: ../../
          dockerfile: devops/docker/frontend.Dockerfile
          args:
            FLASK_DEBUG: "True"
        ports:
          - "5000:5000"
    ```

    ```bash
    docker-compose --file devops/docker/docker-compose.yaml build
    docker-compose --file devops/docker/docker-compose.yaml up --detach
    docker-compose --file devops/docker/docker-compose.yaml stop
    docker-compose --file devops/docker/docker-compose.yaml down
    ```