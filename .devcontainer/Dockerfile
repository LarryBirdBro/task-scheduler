FROM mcr.microsoft.com/devcontainers/javascript-node:20-bullseye

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install fastapi uvicorn motor

RUN corepack enable && corepack prepare pnpm@latest --activate
