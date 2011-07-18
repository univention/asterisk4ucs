# coding=utf-8

import univention.admin.filter
import univention.admin.syntax
import univention.admin.handlers
import univention.admin.handlers.asterisk
import univention.admin.handlers.asterisk.contact
import univention.admin.handlers.asterisk.phonegroup
import univention.admin.handlers.asterisk.waitingloop
import univention.admin.handlers.asterisk.sipPhone
import univention.admin.handlers.asterisk.conferenceRoom
import univention.admin.handlers.asterisk.phoneType

module = "asterisk/asterisk"
childs = 0
short_description = u"Asterisk"
long_description = ''
operations = ['search']

usewizard = 1
wizardmenustring="Asterisk"
wizarddescription="Asterisk verwalten"
wizardpath="univentionAsteriskObject"
childmodules = [
	"asterisk/contact",
	"asterisk/phonegroup",
	"asterisk/waitingloop",
	"asterisk/sipPhone",
	"asterisk/conferenceRoom",
	"asterisk/phoneType",
]

virtual = True
options = {}
layout = []
property_descriptions = {}
mapping = univention.admin.mapping.mapping()

class object(univention.admin.handlers.simpleLdap):
	module=module

	def __init__(self, co, lo, position, dn='', superordinate=None,
			arg=None):
		global mapping
		global property_descriptions
		self.co = co
		self.lo = lo
		self.dn = dn
		self.position = position
		self._exists = 0
		self.mapping = mapping
		self.descriptions = property_descriptions
		univention.admin.handlers.simpleLdap.__init__(self, co, lo, 
			position, dn, superordinate)

	def exists(self):
		return self._exists

def lookup(*args, **kwargs):
	return ( 
		univention.admin.handlers.asterisk.phonegroup.lookup(
			*args, **kwargs) +
		univention.admin.handlers.asterisk.waitingloop.lookup(
			*args, **kwargs) +
		univention.admin.handlers.asterisk.sipPhone.lookup(
			*args, **kwargs) +
		univention.admin.handlers.asterisk.conferenceRoom.lookup(
			*args, **kwargs) +
		univention.admin.handlers.asterisk.phoneType.lookup(
			*args, **kwargs) +
		univention.admin.handlers.asterisk.contact.lookup(
			*args, **kwargs)
	)

def identify(dn, attr, canonical=0):
	pass

