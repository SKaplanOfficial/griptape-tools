import pytest
from gptscripter.tools import WebSearch
from tests.utils import install_requirements


@pytest.mark.usefixtures("install_requirements")
class TestWebSearch:
    @pytest.fixture(scope="class")
    def install_requirements(request):
        install_requirements("web_search")

    def test_search(self):
        assert isinstance(WebSearch().search(b"foo bar"), dict)
        