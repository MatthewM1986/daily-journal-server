import sqlite3
import json
from models import Entry


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyJournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM entry e
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['date'], row['mood_id'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect("./dailyJournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM entry e
        WHERE e.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['concept'], data['entry'],
                      data['date'], data['mood_id'])

    return json.dumps(entry.__dict__)


def create_entry(entry):
    # Get the id value of the last entry in the list
    max_id = ENTRIES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    entry["id"] = new_id

    # Add the animal dictionary to the list
    ENTRIES.append(entry)

    # Return the dictionary with `id` property added
    return entry


def delete_entry(id):
    with sqlite3.connect("./dailyJournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))


def update_entry(id, new_entry):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, entry in enumerate(ENTRIES):
        if entry["id"] == id:
            # Found the animal. Update the value.
            ENTRIES[index] = new_entry
            break
