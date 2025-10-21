from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:Qsdr64@localhost:5432/SQL"

engine = create_engine(DATABASE_URL)

def test_add_subject():

    with engine.connect() as connection:

        connection.execute(

            text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),

            {"id": 100, "title": "Mathematics"}

        )

        result = connection.execute(

            text("SELECT subject_title FROM subject WHERE subject_id = :id"),

            {"id": 100}

        ).fetchone()

        assert result[0] == "Mathematics"

        connection.execute(
            text("delete from subject where subject_id = :id"),
            {"id": 100}
        )

def test_update_subject():

    with engine.connect() as connection:

        connection.execute(

            text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),

            {"id": 100, "title": "Mathematics"}

        )

        connection.execute(

            text("UPDATE subject set subject_title =:title where subject_id =:id"),

            {"title": 'new_title', "id": 100}

        )
        result = connection.execute(
            text("select * from subject where subject_id =:id"),
            {"id": 100}
        ).fetchone()

        assert result[1] == "new_title"

        connection.execute(
            text("delete from subject where subject_id = :id"),
            {"id": 100}
        )

def test_delete_subject():

    with engine.connect() as connection:

        connection.execute(

            text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),

            {"id": 100, "title": "Mathematics"}

        )

        result = connection.execute(

            text("SELECT subject_title FROM subject WHERE subject_id = :id"),

            {"id": 100}

        ).fetchone()

        assert result[0] == "Mathematics"

        connection.execute(
            text("delete from subject where subject_id = :id"),
            {"id": 100}
        )

        result = connection.execute(

            text("SELECT subject_title FROM subject WHERE subject_id = :id"),

            {"id": 100}

        ).fetchone()
        assert result is None


