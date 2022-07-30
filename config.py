import os

class Config(object):
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      MERISSA_TOKEN = os.environ.get("MERISSA_TOKEN", "")
      OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "NoobxCoder")
      BOT_NAME = os.environ.get("BOT_NAME", "")
      OWNER_NAME = os.environ.get("OWNER_NAME", "")
      LANGUAGE_CODE = os.environ.get("LANGUAGE", "lang")

   
