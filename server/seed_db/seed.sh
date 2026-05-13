#!/bin/bash
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -c "INSERT INTO instructors(id, name, email, api_key) VALUES (gen_random_uuid(), 'main', 'fake@example.com', gen_random_uuid());"