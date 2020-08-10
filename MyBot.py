def my_fleets(pw):
	num = 0
	for fleet in pw.fleets(): 
		if fleet.owner() == 1:
			num += 1
	return num		
	
		
def do_turn(pw):
	#my_closest = pw.my_planets()[0]
	#
	#if len(pw.my_planets()) == 1:
	#	for my_planet in pw.my_planets():
	#		for planet in pw.planets():
	#			if planet.owner() == 0 :
	
	strongest = 0
	itr = 0
	sent = False
	
	if len(pw.my_planets()) < 5 or my_fleets(pw) < 5:
		for planet in pw.neutral_planets():
			if planet.growth_rate() > pw.neutral_planets()[strongest].growth_rate():
				for fleet in pw.fleets():
					if fleet.destination_planet() == pw.neutral_planets()[strongest]:
						if fleet.owner() == 1:
							sent = True
							break
						elif fleet.num_ships() > planet.num_ships():
							sent = True
							break 
						elif planet.num_ships() - fleet.num_ships() < 20 and fleet.turns_remaining() < 8:
							sent = True
							break 
				if not sent:
					strongest = itr
			itr += 1
			
		dest = pw.neutral_planets()[strongest]
		source = pw.my_planets()[0]
	
	else:
		dest = pw.enemy_planets()[0]
		source = pw.my_planets()[0]
		
		for planet in pw.my_planets():
			if planet.num_ships() > source.num_ships():
				source = planet
	
	num_ships = source.num_ships() / 2 
	
	pw.issue_order(source, dest, num_ships)
						
			