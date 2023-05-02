import sqlite3


def main():
    try:
        db = sqlite3.connect("Pets.db")
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Owners (OwnerID INTEGER PRIMARY KEY NOT NULL, OwnerName TEXT, 
        OwnerPhone TEXT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Pets (PetID INTEGER PRIMARY KEY NOT NULL, PetName TEXT, PetType 
        TEXT, PetBreed TEXT, OwnerID INTEGER, FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID))""")
        owners_file = open("Owners.txt", "r")
        pets_file = open("Pets.txt", "r")


        for line in owners_file:
            data = line.strip().split(",")  # Split line into list
            cursor.execute("INSERT INTO Owners VALUES(?, ?, ?)", (None, data[0], data[1]))

        for line in pets_file:
            data = line.strip().split(",")
            cursor.execute("INSERT INTO Pets Values(?, ?, ?, ?, ?)", (None, data[0], data[1], data[2], data[3]))

            db.commit()
            cursor.execute("SELECT * FROM Owners")
            owners = cursor.fetchall()

            for owner in owners:
                print(f"{owner[1]}      {owner[2]}")
                cursor.execute("SELECT * FROM Pets WHERE OwnerID=?", (owner[0],))

                for pets in cursor.fetchall():
                    print(f".......{pets[1]} is a {pets[3]} {pets[2]}")
                print()


    except sqlite3.Error as err:
        print("%SQL error encountered.", err)


main()
