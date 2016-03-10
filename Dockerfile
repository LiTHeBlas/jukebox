FROM armbuild/ubuntu-debootstrap:wily
MAINTAINER Olle Vidner <olle@vidner.se>

ENV DEBIAN_FRONTEND=noninteractive
RUN sed -i 's/mirror.cloud.online.net/ports.ubuntu.com/' /etc/apt/sources.list

ADD https://apt.mopidy.com/mopidy.list https://apt.mopidy.com/mopidy.gpg /etc/apt/sources.list.d/
RUN apt-key add /etc/apt/sources.list.d/mopidy.gpg && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        python-dev \
        python-pip \
        python-gst0.10 \
        gstreamer0.10-plugins-good \
        gstreamer0.10-plugins-ugly \
        gstreamer0.10-tools \
        gstreamer0.10-alsa \
        libffi-dev \
        libspotify12 \
        libspotify-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r /requirements.txt

ENV MOPIDY_CACHE_DIR=/tmp/mopidy \
    MOPIDY_CONFIG_DIR=/mopidy/config \
    MOPIDY_DATA_DIR=/mopidy/data \
    MOPIDY_MEDIA_DIR=/mopidy/media \
    MOPIDY_PLAYLISTS_DIR=/mopidy/playlists
COPY start.sh mopidy.sh /
COPY mopidy.conf $MOPIDY_CONFIG_DIR/

EXPOSE 6600 6680
CMD ["/start.sh"]
