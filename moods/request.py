import sqlite3
import json
from models import Mood


def get_all_moods():
    # Open a connection to the database
    with sqlite3.connect("./dailyJournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM mood m
        """)

        # Initialize an empty list to hold all animal representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            mood = Mood(row['id'], row['label'])

            moods.append(mood.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(moods)


def get_single_mood(id):
    with sqlite3.connect("./dailyJournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM mood m
        WHERE m.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        mood = Mood(row['id'], row['label'])

    return json.dumps(mood.__dict__)


def create_mood(mood):
    # Get the id value of the last mood in the list
    max_id = MOODS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    mood["id"] = new_id

    # Add the animal dictionary to the list
    MOODS.append(mood)

    # Return the dictionary with `id` property added
    return mood


def delete_mood(id):
    with sqlite3.connect("./dailyJournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM mood
        WHERE id = ?
        """, (id, ))


def update_mood(id, new_mood):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, mood in enumerate(MOODS):
        if mood["id"] == id:
            # Found the animal. Update the value.
            MOODS[index] = new_mood
            break
