from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel, validator

from app.Agent import enums
from app.Non_agent.enums import ViciboxBoolean, Gender


class Version(BaseModel):
    pass


class Webserver(BaseModel):
    pass


class ExternalHangup(BaseModel):
    value: int


class ExternalStatus(BaseModel):
    value: int
    callback_datetime: Optional[datetime]
    callback_type: Optional[enums.CallbackType]
    callback_comments: Optional[str]
    qm_dispo_code: Optional[int]


class ExternalPause(BaseModel):
    value: enums.ExternalPauseValue


class Logout(BaseModel):
    value: enums.ExternalLogout


class ExternalDial(BaseModel):
    value: int
    lead_id: Optional[str]
    phone_code: int
    search: ViciboxBoolean
    preview: ViciboxBoolean
    focus: ViciboxBoolean
    vendor_id: Optional[str]
    dial_prefix: Optional[str]
    group_alias: Optional[str]
    vtiger_callback: Optional[ViciboxBoolean]
    alt_user: Optional[str]
    alt_dial: Optional[str]
    dial_ingroup: Optional[str]
    outbound_cid: Optional[str]


class PreviewDialAction(BaseModel):
    agent_user: str
    value: enums.PreviewDialActionValues


class ExternalAddLead(BaseModel):
    agent_user: str
    dnc_check: Optional[str]
    campaign_dnc_check: Optional[str]
    address1: Optional[str]
    address2: Optional[str]
    address3: Optional[str]
    alt_phone: Optional[int]
    city: Optional[str]
    comments: Optional[str]
    country_code: Optional[str]
    date_of_birth: Optional[date]
    email: Optional[str]
    first_name: Optional[str]
    gender: Optional[Gender]
    gmt_offset_now: Optional[float]
    last_name: Optional[str]
    middle_initial: Optional[str]
    phone_number: Optional[int]
    phone_code: Optional[int]
    postal_code: Optional[str]
    province: Optional[str]
    security_phrase: Optional[str]
    source_id: Optional[str]
    state: Optional[str]
    title: Optional[str]
    vendor_lead_code: Optional[int]
    rank: Optional[int]
    owner: Optional[str]


class ChangeIngroups(BaseModel):
    value: enums.ChangeIngroupsValues
    blended: ViciboxBoolean
    ingroup_choices: Optional[str]
    set_as_default: Optional[ViciboxBoolean]


class UpdateFields(BaseModel):
    agent_user: str
    address1: Optional[str]
    address2: Optional[str]
    address3: Optional[str]
    alt_phone: Optional[int]
    city: Optional[str]
    comments: Optional[str]
    country_code: Optional[str]
    date_of_birth: Optional[date]
    email: Optional[str]
    first_name: Optional[str]
    gender: Optional[Gender]
    gmt_offset_now: Optional[float]
    last_name: Optional[str]
    middle_initial: Optional[str]
    phone_number: Optional[int]
    phone_code: Optional[int]
    postal_code: Optional[str]
    province: Optional[str]
    security_phrase: Optional[str]
    source_id: Optional[str]
    state: Optional[str]
    title: Optional[str]
    vendor_lead_code: Optional[int]
    rank: Optional[int]
    owner: Optional[str]
    formreload: Optional[int]
    scriptreload: Optional[int]
    script2reload: Optional[int]
    emailreload: Optional[int]
    chatreload: Optional[int]


class SetTimerAction(BaseModel):
    agent_user: str
    value: enums.SetTimerActionValues
    notes: Optional[str]
    rank: Optional[int]


class StLoginLog(BaseModel):
    value: str
    vendor_id: str


class StGetAgentActiveLead(BaseModel):
    value: str
    vendor_id: str


class RACallControl(BaseModel):
    value: str
    agent_user: str
    stage: enums.RACallControlStages
    ingroup_choices: Optional[str]
    phone_number: Optional[int]
    status: Optional[str]

    @validator('ingroup_choices')
    def prevent_none_if_stage_is_ingroup_transfer(cls, v, values):
        if values['stage'] == enums.RACallControlStages.ingroup_transfer and v is None:
            raise ValueError('Value ingroup_choices should not be None if stage is set to INGROUPTRANSFER.')
        return v

    @validator('phone_number')
    def prevent_none_if_stage_is_extension_transfer(cls, v, values):
        if values['stage'] == enums.RACallControlStages.extension_transfer and v is None:
            raise ValueError('Value phone_number should not be None if stage is set to EXTENSIONTRANSFER.')
        return v


class SendDTMF(BaseModel):
    value: str


class ParkCall(BaseModel):
    value: enums.ParkCallValues


class TransferConference(BaseModel):
    value: enums.TransferConferenceValues
    phone_number: Optional[int]
    ingroup_choices: Optional[str]
    consultative: Optional[ViciboxBoolean]
    dial_override: Optional[ViciboxBoolean]
    group_alias: Optional[str]
    cid_choice: Optional[enums.CIDChoices]


class Recording(BaseModel):
    value: enums.RecordingValues
    stage: Optional[str]


class WebphoneURL(BaseModel):
    value: enums.WebphoneURLValues


class CallAgent(BaseModel):
    value: enums.CallAgentValues


class AudioPlayback(BaseModel):
    stage: enums.AudioPlaybackStages
    value: Optional[str]
    dial_override: Optional[ViciboxBoolean]

    @validator('value')
    def prevent_none_if_stage_is_play(cls, v, values):
        if values['stage'] == enums.AudioPlaybackStages.play and v is None:
            raise ValueError('Value of value field should not be None if stage is set to PLAY.')
        return v


class SwitchLead(BaseModel):
    lead_id: str
    vendor_lead_code: Optional[str]


class VMMessage(BaseModel):
    value: str
    lead_id: Optional[str]


class PauseCode(BaseModel):
    value: str


class CallsInQueueCount(BaseModel):
    value: enums.CallsInQueueCountVales


class ForceFronterLeave3Way(BaseModel):
    value: enums.ForceFronterLeave3WayValues
    lead_id: Optional[str]

    @validator('lead_id')
    def prevent_none_if_stage_is_ccc_remote(cls, v, values):
        if values['value'] == enums.AudioPlaybackStages.play and v is None:
            raise ValueError('Value of lead_id field should not be None if stage is set to CCC_REMOTE.')
        return v


class ForceFronterAudioStop(ForceFronterLeave3Way):
    pass


schemas_agent_dict = {
    'version': Version,
    'webserver': Webserver,
    'external_hangup': ExternalHangup,
    'external_status': ExternalStatus,
    'external_pause': ExternalPause,
    'logout': Logout,
    'external_dial': ExternalDial,
    'preview_dial_action': PreviewDialAction,
    'external_add_lead': ExternalAddLead,
    'change_ingroups': ChangeIngroups,
    'update_fields': UpdateFields,
    'set_timer_action': SetTimerAction,
    'st_login_log': StLoginLog,
    'st_get_agent_active_lead': StGetAgentActiveLead,
    'ra_call_control': RACallControl,
    'send_dtmf': SendDTMF,
    'park_call': ParkCall,
    'transfer_conference': TransferConference,
    'recording': Recording,
    'webphone_url': WebphoneURL,
    'call_agent': CallAgent,
    'audio_playback': AudioPlayback,
    'switch_lead': SwitchLead,
    'vm_message': VMMessage,
    'pause_code': PauseCode,
    'calls_in_queue_count': CallsInQueueCount,
    'force_fronter_leave_3way': ForceFronterLeave3Way,
    'force_fronter_audio_stop': ForceFronterAudioStop
}
