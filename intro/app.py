


app = __new__(Vue({'el': '#app',
                   'data': {
                       'message': 'Hello Vue! (from python)'
                   }
                  }))


app2 = __new__(Vue({'el': '#app-2',
                    'data': {
                        'message': 'You loaded this page on ' + __new__(Date()).toLocaleString()
                    }
                   }))


def reverse_message():
    #this.message = this.message[::-1] # fails per https://github.com/QQuick/Transcrypt/issues/455
    #this.message = ''.join(list(this.message)[::-1])
    this.message = ''.join(reversed(list(this.message))) # works

app5 = __new__(Vue({'el': '#app-5',
  'data': {
    'message': 'Hello Vue.js!'
  },
  'methods': {
    'reverseMessage': reverse_message
  }
}))


app6 = __new__(Vue({'el': '#app-6',
                    'data': {
                        'message': 'Hello Vue! (from python)'
                    }
                   }))


Vue.component('todo-item', {
  'props': ['todo'],
  'template': '<li>{{ todo.text }}</li>'
})

app7 = __new__(Vue({'el': '#app-7',
                    'data': {
                      'groceryList': [
                        { 'id': 0, 'text': 'Vegetables' },
                        { 'id': 1, 'text': 'Cheese' },
                        { 'id': 2, 'text': 'Whatever else humans are supposed to eat' }
                      ]
                    }
                   }))

