DROP TABLE IF EXISTS songs CASCADE;

CREATE TABLE songs (
    id                SERIAL PRIMARY KEY,
    artist_hotttnesss DECIMAL,
    title             VARCHAR,
    energy            DECIMAL,
    loudness          DECIMAL,
    tempo             DECIMAL,
    artist_name       VARCHAR,
    track_id          VARCHAR,
    key               INTEGER,
    year              INTEGER,
    song_hotttnesss   DECIMAL
);
