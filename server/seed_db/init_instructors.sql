-- psql -U username -d myDataBase -a -f init_instructors.sql
INSERT INTO instructors(id, name, email, api_key) VALUES (gen_random_uuid(), 'main', 'fake@example.com', gen_random_uuid());
SELECT api_key FROM instructors;
