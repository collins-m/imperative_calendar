calendar = {
	"sun": [],
	"mon": [],
	"tue": [],
	"wed": [],
	"thu": [],
	"fri": [],
	"sat": [],
}

a_calendar = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]				# for checks

def help():
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
	print("Appointments for", day.capitalize())
	print()
	for app in calendar[day]:
		print(app[0]+" from", app[1][0], "until", app[1][1])
	print("-"*76)

def view_week():
	for day in a_calendar:
		view_day(day)

def view(n):
	if n == "calendar":													# View all
		view_week()

	elif n in a_calendar:												# View day
		view_day(n)

	else:
		print("Input Error, type \"help\" for a list of commands")
	

def add(a):																	# Add appointment
	try:
		calendar[a[1]].append([a[2], (a[3], a[4])])
	except:
		print("Input Error, type \"help\" for a list of commands")

def remove(day, app):														# Remove appointment
	try:
		j = 0
		for i in calendar[day]:
			if i[0] == app:
				calendar[day].pop(j)
				j += 1
	except:
		print("Input Error, type \"help\" for a list of commands")


def main():
	print("Type \"help\" for a list of commands.")
	while 1:
		try:
			command = input().split()
			print()

			if command[0] == "exit":										# Exit loop & program
				print("Goodbye.")
				break

			if command[0] == "help":										# User manual
				help()

			if command[0] == "view":										# Display data
				view(command[1])

			if command[0] == "add":											# Add app
				add(command)

			if command[0] == "remove":										# Remove app
				remove(command[1], command[2])

		except:
			print("Input Error, type \"help\" for a list of commands")

if __name__ == "__main__":
	main()