# template_engine.py

def render_template(template, data):
    for key, value in data.items():
        placeholder = "{{" + key + "}}"
        template = template.replace(placeholder, str(value))
    return template


def main():
    template = """
    Hello {{name}},

    Welcome to {{platform}}.
    Your role is {{role}}.

    Regards,
    Team
    """

    data = {
        "name": "Ravi",
        "platform": "CS Labify",
        "role": "DevOps Engineer"
    }

    output = render_template(template, data)

    print(output)


main()
