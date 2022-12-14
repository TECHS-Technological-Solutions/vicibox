import httpx


def create_base_non_agent_url(vicibox_server_ip: str, vicibox_source: str, vicibox_user: str, vicibox_pass: str) -> str:
    non_agent_url = f'https://{vicibox_server_ip}/vicidial/non_agent_api.php?source={vicibox_source}&' \
                    f'user={vicibox_user}&pass={vicibox_pass}'
    return non_agent_url


def create_base_agent_url(vicibox_server_ip: str, vicibox_source: str, vicibox_user: str,
                          vicibox_pass: str, agent_user: str) -> str:
    agent_url = f'https://{vicibox_server_ip}/agc/api.php?source={vicibox_source}&user={vicibox_user}&' \
                f'pass={vicibox_pass}&agent_user={agent_user}'
    return agent_url


def create_target_url(base_url: str, function: str, dict_of_query_values: dict = None) -> str:
    base_url += f'&function={function}'
    for key, value in dict_of_query_values.items():
        base_url += f'&{key}={value}'
    return base_url


async def make_request(call_url: str) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        response = await client.get(call_url, timeout=15)
    return response
