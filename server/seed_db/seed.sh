#!/bin/bash
psql -U username -d myDataBase -a -f init_instructors.sql
