from flask import Flask, request

Ukol1 = Flask('muj-server')
#moje_aplikace = Ukol1
#vysledky = todo

@Ukol1.route("/todo", methods=['DELETE'])
def todo():
    data = {
        "Place1": "Paris",
        "Place2": "Edinburgh",
        "Place3": "Budapest",
        "Place4": "London",
        "Place5": "Vaduz",
        "Place6": "Reykjavik",
    }
    misto = request.form.get("misto") #Získáme hodnotu z POST requestu
    mesto = request.form.get("mesto")
    print(request.args)
    return data

@Ukol1.route("/test", methods=['GET', 'POST'])
def test_post():
    if request.method == "POST":
        d = request.data.decode()
        print(d)
        return "byla použita metoda POST"
    else:
        return "byla použita metoda GET"

if __name__ == "__main__":
    Ukol1.run()

#@Ukol1.route("/testujeme-del", methods=["DELETE"])
    #resp = requests.delete('http://127.0.0.1:5000/todo')
    #print(resp.text)
#resp = requests.post("http://localhost:5000/todo", data="ukol1")
#requests.delete(...)
#resp = requests.delete(...)
