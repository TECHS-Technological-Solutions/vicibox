from functions import non_agent_function_list
from app.Non_agent import schemas

from utils import make_request, create_target_url
from schema import RequestResponse
from exceptions import ViciboxFunctionDoesNotExist


async def call_non_agent_api(base_non_agent_url: str, function: str, query_params_dict: dict):
    if function in non_agent_function_list:
        # Apply validation schema based on provided function
        schemas.schemas_non_agent_dict[function](**query_params_dict)

        # Create target URL based on query params that was provided
        url = create_target_url(base_non_agent_url, function, query_params_dict)

        # Make a request to Vicibox
        response = await make_request(url)
        return RequestResponse(response_text=response.text)
    raise ViciboxFunctionDoesNotExist(api_name='non-agent')
