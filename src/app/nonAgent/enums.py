from enum import Enum


class ViciboxBoolean(str, Enum):
    yes = 'YES'
    no = 'NO'


class ViciboxBooleanShort(str, Enum):
    yes = 'Y'
    no = 'N'


class Format(str, Enum):
    tab = 'tab'
    link = 'link'
    select_frame = 'selectframe'


class SoundsListStage(str, Enum):
    date = 'date'
    size = 'size'
    name = 'name'


class BlindMonitorStage(str, Enum):
    monitor = 'MONITOR'
    barge = 'BARGE'
    hijack = 'HIJACK'


class AgentIngroupInfoStage(str, Enum):
    info = 'info'
    change = 'change'
    text = 'text'


class AgentCampaignsStage(str, Enum):
    csv = 'csv'
    tab = 'tab'
    pipe = 'pipe'


class Detail(str, Enum):
    all = 'ALL'
    last = 'LAST'


class Type(str, Enum):
    in_ = 'IN'
    out = 'OUT'
    all = 'ALL'


class TimeFormat(str, Enum):
    h = 'H'
    hf = 'HF'
    m = 'M'
    s = 'S'


class SearchLocation(str, Enum):
    current = 'CURRENT'
    archive = 'ARCHIVE'
    all = 'ALL'


class DuplicateCheck(str, Enum):
    dup_list = 'DUPLIST'
    dup_camp = 'DUPCAMP'
    dup_sys = 'DUPSYS'
    dup_title_alt_phone_list = 'DUPTITLEALTPHONELIST'
    dup_title_alt_phone_camp = 'DUPTITLEALTPHONECAMP'
    dup_title_alt_phone_sys = 'DUPTITLEALTPHONESYS'
    dup_name_phone_list = 'DUPNAMEPHONELIST'
    dup_name_phone_name = 'DUPNAMEPHONECAMP'
    dup_name_phone_sys = 'DUPNAMEPHONESYS'


class TZMethod(str, Enum):
    postal = 'POSTAL'
    tz_code = 'TZCODE'
    nanpa = 'NANPA'


class CallbackType(str, Enum):
    user_only = 'USERONLY'
    anyone = 'ANYONE'


class Gender(str, Enum):
    undefined = 'U'
    male = 'M'
    female = 'F'


class SearchLocationUpdateLead(str, Enum):
    list = 'LIST'
    campaign = 'CAMPAIGN'
    system = 'SYSTEM'


class Protocol(str, Enum):
    iax2 = 'IAX2'
    sip = 'SIP'
    zap = 'Zap'
    external = 'EXTERNAL'


class TZMethodAddList(str, Enum):
    coutry_and_area_code = 'COUNTRY_AND_AREA_CODE'
    postal_code = 'POSTAL_CODE'
    nanpa_prefix = 'NANPA_PREFIX'
    owner_time_zone_code = 'OWNER_TIME_ZONE_CODE'


class CustomCopyMethod(str, Enum):
    append = 'APPEND'
    update = 'UPDATE'
    replace = 'REPLACE'


class FieldPosition(str, Enum):
    horizontal = 'HORIZONTAL'
    vertical = 'VERTICAL'


class NamePosition(str, Enum):
    top = 'TOP'
    left = 'LEFT'


class FieldShowHide(str, Enum):
    disabled = 'DISABLED'
    x_out_all = 'X_OUT_ALL'
    last_1 = 'LAST_1'
    last_2 = 'LAST_2'
    last_3 = 'LAST_3'
    last_4 = 'LAST_4'
    first_1_last_4 = 'FIRST_1_LAST_4'


class CustomOrder(str, Enum):
    table_order = 'table_order'
    alpha_up = 'alpha_up'
    alpha_down = 'alpha_down'


class TZMethodCheckPhoneNumber(str, Enum):
    postal = 'POSTAL'
    tz_code = 'TZCODE'
    nanpa = 'NANPA'
    areacode = 'AREACODE'


class DialMethod(str, Enum):
    manual = 'MANUAL'
    ratio = 'RATIO'
    inbound_man = 'INBOUND_MAN'
    adapt_average = 'ADAPT_AVERAGE'
    adapt_hard_limit = 'ADAPT_HARD_LIMIT'
    adapt_tapered = 'ADAPT_TAPERED'


class URLEntryType(str, Enum):
    campaign = 'campaign'


class URLType(str, Enum):
    dispo = 'dispo'
    start = 'start'
    addlead = 'addlead'
    noagent = 'noagent'


class UpdatePresetsActions(str, Enum):
    update = 'UPDATE'
    new = 'NEW'
    delete = 'DELETE'
    list = 'LIST'


class DIDRoute(str, Enum):
    exten = 'EXTEN'
    voicemail = 'VOICEMAIL'
    agent = 'AGENT'
    phone = 'PHONE'
    in_group = 'IN_GROUP'
    callmenu = 'CALLMENU'
    vmail_no_inst = 'VMAIL_NO_INST'


class CallHandleMethod(str, Enum):
    cid = 'CID'
    cid_lookup = 'CIDLOOKUP'
    close = 'CLOSE'


class AgentSearchMethod(str, Enum):
    load_balanced_overflow = 'LO'
    load_balanced = 'LB'
    server_only = 'SO'


class CIDGroupEntryStage(str, Enum):
    update = 'UPDATE'
    add = 'ADD'
    delete = 'DELETE'
    info = 'INFO'


class ResponseMessages(str, Enum):
    error = 'ERROR'
    success = 'SUCCESS'
    version = 'VERSION'
