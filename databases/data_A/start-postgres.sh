#!/usr/bin/env bash

docker run --name 518-postgres -p 65432:5432 -e POSTGRES_PASSWORD=518 -v $(pwd)/csv_data:/csv_data -v $(pwd)/scripts:/scripts -v $(pwd)/data:/var/lib/postgresql/data -d postgres
