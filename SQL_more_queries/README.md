# SQL - More Queries

## Description
This project is a continuation of SQL fundamentals, focused on more advanced querying and database administration. It covers:
- Creating and managing MySQL users and privileges
- Enforcing constraints (NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY)
- Designing and populating relational tables (`states`, `cities`, `tv_genres`, `tv_shows`, `tv_show_genres`)
- Writing `JOIN` queries (INNER, LEFT) to combine data across tables
- Using subqueries and `GROUP BY` / aggregate functions
- Understanding how SQL database engines work internally

The goal of this project is to strengthen SQL query-writing skills and understand relational database design, including how tables relate to each other through foreign keys.

## Requirements
- Ubuntu 20.04 LTS
- MySQL 8.0 (or MySQL 5.7, depending on setup)
- All SQL files are executed on Ubuntu with `mysql` (version specified per task)
- All files should end with a new line
- All SQL queries should have a comment just before them
- All files should start with a comment describing the task
- All SQL keywords should be uppercase (`SELECT`, `WHERE`, etc.)

## Installation
```bash
git clone https://github.com/RahafN1/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/SQL_more_queries
```

Run a script against your local MySQL server:
```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists all privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates the MySQL server user `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates a database and a user with only `SELECT` privilege |
| `3-force_name.sql` | Adds a `NOT NULL` constraint to `name` on a `users` table |
| `4-never_empty.sql` | Adds a default value of `0` to the `id` attribute |
| `5-unique_id.sql` | Adds a `UNIQUE` constraint on `id` |
| `6-states.sql` | Creates the `states` table |
| `7-cities.sql` | Creates the `cities` table with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Lists cities of California using a subquery |
| `9-cities_by_state_join.sql` | Lists all cities using a `JOIN` with `states` |
| `10-genre_id_by_show.sql` | Lists shows with at least one genre, sorted by show and genre ID |
| `11-genre_id_all_shows.sql` | Lists all shows and their genre IDs (including shows with no genre) using a `LEFT JOIN` |
| `12-no_genre.sql` | Lists shows without a genre |
| `13-count_shows_by_genre.sql` | Lists all genres with the number of shows linked to each |
| `14-my_genres.sql` | Lists all genres of the show `Dexter` |
| `15-comedy_only.sql` | Lists all shows linked to the genre `Comedy` |
| `16-shows_by_genre.sql` | Lists all shows with their genres |
| `17-not_a_comedy.sql` | Lists all shows without the genre `Comedy` |
| `18-nothing_at_night.sql` | Lists all shows without the genre `Comedy`, ordered without duplicates |
| `19-my_rating.sql` | Lists shows sorted by rating |
| `20-genre_id_by_show.sql` | Lists the genre with the most shows |
| `SQL_101.md` | Notes on how SQL database engines work internally |

## Author
**Rahaf Alabdalh [GitHub](https://github.com/RahafN1)
