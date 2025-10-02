from flask import Flask, render_template

# Inicijalizacija Flask aplikacije
app = Flask(__name__)

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# Definicija ruta (URL putanja) i pripadajucih view funkcija
@app.route("/")
def index():
    prod = ["Mlijeko", "Kruh", "Sir"]
    s1 = Student("Ante", "Stipić")
    return render_template("index.html", title="Zadar", student=s1, products=prod)

@app.route("/about")
def about():
    return render_template("about.html", title="O nama")

# Pokretanje aplikacije samo ako se izvrsava direktno (ne pri importu)
if __name__ == "__main__":
    app.run(debug=True)  # Pokretanje razvojnog (dev) servera s debug nacinom rada