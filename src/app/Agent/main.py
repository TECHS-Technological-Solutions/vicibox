from fastapi.exceptions import HTTPException

from utils import make_request, create_target_url

agent_function_list = [
    'version',
    # shows version and build of the API, along with the date/time

    'webserver',
    # shows version and build of the API, along with the date/time

    'external_hangup',
    # Hangs up the current customer call on the agent screen
    #
    # VALUES: (value)
    # 1  - the only valid value for this function

    'external_status',
    # Sets the status of the current customer call on the agent dispotion screen
    #
    # VALUES: (value)
    # value -
    #  Any valid status in the VICIDIAL system will work for this function
    # callback_datetime -
    #  YYYY-MM-DD+HH:MM:SS, date and time of scheduled callback.
    #  REQUIRED if callback is set and status is flagged as a scheduled callback
    # callback_type -
    #  USERONLY or ANYONE, default is ANYONE
    # callback_comments -
    #  Optional comments to appear when the callback is called back, must be less than 200 characters in length
    # qm_dispo_code -
    #  Option callstatus code used if QM is enabled

    'external_pause',
    # Pauses or Resumes the agent. If a Pause and the agent is on a live call
    # will pause after the live call is dispositioned
    #
    # VALUES: (value)
    # PAUSE  - Pauses the agent session
    # RESUME  - Resumes the agent session

    'logout',
    # Logs the agent out of the agent interface. If the agent is on a live call,
    # will logout after the live call is dispositioned
    #
    # VALUES: (value)
    # LOGOUT  - Logout the agent session

    'external_dial',
    # Places a manual dial phone call on the agent screen, you can define whether to search for the lead in the
    # existing database or not, and you can define the phone_code and the number to dial.
    # This action will pause the agent after their current call, enter the information to place the call,
    # and dialing the call on the agent screen.
    # For required fields check external_dial field in documentation: http://vicidial.org/docs/AGENT_API.txt

    'preview_dial_action',
    # sends a SKIP, DIALONLY, ALTDIAL, ADR3DIAL or FINISH when a lead is being previewed or in Manual Alt Dial
    #
    # VALUES:
    # agent_user -
    #  REQUIRED alphanumeric string for active agent user
    #
    # value -
    #  One of the following actions (SKIP, DIALONLY, ALTDIAL, ADR3DIAL or FINISH)

    'external_add_lead',
    # Adds a lead in the manual dial list of the campaign for logged-in agent.
    # A much simplified add lead function compared to the Non-Agent API function
    # For required fields check external_add_lead field in documentation: http://vicidial.org/docs/AGENT_API.txt

    'change_ingroups',
    # This function will change the selected in-groups for an agent that is logged into a campaign that allows for
    # inbound calls to be handled. Allows the selected in-groups for an agent to be changed while they are
    # logged-in to the ViciDial Agent screen only. Once changed in this way, the agent would need to log out
    # and back in to be able to select in-groups themselves(If Agent Choose In-Groups is enabled for that user).
    # The blended checkbox can also be changed using this function. The API user performing this function must have
    # vicidial_users.change_agent_campaign = 1.
    # For required fields check change_ingroups field in documentation: http://vicidial.org/docs/AGENT_API.txt

    'update_fields',
    # Updates the fields that are specified with the values. This will update the data that is on the agent's
    # screen in the customer information section.
    # For required fields check update_fields field in documentation: http://vicidial.org/docs/AGENT_API.txt

    'set_timer_action',
    # Triggers specific agent screen actions after a set number of seconds, like the Webform,
    # a Transfer-Conf Preset call or a message to be displayed on the agent screen.
    #
    # VALUES:
    # agent_user -
    #  REQUIRED, alphanumeric string for agent user
    # value -
    #  REQUIRED, one of these choices: 'NONE','WEBFORM','WEBFORM2','D1_DIAL','D2_DIAL','D3_DIAL','D4_DIAL',
    #  'D5_DIAL','MESSAGE_ONLY'
    # notes -
    #  Optional, the message to be displayed with the timer action
    # rank -
    #  Optional, the number of seconds into the call to display

    'st_login_log',
    # Looks up the vicidial_users.custom_three field(as "agentId") to associate with a vicidial user ID.
    # If found it will populate the custom_four field with a "teamId" value, then output the vicidial user ID
    #
    # VALUES:
    # value -
    #  REQUIRED alphanumeric string for CRM AgentID
    # vendor_id -
    #  REQUIRED alphanumeric string for CRM TeamID

    'st_get_agent_active_lead',
    # Looks up the vicidial_users.custom_three field(as "agentId") to associate with a vicidial user ID.
    # If found it will output the active lead_id and phone number, vendor_lead_code, province,
    # security_phrase and source_id fields.
    #
    # VALUES:
    # value -
    #  REQUIRED alphanumeric string for CRM AgentID
    # vendor_id -
    #  REQUIRED alphanumeric string for CRM TeamID

    'ra_call_control',
    # Allows for remote agent call control: hangup/transfer calls being handled by remote agents,
    # also options for logging a disposition and call length
    # For required fields check ra_call_control field in documentation: http://vicidial.org/docs/AGENT_API.txt

    'send_dtmf',
    # Sends dtmf signal string to agent's session
    #
    # VALUES: (value)
    # only valid DTMF characters with these replacements:
    #   P = # (pound or hash)
    #   S = * (star)
    #   Q = (one second of silence)

    'park_call',
    # sends command to park customer or grab customer out of park
    #
    # VALUES:
    #  value -
    #   REQUIRED, choices are below
    #    PARK_CUSTOMER - send customer to the park extension as defined in the campaign the agent is logged into
    #    GRAB_CUSTOMER - grab customer from the park extension and send them to the agent session
    #    PARK_IVR_CUSTOMER - send customer to the park ivr as defined in the campaign the agent is logged into,
    #    customer will come back after finishing IVR
    #    GRAB_IVR_CUSTOMER - grab customer from the park ivr and send them to the agent session

    'transfer_conference',
    # sends several commands related to the agent transfer-conf frame
    # For required fields check transfer_conference field in documentation: http://vicidial.org/docs/AGENT_API.txt

    'recording',
    # sends a recording start/stop signal or status of agent recording
    #
    # VALUES:
    #  value -
    #   REQUIRED, choices are below
    #    START - sends a "start recording" signal to the agent screen
    #             (you can have multiple recordings going at the same time)
    #    STOP - sends a "stop recording" signal to the agent screen
    #             (this will stop all active recordings onthe agent screen)
    #    STATUS - displays results of active recording and agent session information
    #             (returns: user|recording_id|filename|server|start_time|agent_server|session|agent_status)
    #   stage -
    #     OPTIONAL, value to append to the recording filename, limited to 14 characters, if more it will truncate.
    #     Only works with START value

    'webphone_url',
    # display or launch the webphone url for the current agent's session
    #
    # VALUES:
    #  value -
    #   REQUIRED, choices are below:
    #    DISPLAY - displays only the URL for the webphone if enabled
    #    LAUNCH - redirects the url to the webphone url to launch it

    'call_agent',
    # send a call to connect the agent to their session
    #
    # VALUES:
    #  value -
    #   REQUIRED, choices are below:
    #    CALL - places call from the agent session to the agent's phone

    'audio_playback',
    # Basic play/stop/pause/resume/restart audio in agent session
    #
    # NOTE: PAUSE/RESUME/RESTART features only work with Asterisk 1.8 and higher
    #        (In Asterisk versions earlier than 1.8 you can replicate RESTART using PLAY and dial_override=Y)
    #
    # VALUES:
    #  stage -
    #   REQUIRED, choices are below:
    #    PLAY - starts playing of new audio file in agent session
    #    STOP - kills playback of audio in agent session
    #    PAUSE - pauses playing of audio
    #    RESUME - resumes playing of audio after pause
    #    RESTART - restarts playback at beginning of audio
    #  value -
    #   REQUIRED for stage of 'PLAY', name of audio file in audio store to play, must NOT have extension
    #  dial_override -
    #   OPTIONAL, (Y or N), default is N. Allows you to PLAY without issuing a STOP to a currently playing audio file

    'switch_lead',
    # For agents on a live inbound call, switches lead_id of live inbound call on agent screen including associated
    # logs. You can define a lead_id or a vendor_lead_code to switch to. Works like the SELECT function of the
    # LEAD SEARCH feature in the agent screen.
    #
    # VALUES:
    # lead_id -
    #  Any valid lead_id from the system(either lead_id or vendor_lead_code are required) if both are defined,
    #  lead_id will override vendor_lead_code
    # vendor_lead_code -
    #  OPTIONAL, any valid Vendor lead code

    'vm_message',
    # IMPORTANT NOTES:
    # - Set the campaign "Answering Machine Message" setting to 'LTTagent' for this to work.
    # - There are some other campaign settings that can override this function, so you will want to disable
    # 'AM Message Wildcards' and 'VM Message Groups'.
    #
    # DESCRIPTION:
    # Set a custom voicemail message to be played when agent clicks the VM button on the agent screen
    #
    # VALUES:
    # value -
    #  REQUIRED, One audio file or multiple audio files(separated by pipes) to play when the call is sent to
    #  VM by the agent
    # lead_id -
    #  OPTIONAL, The lead_id of the call that the agent is currently on, if populated it will validate that
    #  is the lead the agent is talking to

    'pause_code',
    # set a pause code for an agent that is paused
    #
    # VALUES:
    #  value - pause code to set, must be 6 characters or less

    'calls_in_queue_count',
    # display a count of the calls waiting in queue for the specific agent
    #
    # VALUES:
    #  value -
    #   REQUIRED, choices are below:
    #    DISPLAY - displays number of calls in queue that could be sent to this agent

    'force_fronter_leave_3way',
    # will send a command to fronter agent to leave-3way call that executing agent is on.
    # Will not execute command for the named 'agent_user', but will look for oldest other user currently
    # on a call with the same lead_id that the named agent_user is on the phone with.
    #
    # VALUES:
    #  value -
    #   REQUIRED, choices are below:
    #    LOCAL_ONLY - looks for fronter only on local cluster
    #    LOCAL_AND_CCC - looks on local cluster and remote CCC to send command to (will always check local first)
    #    CCC_REMOTE - use this when the closer is not on this cluster
    #   lead_id -
    #     OPTIONAL, only to be used with CCC_REMOTE value commands

    'force_fronter_audio_stop',
    # will send a command to fronter agent session to stop any audio_playback playing on it.
    # Will not execute command for the named 'agent_user', but will look for other user session currently
    # on a call with the same lead_id that the named agent_user is on the phone with.
    #
    # VALUES:
    #  value -
    #   REQUIRED, choices are below:
    #    LOCAL_ONLY - looks for fronter only on local cluster
    #    LOCAL_AND_CCC - looks on local cluster and remote CCC to send command to (will always check local first)
    #    CCC_REMOTE - use this when the closer is not on this cluster
    #   lead_id -
    #     OPTIONAL, only to be used with CCC_REMOTE value commands
]


async def call_agent_api(base_agent_url: str, function_and_values_dict: dict) -> dict:
    if 'function' in function_and_values_dict:
        if function_and_values_dict['function'] in agent_function_list:
            # Create target URL based on query params that was provided
            url = create_target_url(base_agent_url, function_and_values_dict)

            # Make a request to Vicibox
            response = await make_request(url)
            return response
        raise HTTPException(400, 'Provided function is not accessible via non-agent API.')
    raise HTTPException(400, 'No function provided.')
