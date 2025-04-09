import webbrowser
import subprocess
import brain

def parse_command(command_action, argument=""):
  # print(command_action[0:3])
  # print(command_action)
  # print('argument -> ', argument)

  if command_action[0:4]=="web!":
    open_link(command_action[5:])
  elif command_action[0:4]=="web?":
    open_link_with_search(command_action[5:], argument)
    brain.speak("Pesquisando " + argument)
  elif command_action[0:4]=="path":
    open_program(command_action[5:])
    brain.speak("Abrindo " + argument)
  elif command_action=='commands':
    reload_commands()
    brain.speak("Atualizado")


def open_link_with_search(link, argument=""):
  print(f'{link}/search?q={argument}')
  webbrowser.get('windows-default').open_new(f'{link}/search?q={argument}')

def open_link(link):
  webbrowser.get('windows-default').open_new(f'{link}')

def open_program(path):
  subprocess.Popen([path, '-new-tab'])

def reload_commands():
  brain.read_commands_file()