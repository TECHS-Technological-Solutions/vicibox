non_agent_function_list = [
    'version',
    # shows version and build of the API, along with the date/time and timezone

    'sounds_list',
    # outputs a list of audio files from the audio store
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    #
    # OPTIONAL FIELDS-
    # format -		format of the output(tab, link, selectframe)
    # stage -			how to sort the output(date, size, name)
    # comments -		name of the field to populate

    'moh_list',
    # outputs a list of music on hold classes in the system
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    #
    # OPTIONAL FIELDS-
    # format -		format of the output(only 'selectframe' works)
    # comments -		name of the field to populate

    'vm_list',
    # outputs a list of voicemail boxes in the system
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    #
    # OPTIONAL FIELDS-
    # format -		format of the output(only 'selectframe' works)
    # comments -		name of the field to populate

    'blind_monitor',
    # calls user-defined phone and places them in session as blind monitor
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    #
    # REQUIRED FIELDS-
    # phone_login -		alpha-numeric, no spaces or special characters allowed
    # session_id -		must be all numbers, 7 digits
    # server_ip -		must be all numbers and dots, max 15 characters
    # source -		description of what originated the API call (maximum 20 characters)
    # stage -			MONITOR, BARGE(or BARGESWAP) or HIJACK, default is MONITOR
    # 			 (HIJACK option is not currently functional)

    'agent_ingroup_info',
    # shows in-group and outbound auto-dial info for logged-in agent
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    #
    # REQUIRED FIELDS-
    # agent_user -		2-20 characters
    # source -		description of what originated the API call (maximum 20 characters)
    #
    # SETTINGS FIELDS-
    # stage -			info(show information only), change(show options to change), text(standard non-HTML output)

    'agent_campaigns'
    # looks up allowed campaigns/in-groups for a specific user
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    #
    # REQUIRED FIELDS-
    # agent_user -		2-20 characters
    # source -		description of what originated the API call (maximum 20 characters)
    #
    # OPTIONAL FIELDS-
    # campaign_id -		2-8 characters
    # ignore_agentdirect -	Y or N, default is N. Exclude AGENTDIRECT in-groups from results or not
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'campaigns_list',
    # displays information about all campaigns in the system
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    #
    # OPTIONAL FIELDS-
    # campaign_id -		2-8 characters, for all campaigns, leave blank
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'hopper_list',
    # displays information about leads in the hopper for a campaign
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # campaign_id -		2-8 characters
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header
    #
    # OPTIONAL FIELDS-
    # search_method - for faster but blocking SQL queries that may affect database performance, set this to BLOCK

    'recording_lookup',
    # looks up recordings based upon user and date or lead_id
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # SEARCH FIELDS-
    # agent_user - 2-20 characters
    # lead_id - 1-10 digits
    # date - date of the calls to pull (must be in YYYY-MM-DD format)
    # uniqueid - uniqueid of the call, works best included with another search field
    # extension - 3-100 characters, the extension listed in the recording_log
    #
    # SETTINGS FIELDS-
    # stage - the format of the exported data: csv, tab, pipe(default)
    # header - include a header(YES) or not(NO). This is optional, default is not to include a header
    # duration - Y or N, default is N. Includes the duration of the recording in the output(in seconds),
    # before the location

    'did_log_export',
    # exports all calls inbound to a DID for one day
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # phone_number -		2-20 characters, the DID that you want to pull logs for
    # date -			date of the calls to pull (must be in YYYY-MM-DD format)
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'phone_number_log',
    # exports list of calls placed to one of more phone numbers
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # phone_number -		the phone number(s) that you want to pull logs for. allows more than one, separated by commas
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header
    # detail -		(ALL) calls or only (LAST) call. default is (ALL)
    # type -			(IN)inbound, (OUT)outbound or (ALL) calls. defauls is (OUT) calls

    'agent_stats_export'
    # exports agent activity statistics
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # datetime_start -	start date/time of the agent activity to pull (must be in "YYYY-MM-DD+HH:MM:SS" format)
    # datetime_end -		end date/time of the agent activity to pull (must be in "YYYY-MM-DD+HH:MM:SS" format)
    #
    # SETTINGS FIELDS-
    # agent_user -		2-20 characters, use only for one agent stats <optional>
    # campaign_id -		2-8 characters, use only for one campaign stats <optional>
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header
    # time_format -	time format('H','HF','M','S') in hours, minutes or seconds: H = 1:23:45, M = 83:45, S = 5023
    # (default 'HF') HF will force hour format even for zero seconds time "0:00:00"
    # group_by_campaign - divide and output the agent results grouped by campaign(YES) or not(NO).
    # This is optional, default is 'NO'

    'user_group_status',
    # real-time status of one or more user groups
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # user_groups -		pipe-delimited list of user groups to get status information for "ADMIN|AGENTS"
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'in_group_status',
    # real-time status of one or more in groups
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # in_groups -		pipe-delimited list of inbound groups to get status information for "SALESLINE|SUPPORT"
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'agent_status',
    # real-time status of one agent user
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # agent_user -		2-20 characters, use only for one agent status
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'callid_info',
    # information about a call based upon the caller_code or call ID
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # call_id -		16-40 characters
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header
    # detail -		if set to YES, more call info will be output.
    # Default is NO, only callid and customer talk time will be output

    'lead_field_info',
    # pulls the value of one field of a lead
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "modify leads" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # lead_id -		1-10 digits
    # field_name -		name of lead field to pull
    #
    # OPTIONAL FIELDS-
    # custom_fields -		Y or N, default is N. If the field you want to pull is a custom field or not
    # list_id -		override for the entry_list_id of a custom field

    'lead_all_info'
    # outputs all lead data for a lead(optionally including custom fields)
    #
    # NOTE: api user for this function must have user_level set to 7 or higher
    # and "view reports" enabled and modify_leads set to 1-5
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # lead_id -		1-10 digits
    #
    # OPTIONAL FIELDS-
    # phone_number - 6-19 digits, can be used in place of a lead_id
    # (may return multiple records, up to 1000, most recently added lead first)
    # custom_fields - Y or N, default is N. If the field you want to pull is a custom field or not
    # force_entry_list_id -	3-12 digits, will override the lead's assigned entry_list_id to look
    # for custom fields data for this lead from a different list
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, newline, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'lead_status_search',
    # displays all field values of all leads that match the status and call date in request
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "modify leads" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # status -		status of leads to be pulled
    # date -			called date of the leads to pull (must be in YYYY-MM-DD format)
    # 			NOTE: both inbound and outbound call logs are searched, no more than 2000 responses are displayed
    #
    # OPTIONAL FIELDS-
    # lead_id -		1-10 digits, only used if status and date are empty
    # custom_fields -		Y or N, default is N. Display custom fields values or not
    # list_id -		override for the entry_list_id of a custom field

    'lead_search',
    # searches for leads in the vicidial_list table by phone numbers
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and
    # "view reports" enabled and modify_leads set to 1-5
    #
    # REQUIRED FIELDS-
    # phone_number -		6-19 digits(multiple separated by a comma ',', for example: 3125551212,9055551212,4075551212)
    # source -		description of what originated the API call (maximum 20 characters)
    #
    # SETTINGS FIELDS-
    # records -		number of records to display in results if more than 1 found
    # (defaults to '1000'[most recently inserted leads displayed first])
    #
    # SETTINGS FIELDS-
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'ccc_lead_info',
    # outputs lead data for cross-cluster-communication call
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # call_id -		16-40 characters
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, newline, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'lead_callback_info',
    # outputs scheduled callback data for a specific lead
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # lead_id -		16-40 characters
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, newline, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header
    # search_location -	Where to check for scheduled callback records in the system,
    # can select only one(default is CURRENT):
    # 				CURRENT - check for active scheduled callbacks
    # 				ARCHIVE - check for archived scheduled callbacks
    # 				ALL - check for both active and archived scheduled callbacks

    'update_log_entry',
    # updates the status of a vicidial_log or vicidial_closer_log entry
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "modify leads" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    # call_id -		either the uniqueid or the 20-character ID of the call
    # group -			either a campaign_id or an in-group group_id
    # status -		the new status for the log record to be set to

    'add_lead',
    # adds a new lead to the vicidial_list table with several fields and options
    # For required field check add_lead field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'update_lead',
    # updates lead information in the vicidial_list and custom_ tables
    # For required field check update_lead field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'batch_update_lead',
    # updates multiple leads in vicidial_list with single set of field values (limited field options)
    # For required field check batch_update_lead field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'add_user',
    # adds a user to the system
    # For required field check add_user field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'copy_user',
    # copies an existing user in the system to a new user ID and name
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "modify users" enabled
    #
    # REQUIRED FIELDS-
    # agent_user -		2-20 characters (for auto-generated send 'AUTOGENERATED')
    # agent_pass -		1-20 characters
    # agent_full_name -	1-50 characters
    # source_user -		2-20 characters (must be an existing user ID in the system)

    'update_user',
    # updates or deletes a user entry already in the system
    # For required field check update_user field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'add_group_alias',
    # adds group alias to the system
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "ast admin access" enabled
    #
    # REQUIRED FIELDS-
    # caller_id_number -	6-20 characters
    #
    # OPTIONAL FIELDS-
    # group_alias_id -	3-30 characters, no spaces or punctuation allowed, if not defined, caller_id_number is used
    # group_alias_name -	3-50 characters, if not defined, caller_id_number is used
    # caller_id_name -	6-20 characters, if not defined '' is default
    # active -		'Y' or 'N', if not defined 'Y' is default
    # admin_user_group -	a valid user group or '---ALL---' is used as default

    'add_dnc_phone',
    # adds phone number to a DNC list in the system
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "modify lists" enabled
    #
    # REQUIRED FIELDS-
    # phone_number -	6-20 characters
    # campaign_id -	2-30 characters, should be a valid campaign ID or "SYSTEM_INTERNAL" for the internal DNC list

    'add_fpg_phone',
    # adds phone number to a Filter Phone Group in the system
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "modify lists" enabled
    #
    # REQUIRED FIELDS-
    # phone_number -	6-20 characters
    # group -		2-30 characters, should be a valid Filter Phone Group ID in the system

    'add_phone',
    # adds a phone to the system
    # For required field check add_phone field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'update_phone',
    # updates or deletes a phone entry already in the system
    # For required field check update_phone field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'add_phone_alias',
    # updates or deletes a phone alias entry already in the system
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "ast admin access" enabled
    #
    # REQUIRED FIELDS-
    # alias_id -		2-20 characters
    # phone_logins -	2-255 characters (phone logins separated by commas)
    # alias_name -		1-50 characters
    #
    # SETTINGS FIELDS-
    # delete_alias -		Y or N, Setting this to Y will delete the phone alias from the system, default is N.

    'server_refresh',
    # forces a conf file refresh on all telco servers in the cluster
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "ast admin access" enabled
    #
    # REQUIRED FIELDS-
    # stage -		"REFRESH

    'add_list',
    # adds a list to the system
    # For required field check add_list field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'update_list',
    # updates list information in the vicidial_lists table
    # For required field check add_list field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'list_info',
    # summary information about a list
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "modify lists" enabled
    #
    # REQUIRED FIELDS-
    # list_id -		must be all numbers, 2-14 digits
    # source -		description of what originated the API call (maximum 20 characters)
    #
    # SETTINGS FIELDS- (optional)
    # leads_counts -		Y or N, will include the counts of all leads and NEW status leads in
    # the response, default is 'N'
    # dialable_count -	Y or N, will use the list's campaign settings to provide a count of how many are
    # dialable right now, default is 'N'
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'list_custom_fields',
    # shows the custom data fields that are in a list, or all lists
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "modify lists" enabled
    # NOTE: this output will not include display-only fields in the FORM, only the non-default custom data fields,
    #       any DISPLAY, SCRIPT and SWITCH form elements will be ignored
    #
    # REQUIRED FIELDS-
    # list_id -		must be all numbers, 2-14 digits, OR use "---ALL---" for all lists
    # source -		description of what originated the API call (maximum 20 characters)
    #
    # SETTINGS FIELDS- (optional)
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header
    # custom_order -		the order to put the custom fields into: table_order, alpha_up, alpha_down
    # (default is 'table_order')

    'check_phone_number',
    # allows you to check if a phone number is valid and dialable
    # For required field check check_phone_number field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'logged_in_agents',
    # list of agents that are logged in to the system
    #
    # NOTE: api user for this function must have user_level set to 7 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # source -		description of what originated the API call (maximum 20 characters)
    #
    # OPTIONAL FIELDS-
    # campaigns -		pipe-delimited list of campaigns to get status information for "TESTCAMP|INBOUND",
    # default is all campaigns shown
    # user_groups -		pipe-delimited list of user groups to get status information for "ADMIN|AGENTS",
    # default is all user groups shown
    # show_sub_status -	show agent sub-status and pause_code, requires log lookup, (YES|NO) default is NO
    #
    # SETTINGS FIELDS-
    # stage -			the format of the exported data: csv, tab, pipe(default)
    # header -		include a header(YES) or not(NO). This is optional, default is not to include a header

    'call_status_stats',
    # report on number of calls made by campaign and ingroup, with hourly and status breakdowns
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "view reports" enabled
    #
    # REQUIRED FIELDS-
    # campaigns -		Campaigns to return stats on.  Use "---ALL---" or "ALLCAMPAIGNS" for all campaigns,
    # or use single dash delimiters if
    #                         requesting more than one specific campaign
    #
    # OPTIONAL FIELDS-
    # query_date -	Date to report on, leave blank to default to today's date.  Must be in YYYY-MM-DD format
    # ingroups -	List of ingroups to report on.  Leave blank for all ingroups belonging to the campaigns
    # specified in the "campaigns" variable.
    # 		Use dash delimiters if requesting more than one ingroup.
    # statuses -	List of specific statuses to report on.  Leave blank for all, or use dash delimiters if
    # requesting more than one status.

    'call_dispo_report',
    # call disposition breakdown report
    #
    #
    # NOTE: api user for this function must have user_level set to 9 and "view reports" enabled
    #
    # REQUIRED FIELDS(one of the following)-
    # campaigns -		Campaigns to return stats on.  Use single dash delimiters if requesting more than
    # one specific campaign
    # ingroups -		In-Groups to return stats on.  Use single dash delimiters if requesting more than
    # one specific inbound group
    # dids -			DIDs to return stats on.  Use single dash delimiters if requesting more than one specific DID
    #
    # OPTIONAL FIELDS-
    # query_date -	Date to report on, leave blank to default to today's date.  Must be in YYYY-MM-DD format
    # end_date -	Date to report on, leave blank to default to today's date.  Must be in YYYY-MM-DD format
    # statuses -	List of specific statuses to report on.  Leave blank for all, or use dash delimiters if
    # requesting more than one status.
    # categories -	List of specific status categories to report on.  Leave blank for all, or use dash delimiters
    # if requesting more than one category.
    # users -		List of specific users to report on.  Use single dash delimiters if requesting more than
    # one specific user
    # status_breakdown -	[0,1] Breakdown of all statuses within selected elements, default 0
    # show_percentages -	[0,1] (Only works if status_breakdown above is enabled), will show percentages of statuses,
    # default 0
    # file_download -		[0,1] Download as a CSV file, default 0

    'update_campaign',
    # updates campaign information in the vicidial_campaigns table
    # For required field check update_campaign field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'update_alt_url',
    # updates/adds/displays alternate dispo call url entries for a campaign
    # For required field check update_alt_url field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'update_presets',
    # updates/adds/displays/deletes campaign preset entries
    #
    # NOTE: api user for this function must have user_level set to 8 or higher and "modify campaigns" enabled
    #
    # REQUIRED FIELDS-
    # campaign_id -		2-8 characters
    # source -		description of what originated the API call (maximum 20 characters)
    # preset_name -		name of the preset in the system
    # 			   NOTE: If only one preset exists for this campaign, then this field can be left blank
    # action -		'UPDATE', 'NEW', 'DELETE' or 'LIST' (default is 'UPDATE')
    # 			   NOTE: 'stage'(csv, tab, pipe[default]) and 'header'(YES, NO) options are available for an action
    # 			   of 'LIST'
    #
    # EDITABLE FIELDS-
    # preset_hide_number -	One of these: 'Y','N', default is 'N'
    # preset_number -		Digits only (must be from 1 to 50 digits in length)
    # preset_dtmf -		Digits and certain characters only
    # ('0123456789PSQ' [P = #-pound, S = *-star, Q = half-second-quiet])

    'add_did',
    # adds new Inbound DID entries to the system in the vicidial_inbound_dids table
    # For required field check add_did field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'update_did',
    # updates Inbound DID information in the vicidial_inbound_dids table
    # For required field check update_did field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt

    'update_cid_group_entry',
    # updates CID Group entries in the vicidial_campaign_cid_areacodes table
    # For required field check update_cid_group_entry field in documentation: http://vicidial.org/docs/NON-AGENT_API.txt
]
