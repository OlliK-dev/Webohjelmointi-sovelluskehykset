
# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

""" Mikä tässä koodissa on vikana?

Jos tätä arvoidaan vain sillä perusteella, toimiiko kaikki, 
niin koodissa ei ole mitään vikaa, koska kaikki ominaisuudet
toimivat oikein

Arkkitehtuurin näkökulmasta koodi on aivan käyttökelvotonta.

Tehdään tämä seuraavaksi käyttäen MVC:tä.

"""
import sqlite3

# Tätä funktiota käytetään kahdessa routehandlerissa.
def get_user_by_id(con, _id):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (_id,))
    user = cursor.fetchone()
    cursor.close()
    return user

# Hakee kaikki käyttäjät JSON-muodossa
@app.route('/api/users', methods=['GET'])
def get_all_users_handler():
    try:
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            cur.close()
            users_list = []
            for user in users:
                users_list.append({'id': user[0], 'first_name': user[1], 'last_name': user[2], 'username': user[3]})
            return jsonify(users_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Lisää uuden käyttäjän request data oltava json-muodossa
# Voit käyttää tähän vaikka Postmania tms. vastaavaa Rest Clientiä
@app.route('/api/users', methods=['POST'])
def add_user_handler():
    try:
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cur = con.cursor()
            request_data = request.get_json()
            cur.execute("INSERT INTO users(first_name, last_name, username) VALUES(?, ?, ?)",
                        (request_data.get('first_name'), request_data.get('last_name'), request_data.get('username')))
            con.commit()
            cur.close()
            return jsonify({'id': cur.lastrowid, 'first_name': request_data.get('first_name'),
                            'last_name': request_data.get('last_name'), 'username': request_data.get('username')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Hakee käyttäjän id:n perusteella
@app.route('/api/users/<_id>', methods=['GET'])
def get_user_by_id_handler(_id):
    try:
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            user = get_user_by_id(con, _id)
            if user is None:
                return jsonify({'error': 'user not found'}), 404
            return jsonify({'id': user[0], 'first_name': user[1], 'last_name': user[2], 'username': user[3]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Muokkaa id:n mukaan valitun käyttäjän tietoja
# request data lähetettävä JSON-muodossa
@app.route('/api/users/<_id>', methods=['PUT', 'PATCH'])
def update_user_by_id_handler(_id):
    try:
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            user = get_user_by_id(con, _id)
            if user is None:
                return jsonify({'error': 'user not found'}), 404
            request_data = request.get_json()

            new_first_name = request_data.get('first_name', user[1])
            new_last_name = request_data.get('last_name', user[2])
            new_username = request_data.get('username', user[3])
            cur = con.cursor()
            cur.execute("UPDATE users SET first_name = ?, last_name = ?, username = ?  WHERE id = ?",
                        (new_first_name, new_last_name, new_username, _id))
            con.commit()
            cur.close()

            return jsonify(
                {'id': user[0], 'first_name': new_first_name, 'last_name': new_last_name, 'username': new_username})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Käyttäjän poisto id:n perusteella
@app.route('/api/users/<_id>', methods=['DELETE'])
def delete_user_by_id_handler(_id):
    try:
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE id = ?", (_id,))
            con.commit()
            row_count = cur.rowcount
            cur.close()
            if row_count == 0:
                return jsonify({'error': 'user not found'}), 404
            return ""
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run()