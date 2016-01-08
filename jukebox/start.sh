#!/usr/bin/env bash
mkdir -p $MOPIDY_CACHE_DIR $MOPIDY_CONFIG_DIR $MOPIDY_DATA_DIR $MOPIDY_MEDIA_DIR $MOPIDY_PLAYLISTS_DIR
/mopidy.sh local scan
/mopidy.sh
