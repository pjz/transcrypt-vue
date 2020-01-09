

def on_click():
    this.count += 1

initial_data = {
    'message': 'Hello Vue (from Python)!',
    'count': 0,
}

methods = {
    'onClick': on_click
}

app = __new__(Vue(dict(
    el='#app',
    data=initial_data,
    methods=methods,
)))


