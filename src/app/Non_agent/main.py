from non_agent_functions import non_agent_function_list

from utils import make_request, create_target_url
from exceptions import ViciboxFunctionDoesNotExist


async def call_non_agent_api(base_non_agent_url: str, function: str, function_and_values_dict: dict) -> dict:
    if function_and_values_dict['function'] in non_agent_function_list:
        # Create target URL based on query params that was provided
        url = create_target_url(base_non_agent_url, function, function_and_values_dict)

        # Make a request to Vicibox
        response = await make_request(url)
        return response
    raise ViciboxFunctionDoesNotExist(api_name='non-agent')
