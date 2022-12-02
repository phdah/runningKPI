FROM ubuntu:20.04


RUN apt -qq update \
    && apt -qqy --no-install-recommends install \
      vim \
      curl
COPY test.sh ./test.sh
