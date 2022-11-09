=======
VICIBOX PYTHON WRAPPER
=======

   
Introduction
============

This is Python implementation of wrapper for Vicibox API.


Getting Started
===============

Installation
------------

Install Vicibox Python wrapper like this:

.. code-block:: bash

    pip install py-vicibox


How Does it Work?
-----------------

In order to use Python vicibox wrapper firstly have to decide which type of API you want to use.
Then for instance with the use of:

.. code-block:: python

    async def call_non_agent_api(base_url: str, function_and_values_dict: dict) -> dict:
        if 'function' in function_and_values_dict:
            if function_and_values_dict['function'] in non_agent_function_list:
                # Create target URL based on query params that was provided
                url = create_target_url(base_url, function_and_values_dict)

                # Make a request to Vicibox
                response = await make_request(url)
                return response
            raise HTTPException(400, 'Provided function is not accessible via non-agent API.')
        raise HTTPException(400, 'No function provided.')

You can call vicibox server. Remeber to provide valid base url with your Vicibox
IP address and credentials. Moreover  the second parameter should contain following keys:
- function - choose which function of Non-agent API you want to call,
- query params - enter all query parameters that are accessible using provided function.

License
=======

This project is licensed under the terms of the MIT license.
