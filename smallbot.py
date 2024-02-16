import threading
import argparse
import os
import json
import time
import logging
from termcolor import colored

import kik_unofficial.datatypes.xmpp.chatting as chatting
from kik_unofficial.datatypes.xmpp.roster import FetchRosterResponse, PeersInfoResponse
from kik_unofficial.datatypes.xmpp.base_elements import XMPPElement
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.errors import LoginError

username = {}
response = {}
users = {}

# This bot class handles all the callbacks from the kik client
class EchoBot(KikClientCallback):
    def __init__(self, creds: dict):
        username = creds['username']
        password = creds.get('password') or input("Enter your password:")
        # Optional parameters
        device_id = creds['device_id']
        android_id = creds['android_id']
        # Node
        node = creds.get('node')
        self.client = KikClient(self, username, str(password), node, device_id=device_id, android_id=android_id)
        #Captcha
        self.pending_math_problems = {}  # Dictionary to store pending math problems
        self.captcha_status = {}
        self.timeout_duration = 20  # Set the timeout duration in seconds
        self.timers = {}  # Dictionary to store timers for each user
        self.client.wait_for_messages()
    # This method is called when the bot is fully logged in and setup
    def on_authenticated(self):
        self.client.request_roster()  # request list of chat partners
    #keeps bot alive 
    def send_heartbeat(self, group_jid='1100221456712_g@groups.kik.com'):
        while True:
            try:
                if group_jid:
                    self.client.send_chat_message(group_jid, " Status Check: Online Ping")
                time.sleep(300)
            except Exception as e:
                logging.error(f"Heartbeat error: {e}")

    def start_heartbeat(self):
        heartbeat_thread = threading.Thread(target=self.send_heartbeat)
        heartbeat_thread.daemon = True
        heartbeat_thread.start()
    # This method is called when the bot receives a direct message (chat message)
    def on_chat_message_received(self, chat_message: chatting.IncomingChatMessage):
        if chat_message.body.lower() == "friend":
            self.client.add_friend(chat_message.from_jid)
            self.client.send_chat_message(chat_message.from_jid, "You are now my friend! <3")
        else:
            self.client.send_chat_message(chat_message.from_jid, f'You said "{chat_message.body}"!')

    # This method is called when the bot receives a chat message in a group
    def on_group_message_received(self, chat_message: chatting.IncomingGroupChatMessage):
        separator = colored("--------------------------------------------------------", "cyan")
        group_message_header = colored("[+ GROUP MESSAGE +]", "cyan")
        print(separator)
        print(group_message_header)
        print(colored(f"From AJID: {chat_message.from_jid}", "yellow"))
        print(colored(f"From group: {chat_message.group_jid}", "yellow"))
        print(colored(f"Says: {chat_message.body}", "red"))

    def on_roster_received(self, response: FetchRosterResponse):
        print("Roster received!")
        groups = []
        users = []
        for peer in response.peers:
            if "groups.kik.com" in peer.jid:
                groups.append(peer.jid)
            else:
                users.append(peer.jid)

        user_text = '\n'.join([f"User: {us}" for us in users])
        group_text = '\n'.join([f"Group: {gr}" for gr in groups])
        partner_count = len(response.peers)

        roster_info = (
            f"Roster Received\n"
            f"Total Peers: {partner_count}\n"
            f"Groups ({len(groups)}):\n{group_text}\n"
            f"Users ({len(users)}):\n{user_text}"
        )

        print(roster_info)            
    # This method is called if a captcha is required to login
    def on_login_error(self, login_error: LoginError):
        print("Login error: " + login_error.message)
        if login_error.is_captcha():
            login_error.solve_captcha_wizard(self.client)

    def _send_xmpp_element(self, message: XMPPElement):
        """
        Serializes and sends the given XMPP element to kik servers
        :param xmpp_element: The XMPP element to send
        :return: The UUID of the element that was sent
        """
        while not self.client.connected:
            print("[!] Waiting for connection.")
            time.sleep(0.1)
        if type(message.serialize()) is list:
            print("[!] Sending multi packet data.")
            packets = message.serialize()
            for p in packets:
                self.client.loop.call_soon_threadsafe(self.client.connection.send_raw_data, p)
            return message.message_id
        else:
            self.client.loop.call_soon_threadsafe(self.client.connection.send_raw_data, message.serialize())
            return message.message_id
        

def main():
    print('main')
    # The credentials file where you store the bot's login information
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--creds', default='creds.json', help='Path to credentials file')
    args = parser.parse_args()

    # Changes the current working directory to /examples
    if not os.path.isfile(args.creds):
        print("Can't find credentials file.")
        return
    else:
        print(f"Using credentials file: {args.creds}")

    # load the bot's credentials from creds.json
    with open(args.creds, "r") as f:
        creds = json.load(f)

    bot = EchoBot(creds)

    # let the bot start
    bot.client.wait_for_messages()

if __name__ == '__main__':
    main()

    creds_file = "creds.json"

    # Check if the credentials file is in the current working directory, otherwise change directory
    if not os.path.isfile(creds_file):
        os.chdir("credit file path")

    # Load the bot's credentials from creds.json
    with open(creds_file) as f:
        creds = json.load(f)
    callback = EchoBot(creds)
