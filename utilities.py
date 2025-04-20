from dotenv import load_dotenv

class Utilities():
    load_dotenv(".env")

    guildID = 852403894101082143
    eventGuildID = 1222254865795907704

class Acolyte:
    def __init__(self, user_id, exp=0, lvl=0, characters=None):
        self.user_id = user_id  # Klucz główny
        self.exp = exp
        self.lvl = lvl
        self.characters = characters if characters is not None else []

    def add_character(self, cursor, character_name):
        if character_name not in self.characters:
            self.characters.append(character_name)
            cursor.execute('''
            INSERT INTO Characters (acolyte_id, character_name)
            VALUES (?, ?)
            ''', (self.user_id, character_name))
        else:
            print(f"Postać {character_name} już istnieje w liście postaci Acolyte.")

    def remove_character(self, cursor, character_name):
        if character_name in self.characters:
            self.characters.remove(character_name)
            cursor.execute('''
            DELETE FROM Characters
            WHERE acolyte_id = ? AND character_name = ?
            ''', (self.user_id, character_name))
        else:
            print(f"Postać {character_name} nie istnieje w liście postaci Acolyte.")

    def save_to_db(self, cursor):
        cursor.execute('''
        INSERT OR REPLACE INTO Acolyte (user_id, exp, lvl)
        VALUES (?, ?, ?)
        ''', (self.user_id, self.exp, self.lvl))

    @classmethod
    def load_from_db(cls, cursor, user_id):
        cursor.execute('SELECT exp, lvl FROM Acolyte WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        if not result:
            return None

        exp, lvl = result
        cursor.execute('SELECT character_name FROM Characters WHERE acolyte_id = ?', (user_id,))
        characters = [row[0] for row in cursor.fetchall()]
        return cls(user_id, exp, lvl, characters)