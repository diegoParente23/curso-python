import inspect


def tag(name, *content, cls=None, **attrs):
    """Gera uma ou mais tags HTML"""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    
    return '<%s%s />' % (name, attr_str)


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img'))

my_tag = {
    'name': 'img', 
    'title': 'Sunset Boulevard', 
    'src': 'sunset.png', 
    'cls': 'framed'
}

print(tag(**my_tag))

print()

sig = inspect.signature(tag)
bound_args = sig.bind(**my_tag)

print(bound_args)

for name, value in bound_args.arguments.items():
    print(name, '=', value)
