import psycopg

with psycopg.connect("postgres://postgres:postgres@localhost:5432/haemo_store") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM test")

        print(cur.fetchone())
