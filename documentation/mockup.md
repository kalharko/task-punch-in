# Task Punch In Mockup

Cli tool to track time spent on tasks.

## Goals
- Write tracking info in an Obsidian's Vault, taking advantage of it's daily notes.
- Coherent tracking with a minimum of user interactions
    - Stop current tracking when the computer is locked / shutdown
    - Tasks are not tagged to projects, easily add tags afterwrd (in Obsidian ?)

## Use cases
### Install
```
git pull https://github.com/kalharko/task-punch-in
cd task-punch-in
python main.py --install
```

### Uninstall
```
tpi --uninstall
```

### Start to track a task
```
tpi <task name>
```
- If there is a current task, stop tracking it
- `task name` can not:
    - begin with a number
    - begin with today, howlong or downtime

### Stop to track the current task
```
tpi
tpi 25m
tpi 15h20
```
- Stop the current task now
- Mark the current task as stopped 25 minutes ago
- Mark the current task as stopped at 15h20

### Get time spendings info
```
tpi howlong <task name>
12 occurences, 36h total time
```
```
tpi downtime today
42 minutes
```

### Display a day's time spent
```
tpi today
```
'->
```
Tuesday 08/10
 9h23                      10h12 10h19   10h32                                             11h20           12h00
  |tpi mockup redaction      |/////|tpi    |tpi specs definition                             |///////////////|
  |                          |/////|git    |                                                 |///////////////|
  |                          |/////|setup  |                                                 |///////////////|
----------------------------------------------------------------------------------------------------------------
13h00                                                                                  16h09       16h22
  |                                                                                      |tpi pull   |
  |                                                                                      |request    |
  |                                                                                      |           |
```
