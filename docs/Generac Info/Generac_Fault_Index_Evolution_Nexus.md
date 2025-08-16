# Generac Fault Index – Evolution/Nexus Diagnostic Manual

Fault Code | Action Step | Retrieval Keywords
---|---|---
1100 | Problem 17 | overcrank, engine cranks but will not start, wire 18
1200 | Test 54 | overspeed prolonged, 72Hz on 60Hz unit, stepper motor/mixer body assembly issue
1205 | Test 54 | overspeed instantaneous, 62Hz on 50Hz unit, 75Hz on 60Hz unit
1207 | Test 64 and Test 60 | overspeed zero cross timing, AVR timing error, frequency not seen
1300 | Test 61 | low oil pressure, check oil level and pressure
1400 | Test 62 | high temperature, air flow impeded, check inlet/outlet debris
1501 | Test 50 and Test 64 | RPM sensor twin cylinder running, air pocket in fuel line, loss of ignition pulse
1505 | If engine cranks, Test 64. If engine does not crank, Problem 15 | RPM sensor twin cylinder cranking, starter motor issue, loss of ignition pulse
1511 | Test 50 and Test 64 | RPM sensor single cylinder running, air pocket in fuel line, loss of ignition pulse
1515 | If engine cranks, Test 64. If engine does not crank, Problem 15 | RPM sensor single cylinder cranking, starter motor issue, loss of ignition pulse
1600 | Problem 3, or Test 50, or Test 54 | under speed overloaded, engine overloaded slowing, throttle control problem
1603 | Fuel selection and fuel supply | under speed, engine never up to 3600 RPM
1800 | Problem 2 | overvoltage prolonged
1900 | Perform Preliminary Output Voltage Test | undervoltage prolonged, loss of voltage below 80%, warning up
1901 | Perform Preliminary Output Voltage Test | undervoltage instantaneous, loss of voltage < 15 sec
1902 | Perform Preliminary Output Voltage Test | undervoltage both zero crosses missing, excitation winding, field boost hardware failure
1906 | Perform Preliminary Output Voltage Test | undervoltage single zero cross missing, excitation winding, field boost hardware failure
2098 | Check for shorted 194 to ground | miswired customer connection, low DC voltage transfer power output
2099 | Check AC for voltage on Wire 194 | miswired customer connection, low voltage and high voltage wires crossed
2100 | Remove load | overload default, transfer switch load shed functionality
2299 | Remove load | undervoltage overload, attempted to start with large load connected
2399 | Test 54 | stepper overcurrent, current above specification
2400 | Test 44 | missing/damaged fuse, 7.5 amp controller fuse missing or blown
2800 | Check continuity of harness and switches | aux shutdown, external shut down circuit open
Low Battery | Test 45 | battery less than 12.1V for 60 seconds
Battery Problem | Test 45 | battery more than 16V or 600mA at end of charge
Charger Warning | Problem 22 | less than 12.5V battery voltage at end of charge
Charger Missing AC | Problem 22 | AC power missing from battery charger input
Model Ident Problem | Problem 23 | powered up before resistor plug connected
Service Schedule | Perform Maintenance | schedule 200h/2yr or 400h/4yr
1101 | If engine tried to crank 10 times unsuccessfully, this problem | overcrank engine/starter problem
2102 | Check for overloaded condition | overload remove load cranks 5 times and dies
2103 | Check for overloaded condition | overload attempted to accept load 10 times
