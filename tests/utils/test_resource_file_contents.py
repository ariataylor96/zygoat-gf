from zygoat.utils import resource_file_contents


def test_resource_file_contents(tmp_path):
    contents = resource_file_contents("backend/Dockerfile.local")

    assert contents is not None
    assert type(contents) is bytes
