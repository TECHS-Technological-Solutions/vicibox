from enum import Enum


class CallbackType(str, Enum):
    user_only = 'USERONLY'
    anyone = 'ANYONE'


class ExternalPauseValue(str, Enum):
    pause = 'PAUSE'
    resume = 'RESUME'


class ExternalLogout(str, Enum):
    logout = 'LOGOUT'


class PreviewDialActionValues(str, Enum):
    skip = 'SKIP'
    dial_only = 'DIALONLY'
    alt_dial = 'ALTDIAL'
    adr_3_dial = 'ADR3DIAL'
    finish = 'FINISH'


class ChangeIngroupsValues(str, Enum):
    change = 'CHANGE'
    remove = 'REMOVE'
    add = 'ADD'


class SetTimerActionValues(str, Enum):
    none = 'NONE'
    web_form = 'WEBFORM'
    web_form_2 = 'WEBFORM2'
    d1_dial = 'D1_DIAL'
    d2_dial = 'D2_DIAL'
    d3_dial = 'D3_DIAL'
    d4_dial = 'D4_DIAL'
    d5_dial = 'D5_DIAL'
    message_only = 'MESSAGE_ONLY'


class RACallControlStages(str, Enum):
    hangup = 'HANGUP'
    extension_transfer = 'EXTENSIONTRANSFER'
    ingroup_transfer = 'INGROUPTRANSFER'


class ParkCallValues(str, Enum):
    park_customer = 'PARK_CUSTOMER'
    grab_customer = 'GRAB_CUSTOMER'
    park_ivr_customer = 'PARK_IVR_CUSTOMER'
    grab_ivr_customer = 'GRAB_IVR_CUSTOMER'


class TransferConferenceValues(str, Enum):
    hangup_xfer = 'HANGUP_XFER'
    hangup_both = 'HANGUP_BOTH'
    blind_transfer = 'BLIND_TRANSFER'
    leave_vm = 'LEAVE_VM'
    local_closer = 'LOCAL_CLOSER'
    dial_wth_customer = 'DIAL_WITH_CUSTOMER'
    park_customer_dial = 'PARK_CUSTOMER_DIAL'
    leave_3way_call = 'LEAVE_3WAY_CALL'


class CIDChoices(str, Enum):
    campaign = 'CAMPAIGN'
    agent_phone = 'AGENT_PHONE'
    customer = 'CUSTOMER'
    custom_cid = 'CUSTOM_CID'


class RecordingValues(str, Enum):
    start = 'START'
    stop = 'STOP'
    status = 'STATUS'


class WebphoneURLValues(str, Enum):
    display = 'DISPLAY'
    launch = 'LAUNCH'


class CallAgentValues(str, Enum):
    call = 'CALL'


class AudioPlaybackStages(str, Enum):
    play = 'PLAY'
    stop = 'STOP'
    pause = 'PAUSE'
    resume = 'RESUME'
    restart = 'RESTART'


class CallsInQueueCountVales(str, Enum):
    display = 'DISPLAY'


class ForceFronterLeave3WayValues(str, Enum):
    local_only = 'LOCAL_ONLY'
    local_and_ccc = 'LOCAL_AND_CCC'
    ccc_remote = 'CCC_REMOTE'
