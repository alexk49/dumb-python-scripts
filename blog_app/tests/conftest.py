import os
import tempfile

import pytest

from blog.models import Article

# pytest fixtures are executed before each test
# they are usually stored in the conftest file


@pytest.fixture(autouse=True)
def database():
    _, file_name = tempfile.mkstemp()
    os.environ["DATABASE_NAME"] = file_name
    Article.create_table(database_name=file_name)
    yield
    os.unlink(file_name)

@pytest.fixture
def some_fixture():
    # do something before test
    yield # test runs here
    # do something after your test
