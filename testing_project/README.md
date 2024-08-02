# test project

Followed along from:

https://testdriven.io/blog/modern-tdd/

Project structure:

```
├── sum
│   ├── __init__.py
│   └── another_sum.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── pytest.ini
    └── test_sum
        ├── __init__.py
        └── test_another_sum.py
```

With sum being a folder for the main module.

Keeping your tests together in single package allows you to:

    Reuse pytest configuration across all tests
    Reuse fixtures across all tests
    Simplify the running of tests

You can run all the tests with this command:

```
(venv)$ python -m pytest tests
```
