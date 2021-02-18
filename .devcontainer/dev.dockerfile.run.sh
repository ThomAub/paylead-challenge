#! /bin/bash

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PRJ_DIR="$(cd ${DIR}/.. >/dev/null 2>&1 && pwd)"
IMG="paylead_challenge-dev"

docker run -d --rm \
    -p 80:80 \
    --workdir /workspace \
    --name "${IMG}" "${IMG}" \
    poetry run uvicorn paylead_challenge.main:api --host 0.0.0.0 --port 80