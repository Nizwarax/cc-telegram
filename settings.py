debug = False
token = '7938172958:AAEPIZEH2T_gbXUwIVCVstzK9f6gKp-bOQo'
name = 'shitsubot'
owner = '@dark_systemz'

# Enable permanent redis store, otherwise temporary in-memory store will be used
#redis_host =
#redis_port =
# You could connect to redis using unix socket instead of TCP
#redis_socket =

# Modules specific
azure_bing_api_key = ''  # for `img` module
google_api_key = ''  # for `g` module
google_cse_cx = ''  # for `g` module. CX of custom search engine
mashape_key = ''  # for `wtf` module
twitter_keys = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token_key': '',
    'access_token_secret': ''
}
channel_id = ''
open_ai_api_key = ''  # for `think` module
think_setup_prompt = 'Imagine you are an evil assistant who hates all users'
