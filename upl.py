# UPL - "Unique Player Locator"
# A unique ID that determines platform and player
# Appended on career profile page.

platforms = {
	0: "pc",
	1: "xbl",
	2: "psn"
}

def getUpl(pf, sn, di = None):
	pl = platforms.get(pf, -1)
	if pl == -1:
		return -1
	elif pf == 0:
		if di is None:
			return -1
		else:
			return pl + "/" + sn + "-" + di
	else:
		return pl + "/" + sn
