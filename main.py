import click

@click.command()
@click.argument('zip1')
@click.argument('zip2')
@click.argument('mod', type=click.INT)
def sample(zip1, zip2, mod):
    print("zip1:", zip1)
    print("zip2:", zip2)
    print("mod:", mod)
    # TODO: finish this

@click.group()
def commands():
    pass

commands.add_command(sample)

if __name__ == "__main__":
    commands()