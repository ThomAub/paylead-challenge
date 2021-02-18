#! /bin/bash

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PRJ_DIR="$(cd ${DIR}/.. >/dev/null 2>&1 && pwd)"
IMG="paylead_challenge-dev"

docker build -t "${IMG}" \
    --pull \
    -f "${DIR}/dev.dockerfile" \
    ${PRJ_DIR}