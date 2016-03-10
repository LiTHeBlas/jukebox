#!/usr/bin/env bash

mopidy --config $MOPIDY_CONFIG_DIR \
    -o core/cache_dir=$MOPIDY_CACHE_DIR \
    -o core/config_dir=$MOPIDY_CONFIG_DIR \
    -o core/data_dir=$MOPIDY_DATA_DIR \
    -o local/data_dir=$MOPIDY_DATA_DIR/local \
    -o local/media_dir=$MOPIDY_MEDIA_DIR \
    -o m3u/playlists_dir=$MOPIDY_PLAYLISTS_DIR \
    -o spotify/cache_dir=$MOPIDY_CACHE_DIR/spotify \
    -o spotify/settings_dir=$MOPIDY_CONFIG_DIR/spotify \
    -o spotify/password=$SPOTIFY_PASSWORD \
    -o spotify/username=$SPOTIFY_USERNAME \
    "$@"
