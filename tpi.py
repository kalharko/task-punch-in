import sys
import datetime


if not __name__ == "__main__":
    raise Exception("This script should not be imported")


# Constants
# Path to the file where the tasks are stored
TASKS_FILE = 'tasks.txt'
RENDER_WIDTH = 165


class Range():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, item):
        return self.start <= item <= self.end

    def __len__(self):
        return self.end - self.start


def write_start_task(task_name: str):
    dtime = datetime.datetime.now()
    strdtime = dtime.strftime("%Y-%m-%d_%H:%M:%S")
    with open(TASKS_FILE, 'a', encoding='utf-8') as f:
        f.write(f'{strdtime} start {task_name}\n')


def end_task():
    dtime = datetime.datetime.now()
    strdtime = dtime.strftime("%Y-%m-%d_%H:%M:%S")
    with open(TASKS_FILE, 'a', encoding='utf-8') as f:
        f.write(f'{strdtime} end\n')


def render():
    with open(TASKS_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    days = []
    current_date = datetime.datetime.strptime(lines[0].split('_')[0], "%Y-%m-%d")
    current_day = []
    for line in lines:
        date = datetime.datetime.strptime(line.split('_')[0], "%Y-%m-%d")
        if date != current_date:
            days.append(current_day)
            current_day = [line]
            current_date = date
        else:
            current_day.append(line)
    if len(current_day) > 0:
        days.append(current_day)

    print(f'Number of days: {len(days)}')
    for day in days:
        print(f'Number of tasks in day: {len(day)}')

    for day in days:
        markers = {}
        ranges = []
        current_start_time = None
        current_start_dtime = None
        total_time = 0
        for task in day:
            hour = int(task.split('_')[1].split(':')[0])
            minute = int(task.split('_')[1].split(':')[1])
            time_position = (hour - 9) * 60 + minute
            time_position = time_position * (RENDER_WIDTH - 5) // 540
            markers[time_position] = task[11:16]

            if current_start_time is None:
                current_start_time = time_position
            else:
                ranges.append(Range(current_start_time, time_position))
                current_start_time = None

            if current_start_dtime is None:
                current_start_dtime = datetime.datetime.strptime(task.split(' ')[0], "%Y-%m-%d_%H:%M:%S")
            else:
                current_end_minute = datetime.datetime.strptime(task.split(' ')[0], "%Y-%m-%d_%H:%M:%S")
                total_time += (current_end_minute - current_start_dtime).total_seconds()
                current_start_dtime = None

        # headline
        headline = day[0].split('_')[0]
        headline += ' worked for '
        headline += str(int(total_time // 3600)) + 'h' + str(int((total_time % 3600) // 60))
        print(headline)

        # print markers
        i = 2
        while i < RENDER_WIDTH:
            if i in markers.keys():
                markers[i] = markers[i].replace(':', 'h').lstrip('0')
                if len(markers[i]) == 4:
                    markers[i] = ' ' + markers[i]
                print(markers[i], end=' ')
                i += 6
            else:
                print(' ', end='')
                i += 1
        print()

        # timeline text
        tl = ['|' if i in markers.keys() else ' ' for i in range(RENDER_WIDTH)]
        for i in range(len(tl)):
            if tl[i] == '|':
                continue
            for r in ranges:
                if i in r:
                    tl[i] = '/'
                    break

        print(''.join(tl))


# Parse command line arguments
args = sys.argv[1:]

# Cases
if len(args) == 0:
    end_task()

if args[0] == 's':
    write_start_task(' '.join(args[1:]))

elif args[0] == 'e':
    end_task()
elif args[0] == 'render':
    render()
