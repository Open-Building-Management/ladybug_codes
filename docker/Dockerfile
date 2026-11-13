ARG BUILD_FROM=python:3.11-slim

FROM $BUILD_FROM

ARG ENERGYPLUS_VERSION=24.1.0
ARG ENERGYPLUS_BUILD=9d7789a3ac
ARG ROOT=https://github.com/NatLabRockies/EnergyPlus/releases/download
ARG ENERGYPLUS_PLATFORM=Linux-Ubuntu22.04-x86_64
ARG GITHUB_ARCH=https://github.com/Open-Building-Management/ladybug_codes/archive/refs/tags
ARG IDFHUB_REF=0.0.4
ARG IDFHUB_PATH=/opt/ladybug_codes
ARG OS_EP_PATH=/opt/energyplus
ARG MOD_CONF="s|^os_ep_path:.*|os_ep_path: ${OS_EP_PATH}|"

RUN apt-get update && apt-get install -y \
    wget \
    tar \
    libgomp1 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q \
    "${ROOT}/v${ENERGYPLUS_VERSION}/EnergyPlus-${ENERGYPLUS_VERSION}-${ENERGYPLUS_BUILD}-${ENERGYPLUS_PLATFORM}.tar.gz" \
    -O /tmp/energyplus.tar.gz \
    && mkdir -p ${OS_EP_PATH} \
    && tar -xzf /tmp/energyplus.tar.gz -C ${OS_EP_PATH} --strip-components=1 \
    && rm /tmp/energyplus.tar.gz

RUN wget -q \
    "${GITHUB_ARCH}/${IDFHUB_REF}.tar.gz" \
    -O /tmp/ladybug_codes.tar.gz \
    && mkdir -p ${IDFHUB_PATH} \
    && tar -xzf /tmp/ladybug_codes.tar.gz -C ${IDFHUB_PATH} --strip-components=1 \
    && rm /tmp/ladybug_codes.tar.gz \
    && pip install --no-cache-dir ${IDFHUB_PATH}

RUN find ${IDFHUB_PATH} \
    -type f \( -name '*.yml' -o -name '*.yaml' \) \
    -exec sed -i "${MOD_CONF}" {} +

ENV PATH="${OS_EP_PATH}:${PATH}"

LABEL org.opencontainers.image.source="https://github.com/Open-Building-Management/ladybug_codes"
WORKDIR /workspace
