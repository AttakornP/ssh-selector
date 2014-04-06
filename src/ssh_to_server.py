from os import environ, system
#import json
import sys
import yaml


def option_help():
    print (
    "\nUsage:"
    "\n\tssh-server <server-name>"
    "\nOption :"
    "\n\t--help\t\tShow all option and command example."
    "\n\t--list\t\tList all your server name."
    )

def option_list(data):
    for server in data:
        print "server-name : {}".format(server["server-name"])

def read_file(config_file):
    outfile = open(config_file, "r")
#    server_data = json.load(outfile)
    server_data = yaml.load(outfile)
    outfile.close()
    return server_data

def search_server(data, server_name):
    for server in data:
        if server_name == server["server-name"]:
            return server

if __name__ == "__main__":
    server_name = sys.argv[1]
    config_file = environ["HOME"] + "/ssh-server"
    server_data = read_file(config_file)
    if "--" in server_name:
        if "list" in server_name:
            option_list(server_data)
        if "help" in server_name:
            option_help()
    else:
        server = search_server(server_data, server_name)
        ssh_cmd = "ssh {}@{} -p {}".format(server["user"], server["host"], server["port"])
        system(ssh_cmd)


