CREATE TABLE export_profiles (
    id         SERIAL PRIMARY KEY,
    name       TEXT UNIQUE NOT NULL,
    salt       TEXT NOT NULL,
    iterations INTEGER NOT NULL DEFAULT 180000
);

INSERT INTO export_profiles (id, name, salt, iterations) VALUES (1, 'legacy-v1', '9c1f4a7d2e6b08f35a9d4c7e1b02f68a', 120000);
INSERT INTO export_profiles (id, name, salt, iterations) VALUES (2, 'standard', '42b7e0c95d18a36f7c04e9b2d5a81f30', 180000);
INSERT INTO export_profiles (id, name, salt, iterations) VALUES (3, 'archive-cold', 'd70e5b13c8a94f26b0d7e3a91c58f402', 210000);
INSERT INTO export_profiles (id, name, salt, iterations) VALUES (4, 'compliance', '6a3c9e07f4b21d85e09c6a3f7d14b298', 240000);

SELECT setval('export_profiles_id_seq', (SELECT max(id) FROM export_profiles));
