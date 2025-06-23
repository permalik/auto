#!/bin/zsh

if [ "$1" = "dev" ]; then
    LLM_DIR="/Users/tymalik/Docs/Git/project/LLM"
else
    echo "./init-blue.sh < env >"
    echo "Provide Environment: dev, prod"
    exit 0
fi

cd "$LLM_DIR"

git clone git@github.com:permalik/blue-web-frontend.git
git clone git@github.com:permalik/blue-web-backend.git
git clone git@github.com:permalik/blue-api.git
git clone git@github.com:permalik/blue-preprocess.git
git clone git@github.com:permalik/blue-dispatch.git
git clone git@github.com:permalik/blue-core.git
git clone git@github.com:permalik/blue-postprocess.git
git clone git@github.com:permalik/blue-feedback.git
git clone git@github.com:permalik/blue-notification.git
git clone git@github.com:permalik/blue-operation.git
