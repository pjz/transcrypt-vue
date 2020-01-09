
#// 0. If using a module system (e.g. via vue-cli), import Vue and VueRouter
#// and then call `Vue.use(VueRouter)`.

#// 1. Define route components.
#// These can be imported from other files
Foo = dict(template='<div>foo</div>')
Bar = dict(template='<div>bar</div>')

#// 2. Define some routes
#// Each route should map to a component. The "component" can
#// either be an actual component constructor created via
#// `Vue.extend()`, or just a component options object.
#// We'll talk about nested routes later.
routes = [
  dict(path='/foo', component=Foo),
  dict(path='/bar', component=Bar)
]

#// 3. Create the router instance and pass the `routes` option
#// You can pass in additional options here, but let's
#// keep it simple for now.
router = __new__(VueRouter(dict(routes=routes)))

#// 4. Create and mount the root instance.
#// Make sure to inject the router with the router option to make the
#// whole app router-aware.
if not 'using pragma':
    app = __new__(Vue(dict(router=router)))['$mount']('#app')
else:
    # usually at the top of the file
    from org.transcrypt.stubs.browser import __pragma__
    __pragma__ ('alias', 'S', '$')
    # replacement 'prettier' line:
    app = __new__(Vue(dict(router=router))).S__mount('#app')

#// Now the app has started!

