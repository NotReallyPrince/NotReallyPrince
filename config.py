import os

class Config(object):
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      MERISSA_TOKEN = os.environ.get("MERISSA_TOKEN", "")
      OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "NoobxCoder")
