#INCOMPLETE: we ran out of time at the end
import datetime
import sys
in_calendar = False
in_event = False
calendar = [] #maps uuids to event objects
class Event:
	def __init__(self):
		self.occurrences = []
	def parse_time(dt):
		return datetime.strptime(date_string, "%Y%m%dT%H%M%S")
	def add_attrs(self, attrs):
		for attr in attrs:
			if attr == "UID":
				self.uid = attrs[attr]
			elif attr == "SUMMARY":
				self.summary = attrs[attr]
			elif attr == "LOCATION":
				self.location = attrs[attr]
			elif attr.split(';')[0] == "DTSTART":
				self.dtstart = self.parse_time(attrs[attr]) #DT
			elif attr.split(';')[0] == "DTEND":
				self.dtend = self.parse_time(attrs[attr])
			elif attr == "DURATION":
				self.duration = attrs[attr]
			elif attr = "SEQUENCE":
				self.sequence = attrs[attr]
			elif attr == "RDATE":
				self.rdate = attrs[attr]
			#elif attr.split(';')[0] == "RECURRENCE-ID":
			#	if attr.split(';')[-1].strip() == "THISANDFUTURE":
			try:
				
				#change all to durations.  deal with sequences
	def add(self, attrs):
		
	def cancel(self, attrs):
		
periods = []			
for line in sys.stdin:
	if(line.strip() == "BEGIN:VCALENDAR"):
		in_calendar = True
		continue
	elif line.strip().split(":")[0] == "METHOD":
		METHOD = line.strip().split(":")[1]
	elif line.strip() == "BEGIN:VEVENT":
		ev = dict()
		in_event = True
		continue
	elif line.strip() == "END:VEVENT":
		in_event = False
		if(METHOD == "PUBLISH"):
			vev = Event()
			vev.add_attrs(ev)
			for asdf in calendar:
				if asdf.uid == vev.uid:
					calendar.remove(asdf)
			calendar.append(vev)
		elif METHOD == "ADD":
			for i in calendar:
				if i.uid == ev['UID']:
					if i.sequence < ev["SEQUENCE"]:
						i.add(ev)		
		elif METHOD == "CANCEL":
			for i in calendar:
				if i.uid == ev["UID"]:
					i.cancel(ev)
		#do stuff
		#DEAL WITH SEQEUENCE HYERE
		continue
	elif line.strip() == "END:VCALENDAR":
		in_calendar = False
	elif ':' not in line.strip():
		periods.append(line.strip())
	else:
		if in_event:
			ev[line.split(':')[0]] = line.split(':')[1]
			
		
