from utils import make_request


async def version(vicibox_server_ip: str) -> dict:
    """
    shows version and build of the API, along with the date/time and timezone

    :param vicibox_server_ip:
    :return:
    """
    url = f'http://{vicibox_server_ip}/vicidial/non_agent_api.php?function=version'
    version_response = await make_request(url)
    return version_response


async def sounds_list(base_url: str, format: str = None, stage: str = None, comments: str = None) -> dict:
    """
    outputs a list of audio files from the audio store

    :param base_url:
    :param format:
    :param stage:
    :param comments:
    :return:
    """
    function_url = 'function=sounds_list'

    # Check if optional fields are present and add them to function url
    if format:
        function_url += f'&format={format}'
    if stage:
        function_url += f'&format={stage}'
    if comments:
        function_url += f'&format={comments}'

    sounds_list_response = await make_request(f'{base_url}&{function_url}')
    return sounds_list_response


async def moh_list(base_url: str, format: str = None, comments: str = None) -> dict:
    """
    outputs a list of music on hold classes in the system

    :param base_url:
    :param format:
    :param comments:
    :return:
    """
    function_url = 'function=moh_list'

    # Check if optional fields are present and add them to function url
    if format:
        function_url += f'&format={format}'
    if comments:
        function_url += f'&format={comments}'

    moh_list_response = await make_request(f'{base_url}&{function_url}')
    return moh_list_response


async def vm_list(base_url: str, format: str = None, comments: str = None) -> dict:
    """
    outputs a list of voicemail boxes in the system

    :param base_url:
    :param format:
    :param comments:
    :return:
    """
    function_url = 'function=vm_list'

    # Check if optional fields are present and add them to function url
    if format:
        function_url += f'&format={format}'
    if comments:
        function_url += f'&format={comments}'

    vm_list_response = await make_request(f'{base_url}&{function_url}')
    return vm_list_response


async def blind_monitor(base_url: str, phone_login: str, session_id: int,
                        server_ip: str, source: str, stage: str) -> dict:
    """
    calls user-defined phone and places them in session as blind monitor

    :param base_url:
    :param phone_login:
    :param session_id:
    :param server_ip:
    :param source:
    :param stage:
    :return:
    """

    function_url = f'function=blind_monitor&phone_login={phone_login}&session_id={session_id}&server_ip={server_ip}&' \
                   f'source={source}&stage={stage}'

    blind_monitor_response = await make_request(f'{base_url}&{function_url}')
    return blind_monitor_response
