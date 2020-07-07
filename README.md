# pycachecleaner
smol thing to kill \_\_pycache\_\_.<br/>
(you can use python -B ... in future)

# installation
>   $ pip install https://github.com/mikk357/pycachecleaner --upgrade

# usage
you should be in the directory you want to clean up.
>   $ python -m pycachecleaner

or in code
```python
import pycachecleaner


directory: str = "you/path/there"
pycachecleaner.clean(directory, autoagree=True)
```

please be careful, and write issues QwQ
