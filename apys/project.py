import json, os

from apys import config

##
# CONSTANTS
#

_README = """# MY PROJECT

My project description

## LANGUAGE
[Python >= 3.4.2](https://docs.python.org/3/)

## LIBRARIES
* [apys](https://github.com/seijihirao/apys) - Backend restful framework

---

## RUNNING

```
$ apys -s
```

## TESTING

```
$ apys -t
```
"""

##
# FUNCTIONS
#

def init():
    """
    Initiate project folders with sample config and readme
    """

    #folders
    dirs = [
        settings.DIR_CONFIG,
        settings.DIR_ENDPOINTS,
        settings.DIR_UTILS
    ]
    _createDirs(dirs)

    #configs
    _writeConfigFile(settings.DEFAULT_PROD_NAME, {
        'server': {
            'port': settings.DEFAULT_PROD_PORT,
            'cors': settings.DEFAULT_PROD_CORS
        },
        'log': {
            'file': {
                'debug': os.path.joint(settings.DEFAULT_PROD_LOG_DIR, settings.DEFAULT_PROD_LOG_DEBUG_FILE),
                'debug': os.path.joint(settings.DEFAULT_PROD_LOG_DIR, settings.DEFAULT_PROD_LOG_ERROR_FILE)
            },
            'color': settings.DEFAULT_PROD_COLOR
        }
    })

    _writeConfigFile(settings.DEFAULT_DEV_NAME, {
        'server': {
            'port': settings.DEFAULT_DEV_PORT,
            'cors': settings.DEFAULT_DEV_CORS
        }
    })

    #readme
    with open(os.path.join('.', 'README.md'), 'w') as outfile:
        outfile.write(_README)
    
def _createDirs(directories):
    for directory in directories:
        if not os.path.exists(os.path.join('.', directory)):
            os.makedirs(directory)

def _writeConfigFile(file, obj):
    with open(os.path.join('.', settings.DIR_CONFIG, '{}.json'.format(file)), 'w') as outfile:
        json.dump(obj, outfile, indent=4)
