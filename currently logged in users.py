{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_event_date(event):\n",
    "    return event.date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "def current_users(events):\n",
    "    events.sort(key=get_event_date)\n",
    "    machines = {}\n",
    "    for event in events:\n",
    "        if event.machine not in machines:\n",
    "            machines[event.machine] = set()\n",
    "        if event.type == \"login\":\n",
    "            machines[event.machine].add(event.user)\n",
    "        elif event.type == \"logout\":\n",
    "            machines[event.machine].remove(event.user)\n",
    "    return machines       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "def generate_report(machines):\n",
    "    for machine, users in machines.items():\n",
    "        if len(users) > 0:\n",
    "            user_list = \", \".join(users)\n",
    "            print(\"{}: {}\".format(machine, user_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Event:\n",
    "    def __init__(self, event_date, event_type, machine_name, user):\n",
    "        self.date = event_date\n",
    "        self.type = event_type\n",
    "        self.machine = machine_name\n",
    "        self.user = user"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "events = [\n",
    "    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'mohammed'),\n",
    "    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'mohammed'),\n",
    "    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'hassan'),\n",
    "    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'mohammed'),\n",
    "    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'mohammed'),\n",
    "    Event('2020-01-21 11:24:35', 'login', 'mailserver.local', 'ali')\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'webserver.local': {'hassan'}, 'mailserver.local': {'ali'}, 'myworkstation.local': set()}\n"
     ]
    }
   ],
   "source": [
    "users = current_users(events)\n",
    "print(users)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "webserver.local: hassan\n",
      "mailserver.local: ali\n"
     ]
    }
   ],
   "source": [
    "generate_report(users)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
