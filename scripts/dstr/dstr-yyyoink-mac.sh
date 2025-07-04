#!/bin/zsh

YYY_DIR="/Users/tymalik/Docs/Git/project/yyyoink"

REPOS=(
    yyyoink-apple
    yyyoink-avalonia
    yyyoink-android
    yyyoink-web
    yyyoink-portal
    yyyoink-bff
    yyyoink-api
    yyyoink-pipeline
    yyyoink-llm
    yyyoink-core
    yyyoink-operation
)

cd "$YYY_DIR" || exit 1

for repo in "${REPOS[@]}"; do
    if [ -d "$repo/.git" ]; then
        echo "Checking $repo"
        cd "$repo" || continue

        git status

        if ! git diff --quiet || ! git diff --cached --quiet; then
            echo "Found Changes in $repo: Adding, Committing, and Pushing.."
            git add .
            git commit -m "Auto commit before deletion." || echo "Nothing to commit."
            git push
        fi

        LOCAL_HASH=$(git rev-parse @)
        REMOTE_HASH=$(git rev-parse @{u})
        BASE_HASH=$(git merge-base @ @{u})

        # if [ "$LOCAL_HASH" = "$REMOTE_HASH" ]; then
        #     echo "Local branch is fully pushed."
        # elif [ "$LOCAL_HASH" = "$BASE_HASH" ]; then
        #     echo "Local is behind remote. Need to pull."
        # elif [ "$REMOTE_HASH" = "$BASE_HASH" ]; then
        #     echo "Local is ahead of remote. Need to push."
        # else
        #     echo "Local and remote have diverged."
        # fi

        if [[ "$LOCAL_HASH" = "$REMOTE_HASH" ]]; then
            echo "Deletion Safe: $repo"
            cd "$YYY_DIR"
            rm -rf "$repo"
        else
            echo "Unsafe Warning: $repo has unpushed commits."
            cd "$YYY_DIR"
        fi
    else
        echo "Cleanup Notice: $repo is not a git repo."
    fi
done
