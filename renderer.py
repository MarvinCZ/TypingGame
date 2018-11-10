def text_objects(font, text, color, text_center):
    rendered = font.render(text, True, color)
    return rendered, rendered.get_rect(center=text_center)


def render_health_bar():
    raise NotImplemented


def render_words():
    raise NotImplemented
