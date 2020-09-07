from os import environ as env
import multiprocessing
import ast

PORT = int(env.get("PORT", 8080))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()

DBcredentials = "#{DB-credentials}#"
DBcredentials = ast.literal_eval(DBcredentials)
DBcredentials = {'host':DBcredentials['host'],
                       'key':DBcredentials['key'],
                       'database':DBcredentials['database'],
                       'completeEmployeeProfileContainer':DBcredentials['completeEmployeeProfileContainer']
                       }
