from inspect import signature


def clip(text: str, max_len:'int > 0' = 80) -> str:
    """Retorna o texto cortado no último espaço antes ou depois do max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    
    if end is None:
        end = len(text)
    
    return text[:end].rstrip()


print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)
print(clip.__annotations__)

print()

sig = signature(clip)
print(sig)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)


print(sig.return_annotation)

for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)
