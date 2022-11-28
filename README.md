# VICIBOX PYTHON WRAPPER

## Introduction
This is Python implementation of wrapper for Vicibox API.

## Getting Started


### Installation

Install Vicibox Python wrapper like this:

```bash
    pip install py-vicibox
```

### How Does it Work?


#### Non-agent

1. In order to use Python vicibox wrapper firstly you have to build base url based on your Vicidial server address:

```python
import os
from dotenv import load_dotenv

from py_vicibox.utils import create_base_non_agent_url

load_dotenv()
env = os.environ

VICIDIAL_SERVER_IP = env.get('VICIDIAL_SERVER_IP', '127.0.0.1')
VICIDIAL_SOURCE = env.get('VICIDIAL_SOURCE', 'test')
VICIDIAL_USER = env.get('VICIDIAL_USER', '6666')
VICIDIAL_PASSWORD = env.get('VICIDIAL_USER_PASSWORD', '1234')

non_agent_base_url = create_base_non_agent_url(
    VICIDIAL_SERVER_IP,
    VICIDIAL_SOURCE,
    VICIDIAL_USER,
    VICIDIAL_PASSWORD,
)
```

2. After successful creation of base non-agent url, one should prepare the dict of all necessary query parameters in accordance 
to the request function. In order to provide all necessary arguments you can use special provided pydantic schemas that were
created according to Vicidial documentation (sound_list function example):

```python
from py_vicibox.non_agent.schemas import SoundList

query_params = SoundList(format='selectframe', stage='date', comments='Test')
```

3. Then you will be able to call api using `call_non_agent_api` (**Remember that function in this library
are created using async**):

```python
import asyncio

from py_vicibox.non_agent.main import call_non_agent_api

asyncio.run(call_non_agent_api(non_agent_base_url, 'sound_list', query_params))    
```

#### Agent
The usage of agent api look basically the same as non-agent one, there is just one difference during creation
of `base_url`, you need to provide additional argument as agent user that you want to access (example code):

```python
from py_vicibox.utils import create_base_agent_url

from setting import VICIDIAL_SERVER_IP, VICIDIAL_SOURCE, VICIDIAL_USER, VICIDIAL_PASSWORD

base_agent_url = create_base_agent_url(VICIDIAL_SERVER_IP, VICIDIAL_SOURCE, VICIDIAL_USER, VICIDIAL_PASSWORD, 'Test_agent_user')
```
# License

This project is licensed under the terms of the MIT license.

# Docs:
- [Agent](https://github.com/masterfermin02/vicidial-api-wrapper/blob/main/docs/agent.md)
- [Admin](https://github.com/masterfermin02/vicidial-api-wrapper/blob/main/docs/admin.md)