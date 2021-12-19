
--
-- DDL
--

CREATE TABLE CAD_UTILISATEURS (
	SEQ_UTILISATEUR INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	TXT_COURRIEL TEXT(256) NOT NULL,
	TXT_MOT_PASSE TEXT(256) NOT NULL,
	NOM_UTILISATEUR TEXT(1024) NOT NULL,
	FLG_ACCEPTE_MARKETING INTEGER NOT NULL,
	FLG_ACTIF INTEGER NOT NULL,
	DTH_ENREGISTR INTEGER NOT NULL,
	DTH_CONF_COURRIEL INTEGER
);

CREATE TABLE TAB_GENRES_MUSIQ (
	COD_GENRE_MUSIQ INTEGER NOT NULL PRIMARY KEY,
	DSC_GENRE_MUSIQ TEXT(255) NOT NULL
);

CREATE TABLE TAB_TYPE_ARTISTE (
    COD_TYPE_ARTISTE INTEGER NOT NULL PRIMARY KEY,
    COD_TYPE_ARTISTE_PARENT INTEGER NULL,
    DSC_TYPE_ARTISTE TEXT(255) NOT NULL
)

CREATE TABLE CAD_ARTISTES (
	SEQ_ARTISTE                 INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	NOM_ARTISTE                 TEXT(255) NOT NULL,
	COD_ARTISTE                 TEXT(128) NOT NULL,
	COD_PAYS_ORIGINE            INTEGER NOT NULL,
	NUM_ANNEE_DEBUT_ACTIVITE    INTEGER NOT NULL,
	NUM_ANNEE_FIN_ACTIVITE      INTEGER,
	URL_SITEWEB                 TEXT(1024),
	DSC_HISTORIQUE              TEXT(2048)
);

CREATE TABLE CAD_GENRE_MUSIQ_ARTISTE (
	COD_GENRE_MUSIQ INTEGER NOT NULL,
	COD_ARTISTE INTEGER NOT NULL,
    PRIMARY KEY (COD_GENRE_MUSIQ, COD_ARTISTE)
);

CREATE TABLE CAD_TYPE_ALBUM (
    COD_TYPE_ALBUM INTEGER NOT NULL PRIMARY KEY,
    DSC_TYPE_ALBUM TEXT(255) NOT NULL,
    SIG_TYPE_ALBUM TEXT(16) NOT NULL
);

CREATE TABLE CAD_ALBUM (
    SEQ_ALBUM           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    COD_TYPE_ALBUM      INTEGER NOT NULL,
    COD_ALBUM           TEXT(32) NOT NULL, -- GUID
    SEQ_ARTISTE         INTEGER NOT NULL,
    NOM_ALBUM           TEXT(255) NOT NULL,
    NUM_ANNEE_SORTIE    INTEGER NOT NULL,
    DSC_ALBUM           TEXT(1024)
);

CREATE TABLE CAD_PISTES_ALBUM (
    SEQ_PISTE           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    SEQ_CHANSON         INTEGER NULL,
    SEQ_ALBUM           NOT NULL,
    NUM_ORDRE           INTEGER,
    NUM_FACE            INTEGER,
    NOM_PISTE           TEXT(255),
    NUM_DURATION_SEC    INTEGER NOT NULL,
    UNIQUE (NUM_ORDRE, NUM_FACE, SEQ_ALBUM)
);

CREATE TABLE CAD_FAVORIS_UTILISATEUR (
    SEQ_FAVORI          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    SEQ_PISTE           INTEGER NOT NULL,
    SEQ_UTILISATEUR     INTEGER NOT NULL,
    DTH_AJOUT           INTEGER NOT NULL
);

CREATE TABLE CAD_ALBUM_PHOTO (
	SEQ_ALBUM_PHOTO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	SEQ_ALBUM INTEGER NOT NULL,
	BIN_ALBUM_PHOTO BLOB NOT NULL,
	NUM_TAILLE INTEGER NOT NULL,
	DSC_MIME_TYPE TEXT(255),
	FLG_COMPRESSE INT NOT NULL
)

--
-- DATA
--

-- TYPE ALBUM

INSERT INTO CAD_TYPE_ALBUM ( COD_TYPE_ALBUM, DSC_TYPE_ALBUM, SIG_TYPE_ALBUM ) VALUES 
( 1, 'LONG PLAY', 'LP'), ( 2, 'EXTENDED PLAY', 'EP'), ( 3, 'MINI ALBUM', 'MA');

-- ARTISTES

INSERT INTO CAD_ARTISTES (NOM_ARTISTE,COD_ARTISTE,COD_PAYS_ORIGINE,NUM_ANNEE_DEBUT_ACTIVITE,NUM_ANNEE_FIN_ACTIVITE,URL_SITEWEB,DSC_HISTORIQUE) VALUES
	 ('The Beatles','THE_BEATLES',0,1960,1970,'https://thebeatles.com/','The Beatles were an English rock band, formed in Liverpool in 1960, whose best-known line-up comprised John Lennon, Paul McCartney, George Harrison and Ringo Starr. They are regarded as the most influential band of all time[1] and were integral to the development of 1960s counterculture and popular music''s recognition as an art form.'),
	 ('Queen','QUEEN',0,1970,NULL,'https://queenonline.com/','Queen are a British rock band formed in London in 1970. Their classic line-up was Freddie Mercury (lead vocals, piano), Brian May (guitar, vocals), Roger Taylor (drums, vocals) and John Deacon (bass). Their earliest works were influenced by progressive rock, hard rock and heavy metal, but the band gradually ventured into more conventional and radio-friendly works by incorporating further styles, such as arena rock and pop rock.');

-- GENRE MUSIQUE

INSERT INTO TAB_GENRES_MUSIQ (COD_GENRE_MUSIQ,DSC_GENRE_MUSIQ) VALUES
	 (1,'Blues'),
	 (2,'Classical'),
	 (3,'Country'),
	 (4,'Dance'),
	 (5,'Drill'),
	 (6,'Drum and bass'),
	 (7,'Dubstep'),
	 (8,'Easy Listening'),
	 (9,'Electronic Dance Music (EDM)'),
	 (10,'Emo');
INSERT INTO TAB_GENRES_MUSIQ (COD_GENRE_MUSIQ,DSC_GENRE_MUSIQ) VALUES
	 (11,'Funk'),
	 (12,'Folk'),
	 (13,'Garage'),
	 (14,'Grunge'),
	 (15,'Grime'),
	 (16,'Hip Hop'),
	 (17,'House'),
	 (18,'Indie'),
	 (19,'Jazz'),
	 (20,'K-Pop');
INSERT INTO TAB_GENRES_MUSIQ (COD_GENRE_MUSIQ,DSC_GENRE_MUSIQ) VALUES
	 (21,'Latin'),
	 (22,'Motown'),
	 (23,'Mod'),
	 (24,'Opera'),
	 (25,'Pop'),
	 (26,'Punk'),
	 (27,'Rap'),
	 (28,'Reggae'),
	 (29,'Rhythm and Blues (R&B)'),
	 (30,'Rock');
INSERT INTO TAB_GENRES_MUSIQ (COD_GENRE_MUSIQ,DSC_GENRE_MUSIQ) VALUES
	 (31,'Soul'),
	 (32,'Techno'),
	 (33,'Trance'),
	 (34,'World');


-- GENRE MUSIQUE ET ARTISTES

INSERT INTO CAD_GENRE_MUSIQ_ARTISTE (COD_GENRE_MUSIQ,COD_ARTISTE) VALUES
	 (30,2),
	 (30,1),
	 (25,1);

-- Albums et leur pistes

INSERT INTO CAD_ALBUM (COD_TYPE_ALBUM, COD_ALBUM, SEQ_ARTISTE, NOM_ALBUM, NUM_ANNEE_SORTIE, DSC_ALBUM) VALUES 
	(1, '21b559c4-6de6-4b00-91b1-e22db44db268', 1, 'Abbey Road', 1969, 'Abbey Road is the eleventh studio album by the English rock band the Beatles, released on 26 September 1969 by Apple Records. Named after the location of EMI Studios in London, the cover features the group walking across the streets zebra crossing, an image that became one of the most famous and imitated in popular music. The album''s initially mixed reviews were contrasted by its immediate commercial success, topping record charts in the UK and US. The single "Something" / "Come Together" was released in October and topped the US charts.'),
	(1, '9aa7f040-7f4e-44d4-a748-7a823bb496d2', 1, 'Yellow Submarine', 1969, 'Yellow Submarine is the tenth studio album by English rock band the Beatles, released on 13 January 1969 in the United States and on 17 January in the United Kingdom. It was issued as the soundtrack to the animated film of the same name, which premiered in London in July 1968. The album contains six songs by the Beatles, including four new songs and the previously released "Yellow Submarine" and "All You Need Is Love". The remainder of the album is a re-recording of the films orchestral soundtrack by the bands producer, George Martin. '),
	(1, '8229ae99-9d74-45a0-b178-d6b49b6b03fb', 2, 'Queen II', 1974, 'Queen II is the second studio album by the British rock band Queen. It was released on 8 March 1974 by EMI Records in the UK and by Elektra Records in the US.'),
	(1, '9d4f4180-a1b5-45de-a96c-8d3861a7266b', 2, 'Queen', 1973, 'Queen is the self-titled debut studio album by the British rock band Queen. Released on 13 July 1973 by EMI Records in the UK and by Elektra Records in the US, it was recorded at Trident Studios and De Lane Lea Music Centre, London, with production by Roy Thomas Baker, John Anthony and the band members themselves.');

INSERT INTO CAD_PISTES_ALBUM (SEQ_ALBUM, SEQ_CHANSON, NOM_PISTE, NUM_DURATION_SEC, NUM_ORDRE, NUM_FACE)	VALUES 
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '21b559c4-6de6-4b00-91b1-e22db44db268'), NULL, 'Come Together', 258, 1, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '21b559c4-6de6-4b00-91b1-e22db44db268'), NULL, 'Something', 150, 2, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '21b559c4-6de6-4b00-91b1-e22db44db268'), NULL, 'Maxwell''s Silver Hammer', 206, 3, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '21b559c4-6de6-4b00-91b1-e22db44db268'), NULL, 'Oh! Darling', 206, 4, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '21b559c4-6de6-4b00-91b1-e22db44db268'), NULL, 'Octopus''s Garden', 170, 5, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '21b559c4-6de6-4b00-91b1-e22db44db268'), NULL, 'I Want You (She''s So Heavy)	', 467, 6, 1);

INSERT INTO CAD_PISTES_ALBUM (SEQ_ALBUM, SEQ_CHANSON, NOM_PISTE, NUM_DURATION_SEC, NUM_ORDRE, NUM_FACE)	VALUES 
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Yellow Submarine', 157, 1, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Only a Northern Song', 203, 2, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'All Together Now', 128, 3, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Hey Bulldog', 189, 4, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'It''s All Too Much', 387, 5, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'All You Need Is Love', 228, 6, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Pepperland', 138, 1, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Sea of Time', 180, 2, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Sea of Holes', 136, 3, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Sea of Monsters', 215, 4, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'March of the Meanies', 136, 5, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Pepperland Laid Waste', 129, 6, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9aa7f040-7f4e-44d4-a748-7a823bb496d2'), NULL, 'Yellow Submarine in Pepperland', 130, 7, 2);
	
INSERT INTO  CAD_PISTES_ALBUM (SEQ_ALBUM, SEQ_CHANSON, NOM_PISTE, NUM_DURATION_SEC, NUM_ORDRE, NUM_FACE) VALUES 
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'Procession', 71, 1, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'Father to Son', 371, 2, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'White Queen (As It Began)', 271, 3, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'Some Day One Day', 260, 4, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'The Loser in the End', 240, 5, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'Ogre Battle', 246, 1, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'The Fairy Feller''s Master-Stroke', 160, 2, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'Funny How Love Is', 77, 3, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '8229ae99-9d74-45a0-b178-d6b49b6b03fb'), NULL, 'Seven Seas of Rhye', 391, 4, 2);

INSERT INTO  CAD_PISTES_ALBUM (SEQ_ALBUM, SEQ_CHANSON, NOM_PISTE, NUM_DURATION_SEC, NUM_ORDRE, NUM_FACE) VALUES 
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'Keep Yourself Alive', 223, 1, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'Doing All Right', 247, 2, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'Great King Rat', 342, 3, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'My Fairy King', 246, 4, 1),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'Liar', 382, 1, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'The Night Comes Down', 262, 2, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'Modern Times Rock ''n'' Roll', 107, 3, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'Son and Daughter', 198, 4, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'Jesus', 223, 5, 2),
	((SELECT SEQ_ALBUM FROM CAD_ALBUM ca WHERE COD_ALBUM  = '9d4f4180-a1b5-45de-a96c-8d3861a7266b'), NULL, 'Seven Seas of Rhye', 75, 6, 2);

-- ALBUM PHOTOS