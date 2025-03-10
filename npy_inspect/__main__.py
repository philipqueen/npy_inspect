import numpy as np
import typer

from pathlib import Path

app = typer.Typer()

@app.command()
def main(
    path: str,
):
    input_path = Path(path)
    if not Path(input_path).exists():
        typer.echo(f"File {input_path} does not exist.")
        raise typer.Exit(code = 1)
    
    if not input_path.is_file():
        typer.echo(f"{input_path} is not a file.")
        raise typer.Exit(code = 1)  
    
    if not input_path.suffix == ".npy":
        typer.echo(f"{input_path} is not a .npy file.")
        raise typer.Exit(code = 1)

    array = np.load(path, allow_pickle=True)

    typer.echo(f"\nFile: {input_path}\n")

    typer.echo(f"Shape: {array.shape}")
    typer.echo(f"Size: {array.size}")
    typer.echo(f"Data type: {array.dtype}")
    typer.echo(f"File size: {(input_path.stat().st_size / 1024):.2f} KB")
    typer.echo(f"NaN count: {np.isnan(array).sum()}")

    # TODO: display array in table with rich

    raise typer.Exit(code = 0)

if __name__ == "__main__":
    app()