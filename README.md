# Wippy


Wippy is a Python package for generating interesting Work In Progress messages similar to the one 
found on [Rust Language](http://www.rust-lang.org) website

## Installation
From within the ```wippy``` directory run,
```
python setup.py install
```

## Usage

Wippy is drop dead simple. Just import the method 'wippyfy' and you're good to go!

```python

from wippy import wippyfy

# Default usage
wippyfy()
# Output: 'This project is a work in progress and may do anything it likes up to and including swallowing your boss'

wippyfy()
# Output: 'This project is a work in progress and may do anything it likes up to and including stabbing your pet frog'

wippyfy()
# Output: 'This project is a work in progress and may do anything it likes up to and including whipping your users'

# Custom project name (default='This project')
wippyfy(name='Wippy')
# Output: 'Wippy is a work in progress and may do anything it likes up to and including vacuuming your smartphone'

wippyfy(name='Wippy')
# Output: 'Wippy is a work in progress and may do anything it likes up to and including losing your pet parrot'
```

## Contributing

Welcome aboard! Here are a few ways you can help:

- Report bugs or Suggest features on the [Issue List](https://github.com/ankitjavalkar/wippy/issues)
- Fix bugs, Add features and submit [pull requests](https://github.com/ankitjavalkar/wippy/pulls)
- Improve or Fix documentation

## Disclaimer

Wippy is a work in progress and may do anything it likes upto and including burying your sink.