#
# Actions to perform after cookie cutter installs the repo
#


def replace_content(filename, what, replacement):
    with open(filename) as fh:
        content = fh.read()
    with open(filename, 'w') as fh:
        fh.write(content.replace(what, replacement))


if __name__ == "__main__":
    print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:

{% for key, value in cookiecutter.items()|sort %}{% if key != '_template' %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endif %}{%- endfor %}

################################################################################

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        docker-compose build base --pull
        docker-compose build
        docker-compose up
""")
