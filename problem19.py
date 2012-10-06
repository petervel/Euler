#!/usr/bin/python
__author__ = 'peter.vel'

month_size = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

class Date:
	year = 1900
	month = 1
	day = 7

	@staticmethod
	def is_leap_year(year):
		if year % 4 != 0:
			return False
		if year % 400 == 0:
			return True
		if year % 100 == 0:
			return False
		return True

	def valid_date(self):
		if self.month > 12:
			return False
		if self.day > 31:
			return False

		if self.is_leap_year(self.year):
			month_size[2] = 29
		else:
			month_size[2] = 28

		return self.day <= month_size[self.month]

	def to_next_week(self):
		self.day += 7
		if self.valid_date() == False:
			self.fix_date()

	def fix_date(self):
		self.day -= month_size[self.month]
		self.month += 1
		if self.month > 12:
			self.month = 1
			self.year += 1

def main():
	date = Date()
	count = 0
	while True:
		date.to_next_week()
		if date.year > 2000:
			break
		if date.year > 1900:
			if date.day == 1:
				count += 1

	print count

main()
