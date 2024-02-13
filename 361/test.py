from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_navigation import Navigation

app = Flask(__name__, static_url_path='/static')
#nav = Navigation(app)




# Predefined lists for weapons and styles
weapons_list = ["Sword", "Axe", "Bow", "Staff", "Dagger", "Hammer", "Crossbow", "Katana", "Spear", "Greatsword"]
styles_list = ["Aggressive", "Defensive", "Balanced", "Ranged", "Dual Wielding", "Stealthy", "Magic User", "Brute Force", "Tactical", "Swift"]

# List to store party members
party_members = []


#

# Route to display the form for creating a party member
@app.route('/index')
def index():
    return render_template('create_party_member.html', weapons=weapons_list, styles=styles_list, party=party_members)

# Route to handle the form submission
@app.route('/create_party_member', methods=['POST'])
def create_party_member():





    # Get user input for name, weapon, and style

    name = request.form['name']
    weapon = request.form['weapon']
    style = request.form['style']
    id_number = len(party_members) + 1

    if id_number > 5:

        return redirect(url_for('index'))

    # Add the new party member to the list
    party_members.append({
        'id': id_number,
        "name": name,
         "weapon": weapon,
         "style": style
    })
    print(party_members[id_number-1]['id'])
    return redirect(url_for('index'))

@app.route('/delete_party_member', methods=['POST'])
def delete_party_member():
    if request.method == 'POST':
        member_id = int(request.form.get('member_id'))
        # Implement your logic to delete the party member from the data
        # In a real application, this might involve interacting with a database
        # For now, let's assume party is a global list containing party members
        for member in party_members:
            if member['id'] == member_id:
                party_members.remove(member)
                break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

