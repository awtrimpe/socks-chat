import pytest

from app.main.helpers import svg_contents


def describe_svg_contents():
    def test_good_link():
        assert type(svg_contents('./app/static/socks.svg')) is str

    def test_bad_link():
        with pytest.raises(FileNotFoundError) as expt:
            svg_contents('./app/static/bad_link_to.svg')
        assert str(
            expt.value) == "[Errno 2] No such file or directory: './app/static/bad_link_to.svg'"
