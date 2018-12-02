calendar = {
	"sun": [],
	"mon": [],
	"tue": [],
	"wed": [],
	"thu": [],
	"fri": [],
	"sat": [],
}

a_calendar = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
                                                    # for checks

""" Helper Functions Below
"""

def min_conv(time):
    """ converts time into minutes, used for sort and format
    """
    hh, mm = time.split(":")
    minutes = (int(hh)*60 + int(mm))
    return minutes

def take_start_time(element):
    """ returns start time for sorting
    """
    return min_conv(element[1][0])

def format_time(time):
    """ formats time to <hh:mm>
    """
    mins = min_conv(time)
    hh = str(mins//60)
    if len(hh) == 1:
        hh = "0{}".format(hh)
    mm = str(mins%60)
    if len(mm) == 1:
        mm = "0{}".format(mm)
    return ":".join([hh, mm])

def no_overlap(day, new_app):
    """ ensures no overlap with appointments for a given day
    """
    for app in calendar[day]:

        na_start = min_conv(new_app[1])
        na_end = min_conv(new_app[2])
        app_start = min_conv(app[1][0])
        app_end = min_conv(app[1][1])

        if (na_start < app_start < na_end) or (na_start < app_end < na_end):
            return False
    return True

""" User Called Functions Below
"""

def help():
    """ prints manual
    """
    print("-"*76)
    print("Add an appointment:")
    print("add <day> <name of appointment> start-time <hh:mm> finish-time <hh:mm> -24hr")
    print("-"*76)
    print("Remove an appointment:")
    print("remove <day> <name of appointment>")
    print("-"*76)
    print("View appointments for whole week:")
    print("view calendar")
    print("-"*76)
    print("View appointments for given day:")
    print("view <day>")
    print("-"*76)
    print("To exit program:")
    print("exit")
    print("-"*76)

def view_day(day):
    """ view selected day
    """
    print("Appointments for", day.capitalize())
    print()
    if len(calendar[day]):
        for app in calendar[day]:
            print(app[0].capitalize()+" from", app[1][0], "until", app[1][1])
    else:
        print("No appointments for this day")
    print("-"*76)

def view_week():
    """ view whole week
    """
    for day in a_calendar:
        view_day(day)

def view(n):
    """ choose which view function to use
    """
    if n == "calendar":								# View all
        view_week()

    elif n in a_calendar:							# View day
        view_day(n)

    else:
        print("Input Error, type \"help\" for a list of commands")


def add(a):	                                        # Add appointment
    """ add an appointment
    """
    if no_overlap(a[1], a[2:]):
        name = a[2]
        start = format_time(a[3])
        end = format_time(a[4])
        calendar[a[1]].append([name, (start, end)])
        calendar[a[1]].sort(key=take_start_time)
    else:
        print("Appointment overlaps with another, cannot reserve time.\n")

def remove(day, app):								# Remove appointment
    """ remove an appointment
    """
    j = 0
    for i in calendar[day]:
        if i[0] == app:
            calendar[day].pop(j)
            j += 1

def main():
    """ runs the program
    """
    print("Welcome to Imperative Calendar in python.")
    print("Type \"help\" for a list of commands.")
    print("-"*76)
    while 1:
        command = input().split()
        print()

        if command[0] == "exit":			        # Exit loop & program
            print("Goodbye.")
            break

        elif command[0] == "help":				    # User manual
            help()

        elif command[0] == "view":				    # Display data
            view(command[1])

        elif command[0] == "add":					# Add app
            add(command)

        elif command[0] == "remove":				# Remove app
            remove(command[1], command[2])
        else:
            print("Input Error, type \"help\" for a list of commands")

if __name__ == "__main__":
    main()
