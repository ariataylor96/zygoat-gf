from typing import Union
import os


def inject_file_contents(
    name: Union[str, os.PathLike],
    contents: Union[str, bytes],
    overwrite: bool = False,
) -> None:
    """
    Directly writes the contents of a file. Useful for data not easily manipulated via Python, but shouldn't be the first resort for configuration changes.

    :param name: Path to the file to write
    :param contents: Data to write to the file,
    :param overwrite: Overwrite existing files
    """

    if os.path.isfile(name) and not overwrite:
        raise FileExistsError(
            f"{name} already exists in the filesystem and overwrite is not specified"
        )

    # Normalize content type to bytes
    if type(contents) is str:
        contents = contents.encode()

    with open(name, "wb") as f:
        f.write(contents)
