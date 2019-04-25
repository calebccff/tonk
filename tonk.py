#!/usr/bin/env python3

import toml, sys, os
from trello import TrelloClient, exceptions

FORMAT_TITLE = "${color a0d789}"
FORMAT_TASK = "${color cfebc4}"
FORMAT_RESET = "${color white}"

CONFIG_TEMPLATE = """[params]
  api_key = ""
  token = ""

[board]
  id = ""
  [[list]]
    id = ""
  [[list]]
    id = ""
"""

CONFIG_FILE = "{}/.config/tonk/tonk.toml".format(os.environ.get("HOME"))

def load_config():
    config = ""
    if os.path.isfile(CONFIG_FILE):
        config = toml.loads(open(CONFIG_FILE, "r").read())
        return config
    try:
        os.makedirs(os.path.dirname(CONFIG_FILE))
    except FileExistsError: #All the directories exist, just not the config file
        pass
    
    f = open(CONFIG_FILE, "w")
    f.write(CONFIG_TEMPLATE)
    f.close()
    print("Please configure this program with the config file in \n\"{}\"".format(CONFIG_FILE))
    exit()


config = load_config()
if not config["params"]["api_key"]:
    api = toml.loads(open("api.toml").read())
    config["params"]["api_key"], config["params"]["token"] = api["api_key"], api["token"]

client = TrelloClient(
    api_key=config["params"]["api_key"],
    token=config["params"]["token"]
)

board = config["board"]
try:
    tb = client.get_board(board["id"])
except trello.exceptions.ResourceUnavailable:
    println("ERROR: Failed GET board, check that your config file is correct")
for li in config["list"]:
    tl = tb.get_list(li["id"])
    print("{}> {}".format(FORMAT_TITLE, tl.name))
    print(FORMAT_TASK, end="")
    for i, card in enumerate(tl.list_cards(), start=1):
        print("{}. {}".format(i, card.name))
    print()

END = FORMAT_RESET
if len(sys.argv) > 1:
    END = sys.argv[1]
print(END)