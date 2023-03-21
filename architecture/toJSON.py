import h5py
import os
import json

main_directory = 'MillionSongSubset'

analysis = ['analysis_sample_rate', 'audio_md5', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'idx_bars_confidence', 'idx_bars_start', 'idx_beats_confidence', 'idx_beats_start', 'idx_sections_confidence', 'idx_sections_start', 'idx_segments_confidence', 'idx_segments_loudness_max', 'idx_segments_loudness_max_time', 'idx_segments_loudness_start', 'idx_segments_pitches', 'idx_segments_start', 'idx_segments_timbre', 'idx_tatums_confidence', 'idx_tatums_start', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'start_of_fade_out', 'tempo', 'time_signature', 'time_signature_confidence', 'track_id']

meta = ['analyzer_version', 'artist_7digitalid', 'artist_familiarity', 'artist_hotttnesss', 'artist_id', 'artist_latitude', 'artist_location', 'artist_longitude', 'artist_mbid', 'artist_name', 'artist_playmeid', 'genre', 'idx_artist_terms', 'idx_similar_artists', 'release', 'release_7digitalid', 'song_hotttnesss', 'song_id', 'title', 'track_7digitalid']

brainz = ['idx_artist_mbtags', 'year']

counter = 0

for root, dirs, files in os.walk(main_directory):
    for filename in files:
        counter += 1
        f = h5py.File(os.path.join(root, filename), 'r')
        dic = {}

        for i in analysis:
            dic[i] = str(f['analysis']['songs'][i][0])

        for i in meta:
            dic[i] = str(f['metadata']['songs'][i][0])

        for i in brainz:
            dic[i] = str(f['musicbrainz']['songs'][i][0])

        jsonDict = json.dumps(dic)
        newfile = "MSS-JSON/File" + str(counter) + ".json"

        with open(newfile, "w") as outfile:
            outfile.write(jsonDict)
            outfile.close()
        
        del f
