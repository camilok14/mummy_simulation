import sys
from getopt import getopt, GetoptError
from simulation import Simulation, allowed_distributions
from controller.db import DatabaseController
from server import Server
from threading import Thread

def main(argv):
  population = 10000
  timelapse = 10
  distribution = 'uniform'

  help_text = 'usage: mummy [args]\n'\
    '-h\t: print this help message\n'\
    '-p\t: population, number of investors\n'\
    '-d\t: distribution (normal or uniform)\n'\
    '-t\t: timelapse, number of seconds taken to simulate a week time\n'
  try:
    shortopts = 'hp:d:t:'
    longopts = ['help', 'population=', 'distribution=', 'timelapse=']
    opts, args = getopt(argv, shortopts, longopts) #pylint: disable=unused-variable
    for opt, arg in opts:
      if opt == '-h':
        print(help_text)
        sys.exit()
      elif opt in ('-p', '--population'):
        population = int(arg)
      elif opt in ('-d', '--distribution'):
        if arg not in allowed_distributions:
          raise ValueError('distribution must be normal or uniform')
        distribution = arg
      elif opt in ('-t', '--timelapse'):
        timelapse = int(arg)
  except (GetoptError, ValueError) as e:
    print(e)
    print(help_text)
    sys.exit()
  db_controller = DatabaseController(True)
  server = Server()
  Thread(target = server.run).start()
  simulation = Simulation(population, timelapse, distribution, db_controller)
  simulation.start()

if __name__ == '__main__':
  main(sys.argv[1:])