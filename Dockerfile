####################
# - Stage: Builder
####################
FROM docker.io/python:3.11-slim-bookworm as base-python
WORKDIR /app-src

# Build Variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PIP_NO_CACHE_DIR 1
## Disable Non-Reproducible pip

# Runtime Variables
ENV PYTHONOPTIMIZE 1
ENV PYTHONUNBUFFERED 1

# Get Make
RUN apt update \
	&& apt install --no-install-recommends -y \
		make libenchant-2-2

# Install Dependencies
COPY ./requirements.txt /app-src/requirements.txt
RUN pip install -r /app-src/requirements.txt
RUN pip install -U sphinx>=7.2.5

# Make
COPY ./ /app-src/
RUN make all



####################
# - Stage: Production
####################
FROM ghcr.io/static-web-server/static-web-server:2-debian as production

RUN apt update \
	&& apt upgrade -y \
	&& apt install --no-install-recommends -y \
		curl

RUN groupadd -g 5000 sws && \
	useradd -m -u 5000 -g sws sws

COPY --from=base-python --chown=sws:sws /app-src/build/html/ /app

USER sws
WORKDIR /app

HEALTHCHECK CMD curl --fail http://localhost:3000 || exit 1

ENV SERVER_PORT 3000
ENV SERVER_ROOT /app
ENV SERVER_LOG_REMOTE_ADDRESS false
