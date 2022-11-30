from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel

from app.nonAgent import enums


class Version(BaseModel):
    pass


class SoundList(BaseModel):
    format: Optional[enums.Format]
    stage: Optional[enums.SoundsListStage]
    comments: Optional[str]


class MOHList(BaseModel):
    format: Optional[enums.Format.select_frame]
    comments: Optional[str]


class VMList(BaseModel):
    format: Optional[enums.Format.select_frame]
    comments: Optional[str]


class BlindMonitor(BaseModel):
    phone_login: str
    session_id: int
    server_ip: str
    source: str
    stage: enums.BlindMonitorStage


class AgentIngroupInfo(BaseModel):
    agent_user: str
    source: str
    stage: enums.AgentIngroupInfoStage


class AgentCampaigns(BaseModel):
    agent_user: str
    source: str
    campaign_id: Optional[str]
    ignore_agentdirect: Optional[enums.ViciboxBoolean]
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]


class CampaignList(BaseModel):
    source: str
    campaign_id: Optional[str]
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]


class HopperList(BaseModel):
    source: str
    campaign_id: str
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]
    search_method: str


class RecordingLookup(BaseModel):
    agent_user: str
    lead_id: int
    date: date
    uniqueid: str
    extension: str
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]
    duration: Optional[enums.ViciboxBoolean]


class DidLogExport(BaseModel):
    phone_number: str
    date: date
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]


class PhoneNumberLog(BaseModel):
    phone_number: str
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]
    detail: enums.Detail
    type: enums.Type


class AgentStatsExport(BaseModel):
    source: str
    datetime_start: datetime
    datetime_end: datetime
    agent_user: str
    campaign_id: str
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]
    time_format: enums.TimeFormat
    group_by_campaign: Optional[enums.ViciboxBoolean]


class UserGroupStatus(BaseModel):
    source: str
    user_groups: str = 'ADMIN|AGENTS'
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]


class InGroupStatus(BaseModel):
    source: str
    in_groups: str = 'SALESLINE|SUPPORT'
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]


class AgentStatus(BaseModel):
    source: str
    agent_user: str
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]
    include_ip: enums.ViciboxBoolean


class CallIdInfo(BaseModel):
    source: str
    call_id: str
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]
    detail: enums.ViciboxBoolean


class LeadFieldInfo(BaseModel):
    source: str
    lead_id: int
    field_name: str
    custom_fields: enums.ViciboxBooleanShort
    list_id: str


class LeadAllInfo(BaseModel):
    source: str
    lead_id: int
    phone_number: Optional[str]
    custom_fields: Optional[enums.ViciboxBooleanShort]
    force_entry_list_id: int
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]


class LeadStatusSearch(BaseModel):
    source: str
    status: str
    date: date
    lead_id: Optional[int]
    custom_fields: Optional[enums.ViciboxBooleanShort]
    list_id: Optional[str]


class LeadSearch(BaseModel):
    phone_number: str
    source: str
    records: int
    header: Optional[enums.ViciboxBoolean]


class CCCLeadInfo(BaseModel):
    source: str
    call_id: str
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]


class LeadCallbackInfo(BaseModel):
    source: str
    lead_id: int
    stage: enums.AgentCampaignsStage
    header: Optional[enums.ViciboxBoolean]
    search_location: enums.SearchLocation


class UpdateLogEntry(BaseModel):
    source: str
    call_id: str
    group: str
    status: str


class AddLead(BaseModel):
    phone_number: str
    phone_code: str
    list_id: int
    source: str
    dnc_check: enums.ViciboxBooleanShort
    campaign_dnc_check: enums.ViciboxBooleanShort
    campaign_id: str
    add_to_hopper: enums.ViciboxBooleanShort
    hopper_priority: int = 0
    hopper_local_call_time_check: enums.ViciboxBooleanShort
    duplicate_check: enums.DuplicateCheck
    usacan_prefix_check: enums.ViciboxBooleanShort
    usacan_areacode_check: enums.ViciboxBooleanShort
    nanpa_ac_prefix_check: enums.ViciboxBooleanShort
    custom_fields: enums.ViciboxBooleanShort
    tz_method: enums.TZMethod
    callback: enums.ViciboxBooleanShort
    callback_status: str
    callback_datetime: datetime
    callback_type: enums.CallbackType
    callback_user: str
    callback_comments: str
    lookup_state: enums.ViciboxBooleanShort
    list_exists_check: enums.ViciboxBooleanShort
    vendor_lead_code: Optional[str]
    source_id: Optional[str]
    gmt_offset_now: Optional[str]
    title: Optional[str]
    first_name: Optional[str]
    middle_initial: Optional[str]
    last_name: Optional[str]
    address1: Optional[str]
    address2: Optional[str]
    address3: Optional[str]
    city: Optional[str]
    state: Optional[str]
    province: Optional[str]
    postal_code: Optional[str]
    country_code: Optional[str]
    gender: Optional[enums.Gender]
    date_of_birth: Optional[date]
    alt_phone: Optional[str]
    email: Optional[str]
    security_phrase: Optional[str]
    comments: Optional[str]
    multi_alt_phones: Optional[str]
    rank: Optional[int]
    owner: Optional[str]
    entry_list_id: Optional[str]


class UpdateLead(AddLead):
    lead_id: int
    search_method: str = 'LEAD_ID'
    search_location: str = enums.SearchLocationUpdateLead
    insert_if_not_found: enums.ViciboxBooleanShort
    records: int
    no_update: enums.ViciboxBooleanShort
    delete_lead: enums.ViciboxBooleanShort
    delete_cf_data: enums.ViciboxBooleanShort
    reset_lead: enums.ViciboxBooleanShort
    update_phone_number: Optional[enums.ViciboxBooleanShort]
    remove_from_hopper: Optional[enums.ViciboxBooleanShort]
    user_field: Optional[str]
    list_id_field: Optional[int]
    status: Optional[str]
    called_count: Optional[int]
    force_entry_list_id: Optional[list]


class BatchUpdateLead(BaseModel):
    lead_ids: str
    source: str
    list_exists_check: Optional[enums.ViciboxBooleanShort]
    reset_lead: Optional[enums.ViciboxBooleanShort]
    records: int
    user_field: Optional[str]
    list_id_field: Optional[int]
    status: Optional[str]
    vendor_lead_code: Optional[str]
    source_id: Optional[str]
    gmt_offset_now: Optional[str]
    title: Optional[str]
    first_name: Optional[str]
    middle_initial: Optional[str]
    last_name: Optional[str]
    address1: Optional[str]
    address2: Optional[str]
    address3: Optional[str]
    city: Optional[str]
    state: Optional[str]
    province: Optional[str]
    postal_code: Optional[str]
    country_code: Optional[str]
    gender: Optional[enums.Gender]
    date_of_birth: Optional[date]
    alt_phone: Optional[str]
    email: Optional[str]
    security_phrase: Optional[str]
    comments: Optional[str]
    rank: Optional[int]
    owner: Optional[str]
    called_count: Optional[int]
    phone_code: Optional[str]


class AddUser(BaseModel):
    agent_user: str
    agent_pass: str
    agent_user_level: int
    agent_full_name: str
    agent_user_group: str
    phone_login: Optional[str]
    phone_pass: Optional[str]
    hotkeys_active: Optional[int]
    voicemail_id: Optional[int]
    email: Optional[str]
    custom_one: Optional[str]
    custom_two: Optional[str]
    custom_three: Optional[str]
    custom_four: Optional[str]
    custom_five: Optional[str]
    wrapup_seconds_override: Optional[int]
    agent_choose_ingroups: Optional[int]
    agent_choose_blended: Optional[int]
    closer_default_blended: Optional[int]
    in_groups: Optional[str]


class CopyUser(BaseModel):
    agent_user: str
    agent_pass: str
    agent_full_name: str
    source_user: str


class UpdateUser(AddUser):
    active: Optional[enums.ViciboxBooleanShort]
    campaign_rank: Optional[int]
    campaign_grade: Optional[int]
    ingroup_rank: Optional[int]
    ingroup_grade: Optional[int]
    camp_rg_only: Optional[int]
    campaign_id: Optional[int]
    ingrp_rg_only: Optional[int]
    group_id: Optional[int]


class AddGroupAlias(BaseModel):
    caller_id_number: str
    group_alias_id: Optional[str]
    group_alias_name: Optional[str]
    caller_id_name: Optional[str]
    active: Optional[enums.ViciboxBooleanShort]
    admin_user_group: Optional[str]


class AddDNCPhone(BaseModel):
    phone_number: str
    campaign_id: str


class AddFPGPhone(BaseModel):
    phone_number: str
    group: str


class AddPhone(BaseModel):
    extension: str
    dialplan_number: int
    voicemail_id: int
    phone_login: str
    phone_pass: str
    server_ip: str
    protocol: enums.Protocol
    registration_password: str
    phone_full_name: str
    local_gmt: float
    outbound_cid: int
    phone_context: Optional[str]
    email: Optional[str]
    admin_user_group: Optional[str]
    is_webphone: Optional[enums.ViciboxBooleanShort]
    webphone_auto_answer: Optional[enums.ViciboxBooleanShort]
    use_external_server_ip: Optional[enums.ViciboxBooleanShort]
    template_id: Optional[str]
    on_hook_agent: Optional[enums.ViciboxBooleanShort]


class UpdatePhone(AddPhone):
    delete_phone: Optional[enums.ViciboxBooleanShort]


class AddPhoneAlias(BaseModel):
    alias_id: Optional[str]
    phone_logins: Optional[str]
    alias_name: Optional[str]


class UpdatePhoneAlias(AddPhoneAlias):
    delete_alias: Optional[enums.ViciboxBooleanShort]


class ServerRefresh(BaseModel):
    stage: str = "REFRESH"


class AddList(BaseModel):
    list_id: int
    list_name: str
    campaign_id: str
    active: Optional[enums.ViciboxBooleanShort]
    list_description: Optional[str]
    outbound_cid: Optional[int]
    script: Optional[str]
    am_message: Optional[str]
    drop_inbound_group: Optional[str]
    web_form_address: Optional[str]
    web_form_address_two: Optional[str]
    web_form_address_three: Optional[str]
    reset_time: Optional[str]
    tz_method: Optional[enums.TZMethodAddList]
    local_call_time: Optional[str]
    expiration_date: Optional[date]
    xferconf_one: Optional[str]
    xferconf_two: Optional[str]
    xferconf_three: Optional[str]
    xferconf_four: Optional[str]
    xferconf_five: Optional[str]
    custom_fields_copy: Optional[int]
    custom_copy_method: Optional[enums.CustomCopyMethod]


class UpdateList(AddList):
    source: str
    insert_if_not_found: Optional[enums.ViciboxBooleanShort]
    reset_list: Optional[enums.ViciboxBooleanShort]
    delete_list: Optional[enums.ViciboxBooleanShort]
    delete_leads: Optional[enums.ViciboxBooleanShort]
    custom_fields_add: Optional[enums.ViciboxBooleanShort]
    field_label: Optional[str]
    field_name: Optional[str]
    field_size: Optional[int]
    field_type: Optional[str]
    field_rank: Optional[int]
    field_order: Optional[int]
    field_rerank: Optional[enums.ViciboxBooleanShort]
    field_max: Optional[int]
    field_default: Optional[str]
    field_options: Optional[str]
    field_duplicate: Optional[enums.ViciboxBooleanShort]
    field_description: Optional[str]
    field_help: Optional[str]
    field_required: Optional[enums.ViciboxBooleanShort]
    multi_position: Optional[enums.FieldPosition]
    name_position: Optional[enums.NamePosition]
    field_encrypt: Optional[enums.ViciboxBooleanShort]
    field_show_hide: Optional[enums.FieldShowHide]
    custom_fields_update: Optional[enums.ViciboxBooleanShort]
    custom_fields_delete: Optional[enums.ViciboxBooleanShort]


class ListInfo(BaseModel):
    list_id: int
    source: str
    leads_counts: Optional[enums.ViciboxBooleanShort]
    dialable_count: Optional[enums.ViciboxBooleanShort]
    stage: Optional[enums.AgentCampaignsStage]
    header: Optional[enums.ViciboxBoolean]


class ListCustomFields(BaseModel):
    list_id: int
    source: str
    stage: Optional[enums.AgentCampaignsStage]
    header: Optional[enums.ViciboxBoolean]
    custom_order: Optional[enums.CustomOrder]


class CheckPhoneNumber(BaseModel):
    phone_number: int
    phone_code: int
    local_call_time: str
    postal_code: Optional[int]
    state: Optional[str]
    owner: Optional[str]
    dnc_check: Optional[enums.ViciboxBooleanShort]
    campaign_dnc_check: Optional[enums.ViciboxBooleanShort]
    campaign_id: str
    usacan_prefix_check: Optional[enums.ViciboxBooleanShort]
    usacan_areacode_check: Optional[enums.ViciboxBooleanShort]
    nanpa_ac_prefix_check: Optional[enums.ViciboxBooleanShort]
    tz_method: Optional[enums.TZMethodCheckPhoneNumber]


class LoggedInAgents(BaseModel):
    source: str
    campaigns: str
    user_groups: str
    show_sub_status: Optional[enums.ViciboxBoolean]
    stage: Optional[enums.AgentCampaignsStage]
    header: Optional[enums.ViciboxBoolean]


class CallStatusStats(BaseModel):
    campaigns: str
    query_date: Optional[date]
    ingroups: Optional[str]
    statuses: Optional[str]


class CallDispoReport(BaseModel):
    campaigns: str
    ingroups: str
    dids: str
    query_date: Optional[date]
    ene_date: Optional[date]
    statuses: Optional[str]
    categories: Optional[str]
    users: Optional[str]
    status_breakdown: Optional[int]
    show_percentages: Optional[int]
    file_download: Optional[int]


class UpdateCampaign(BaseModel):
    campaign_id: str
    source: str
    campaign_name: Optional[str]
    active: Optional[enums.ViciboxBooleanShort]
    auto_dial_level: Optional[str]
    adaptive_maximum_level: Optional[int]
    campaign_vdad_exten: Optional[str]
    hopper_level: Optional[int]
    reset_hopper: Optional[enums.ViciboxBooleanShort]
    dial_method: Optional[enums.DialMethod]
    dial_timeout: Optional[int]
    outbound_cid: Optional[int]
    dial_status_add: Optional[str]
    dial_status_remove: Optional[str]
    lead_filter_id: Optional[str]
    xferconf_one: Optional[str]
    xferconf_two: Optional[str]
    xferconf_three: Optional[str]
    xferconf_four: Optional[str]
    xferconf_five: Optional[str]
    dispo_call_url: Optional[str]


class UpdateALTURL(BaseModel):
    campaign_id: str
    source: str
    entry_type: enums.URLEntryType
    url_type: enums.URLType
    alt_url_id: str
    active: Optional[enums.ViciboxBooleanShort]
    url_rank: Optional[int]
    url_statuses: Optional[str]
    url_description: Optional[str]
    url_lists: Optional[str]
    url_call_length: Optional[int]
    url_address: Optional[str]


class UpdatePresets(BaseModel):
    campaign_id: str
    source: str
    preset_name: str
    action: enums.UpdatePresetsActions
    preset_hide_number: Optional[enums.ViciboxBooleanShort]
    preset_number: Optional[int]
    preset_dtmf: Optional[str]


class AddDID(BaseModel):
    did_pattern: str
    source: str
    did_description: Optional[str]
    active: Optional[enums.ViciboxBooleanShort]
    did_route: Optional[enums.DIDRoute]
    record_call: Optional[enums.ViciboxBooleanShort]
    extension: Optional[int]
    exten_context: Optional[str]
    voicemail_ext: Optional[int]
    phone_extension: Optional[str]
    server_ip: Optional[str]
    group: Optional[str]
    menu_id: Optional[str]
    filter_clean_cid_number: Optional[str]
    call_handle_method: Optional[enums.CallHandleMethod]
    agent_search_method: Optional[enums.AgentSearchMethod]
    list_id: Optional[int]
    entry_list_id: Optional[int]
    campaign_id: Optional[str]
    phone_code: Optional[int]


class UpdateDID(AddDID):
    delete_did: Optional[enums.ViciboxBooleanShort]


class UpdateCIDGroupEntry(BaseModel):
    cid_group_id: str
    source: str
    areacode: str
    stage: enums.CIDGroupEntryStage
    outbound_cid: Optional[int]
    cid_description: Optional[str]
    active: Optional[enums.ViciboxBooleanShort]


schemas_non_agent_dict = {
    'version': Version,
    'sound_list': SoundList,
    'moh_list': MOHList,
    'vm_list': VMList,
    'blind_monitor': BlindMonitor,
    'agent_ingroup_info': AgentIngroupInfo,
    'agent_campaigns': AgentCampaigns,
    'campaigns_list': CampaignList,
    'hopper_list': HopperList,
    'recording_lookup': RecordingLookup,
    'did_log_export': DidLogExport,
    'phone_number_log': PhoneNumberLog,
    'agent_stats_export': AgentStatsExport,
    'user_group_status': UserGroupStatus,
    'in_group_status': InGroupStatus,
    'agent_status': AgentStatus,
    'callid_info': CallIdInfo,
    'lead_field_info': LeadFieldInfo,
    'lead_all_info': LeadAllInfo,
    'lead_status_search': LeadStatusSearch,
    'lead_search': LeadSearch,
    'ccc_lead_info': CCCLeadInfo,
    'lead_callback_info': LeadCallbackInfo,
    'update_log_entry': UpdateLogEntry,
    'add_lead': AddLead,
    'update_lead': UpdateLead,
    'batch_update_lead': BatchUpdateLead,
    'add_user': AddUser,
    'copy_user': CopyUser,
    'update_user': UpdateUser,
    'add_group_alias': AddGroupAlias,
    'add_dnc_phone': AddDNCPhone,
    'add_fpg_phone': AddFPGPhone,
    'add_phone': AddPhone,
    'update_phone': UpdatePhone,
    'add_phone_alias': AddPhoneAlias,
    'server_refresh': ServerRefresh,
    'add_list': AddList,
    'update_list': UpdateList,
    'list_info': ListInfo,
    'list_custom_fields': ListCustomFields,
    'check_phone_number': CheckPhoneNumber,
    'logged_in_agents': LoggedInAgents,
    'call_status_stats': CallStatusStats,
    'call_dispo_report': CallDispoReport,
    'update_campaign': UpdateCampaign,
    'update_alt_url': UpdateALTURL,
    'update_presets': UpdatePresets,
    'add_did': AddDID,
    'update_did': UpdateDID,
    'update_cid_group_entry': UpdateCIDGroupEntry
}
