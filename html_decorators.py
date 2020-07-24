def div(func):
    def new_func(*args, **kwargs):
        content = '<div>'
        content += func(args)
        content += '</div>'
        return content
    return new_func


def article(func):
    def new_func(*args, **kwargs):
        content = '<article>'
        content += func(args)
        content += '</article>'
        return content
    return new_func


def p(func):
    def new_func(*args, **kwargs):
        content = '<p>'
        content += func(args)
        content += '</p>'
        return content
    return new_func


# Here you must apply the decorators, uncomment this later
# @div
# @article
# @p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
