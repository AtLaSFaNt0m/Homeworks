def hello():
    hello = 'Hello,'

    def world():
        world = 'World'
        Helloworld = hello + world
        print(Helloworld)

    world()


hello()
