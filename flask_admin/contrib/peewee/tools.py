def get_primary_key(model):
    return model._meta.primary_key.name


def parse_like_term(term):
    if term.startswith('^'):
        return '%s%%' % term[1:]
    elif term.startswith('='):
        return term[1:]
    else:
        return '%%%s%%' % term


def get_meta_fields(model):
    return (
        model._meta.sorted_fields
        if hasattr(model._meta, 'sorted_fields')
        else model._meta.get_fields()
    )
