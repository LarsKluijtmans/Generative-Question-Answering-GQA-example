# Workflows

## Linting

```commandline
pylint --rcfile=.pylintrc $(git ls-files '*.py')
```

## Formatting

```commandline
black --check $(git ls-files '*.py')
```
