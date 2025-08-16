# Generac Fault Index – PowerZone Diagnostic Manual (with Extra Keywords)

Displayed Alarm | Alarm/Warning | E-Code | Condition Description | Action Step | Extra Keywords
---|---|---|---|---|---
Missing Config - Parameter Group | ALARM | 502 | Generator Model not selected; finish setup. | Call Technical support. | missing config, parameter, setup
Missing Config - Fuel Type | ALARM | 504 | Generator fuel not selected; finish setup. | Call Technical support. | missing config, fuel type, setup
Invalid Serial Number | ALARM | 505 | Invalid serial number in controller. | Call Technical support. | invalid serial number, controller
Controller Fault | ALARM | 1000 | Controller memory failure. | Call Technical support. | controller fault, memory
Controller Fault | ALARM | 1005 | Controller timer failure. | Call Technical support. | controller fault, timer
Controller Fault | ALARM | 1006 | Internal controller alarm. | Call Technical support. | internal controller alarm
Overcrank | ALARM | 1100 | Engine cranks but will not start. | Fuel Supply and Pressure Test page 76 | overcrank, will not start, fuel supply
Overspeed | ALARM | 1200 | Prolonged overspeed; >72 Hz for 3 s (60 Hz unit). | Engine Speed Test page 70 | overspeed prolonged, 72 Hz
Overspeed | ALARM | 1205 | Instantaneous overspeed; >75 Hz for 0.1 s (60 Hz unit). | Engine Speed Test page 70 | overspeed instantaneous, 75 Hz
Overspeed | ALARM | 1208 | System overspeed from DPE sensing wires. | Call Technical support. | overspeed DPE, sensing wires
RPM Sensor | ALARM | 1522 | Crank Position RPM and DPE frequency both 0 after crank command. | Battery and Cables Test page 63 | rpm sensor, crank position, dpe 0
Underspeed | ALARM | 1600 | Unit overloaded / slowing engine speed. | Overload Condition Test page 45 | underspeed, overloaded
Overvoltage | ALARM | 1800 | Prolonged overvoltage. | AC Output Voltage Test page 42 | overvoltage prolonged
Overvoltage | ALARM | 1801 | Instantaneous overvoltage. | AC Output Voltage Test page 42 | overvoltage instantaneous
Undervoltage | ALARM | 1900 | Prolonged undervoltage (>10 s). | Preliminary Output Voltage Test page 46 | undervoltage prolonged
Undervoltage | ALARM | 1901 | Instantaneous undervoltage (<15 s after start-up). | Preliminary Output Voltage Test page 46 | undervoltage instantaneous
Undervoltage | ALARM | 1902 | Both zero crosses missing (>1.5 s). | Preliminary Output Voltage Test page 46 | undervoltage zero crosses missing
Undervoltage | ALARM | 1906 | Single zero cross missing (>1.5 s). | Preliminary Output Voltage Test page 46 | undervoltage single zero cross
Undervoltage | ALARM | 1907 | After load shed, generator remains overloaded. | Overload Condition Test page 45 | undervoltage overloaded after shed
Keypad Missing | ALARM | 2070 | Controller does not recognize keypad presence. | Power cycle unit; if error reoccurs call Technical support. | keypad missing
Quadclops Missing | WARNING | 2075 | Controller does not recognize external LED indicators. | Call Technical support. | quadclops missing, external LED
Model ID Sync Failed | WARNING | 2090 | Communication failure controller/radio/ECM (Serial number). | Call Technical support. | model id sync failed
Wiring Error | ALARM | 2094 | DC wires 395A/B sees AC power. | Verify customer wiring to ATS/Generator. | wiring error 395A 395B
Fuel Type Sync Failed | WARNING | 2095 | Communication failure controller/radio/ECM for fuel type. | Call Technical support. | fuel type sync failed
Wiring Error | ALARM | 2099 | DC wires 194/23 sees AC power. | Verify customer wiring to ATS/Generator. | wiring error 194 23
Overload Remove Load | ALARM | 2100 | Controller detecting overload; hold-off depends on field current. | Overload Condition Test page 45 | overload remove load
AVR PWM Overload | ALARM | 2115 | AVR sensed overload. | Overload Condition Test page 45 | avr pwm overload
Serial Num Sync Failed | WARNING | 2120 | Communication failure controller/radio/ECM (Serial number). | Call Technical support. | serial num sync failed
Run Hours Sync Failed | WARNING | 2125 | Communication failure controller/radio/ECM (run hours). | Call Technical support. | run hours sync failed
CANBus Error | ALARM | 2670 | Communication lost between ECM and Controller. | CAN bus Test page 65 | can bus error
No Transfer Detected | WARNING | 2738 | Transfer commanded but not detected. | Transfer Control Wires Test page 92 | no transfer detected
Low Battery | WARNING | 2750 | Battery <12.1V for 60 s. | Battery and Cables Test page 63 | low battery
Very Low Battery | ALARM | 2751 | Battery <9.0V for 60 s. | Battery and Cables Test page 63 | very low battery
Battery Problem | WARNING | 2760 | >16V or >600 mA at end of 18h charge. | AC Battery Charger Test page 61 | battery problem charge
Charger Warning | WARNING | 2770 | Battery <12.5V after 18h charge. | AC Battery Charger Test page 61 | charger warning
Charger Missing AC | WARNING | 2780 | AC input to charger missing >3 minutes. | Problem 22 / Battery charger input | charger missing AC
SEEPROM Abuse | WARNING | 2790 | Internal controller alarm. | Power cycle unit; if error reoccurs call Technical support. | seeprom abuse
Emergency Shutdown Pressed | ALARM | 2800 | Emergency Shutdown active. | With unit OFF, press and hold OFF 3s to reset or contact Technical support. | emergency shutdown pressed
Auxiliary Shutdown | ALARM | 2801 | Remote E-Stop active. | Verify remote E-Stop; with unit OFF press OFF 3s to reset. | aux shutdown remote e-stop
ECU Faulted | WARNING | 3000 | ECU faulted. | Power cycle unit; if error reoccurs call Technical support. | ecu faulted
Engine Throttle Valve 1 Position 1 | ALARM | 3100 | Throttle position above normal; high severe. | Throttle Position Sensor Test page 91 | throttle valve high
Engine Throttle Valve 1 Position 1 | ALARM | 3101 | Throttle position below normal; high severe. | Throttle Position Sensor Test page 91 | throttle valve low
Engine Throttle Valve 1 Position 1 | ALARM | 3103 | Throttle position signal >4900 mV. | Throttle Position Sensor Test page 91 | throttle signal high 4900mV
Engine Throttle Valve 1 Position 1 | ALARM | 3104 | Throttle position signal <250 mV. | Throttle Position Sensor Test page 91 | throttle signal low 250mV
Engine Throttle Valve 1 Position 1 | ALARM | 3107 | Mechanical system does not respond. | Electronic Throttle Control Power Test page 68 | throttle no response
Engine Throttle Valve 1 Position 1 | WARNING | 3115 | Voltage above range; least severe. | Throttle Position Sensor Test page 91 | throttle voltage high warning
Engine Throttle Valve 1 Position 1 | WARNING | 3117 | Voltage below range; least severe. | Throttle Position Sensor Test page 91 | throttle voltage low warning
Engine Fuel Delivery Pressure | ALARM | 3200 | Fuel pressure above normal; high severe. | Fuel Pressure Sensor Test page 73 | fuel pressure high
Engine Fuel Delivery Pressure | ALARM | 3201 | Fuel pressure below normal; high severe. | Fuel Pressure Sensor Test page 73 | fuel pressure low
Engine Fuel Delivery Pressure | ALARM | 3203 | Fuel pressure signal above 4900 mV. | Fuel Pressure Sensor Test page 73 | fuel pressure signal high
Engine Fuel Delivery Pressure | ALARM | 3204 | Fuel pressure signal below 120 mV. | Fuel Pressure Sensor Test page 73 | fuel pressure signal low
Engine Fuel Delivery Pressure | WARNING | 3215 | Fuel pressure above normal; least severe. | Fuel Pressure Sensor Test page 73 | fuel pressure high warn
Engine Fuel Delivery Pressure | WARNING | 3217 | Fuel pressure below normal; least severe. | Fuel Pressure Sensor Test page 73 | fuel pressure low warn
Engine Oil Pressure | ALARM | 3301 | Oil pressure signal below normal; high severe. | Oil Pressure Switch Test page 84 | oil pressure low
Engine Oil Pressure | ALARM | 3304 | Oil pressure signal above normal range. | Oil Pressure Switch Test page 84 | oil pressure high
Engine Intake Manifold #1 Pressure | ALARM | 3400 | Manifold pressure above normal; high severe. | Intake Manifold Pressure Sensor Test page 78 | map high
Engine Intake Manifold #1 Pressure | ALARM | 3401 | Manifold pressure below normal; high severe. | Intake Manifold Pressure Sensor Test page 78 | map low
Engine Intake Manifold #1 Pressure | ALARM | 3403 | Signal voltage above 4900 mV. | Intake Manifold Pressure Sensor Test page 78 | map signal high
Engine Intake Manifold #1 Pressure | ALARM | 3404 | Signal voltage below 250 mV. | Intake Manifold Pressure Sensor Test page 78 | map signal low
Engine Intake Manifold #1 Pressure | WARNING | 3415 | Manifold pressure above normal; least severe. | Intake Manifold Pressure Sensor Test page 78 | map high warn
Engine Intake Manifold #1 Pressure | WARNING | 3417 | Manifold pressure below normal; least severe. | Intake Manifold Pressure Sensor Test page 78 | map low warn
Engine Intake Manifold 1 Temperature | ALARM | 3500 | Manifold temp above normal; high severe. | Intake Manifold Temperature Sensor Test page 79 | iat high
Engine Intake Manifold 1 Temperature | ALARM | 3501 | Manifold temp below normal; high severe. | Intake Manifold Temperature Sensor Test page 79 | iat low
Engine Intake Manifold 1 Temperature | ALARM | 3503 | Resistance below 100 Ohms. | Intake Manifold Temperature Sensor Test page 79 | iat resistance low
Engine Intake Manifold 1 Temperature | ALARM | 3504 | Resistance OL or above 65 kOhms. | Intake Manifold Temperature Sensor Test page 79 | iat resistance high
Engine Intake Manifold 1 Temperature | WARNING | 3515 | Manifold temp above normal; least severe. | Intake Manifold Temperature Sensor Test page 79 | iat high warn
Engine Intake Manifold 1 Temperature | WARNING | 3517 | Manifold temp below normal; least severe. | Intake Manifold Temperature Sensor Test page 79 | iat low warn
Battery Potential / Power Input 1 | ALARM | 3803 | Battery voltage above 16 V; high severe. | Battery Potential/Power Output 1 Test page 64 | battery high 16V
Battery Potential / Power Input 1 | ALARM | 3804 | Battery voltage below 8.5 V; high severe. | Battery Potential/Power Output 1 Test page 64 | battery low 8.5V
Battery Potential / Power Input 1 | WARNING | 3815 | Battery voltage above 15 V; least severe. | Battery Potential/Power Output 1 Test page 64 | battery high warn
Battery Potential / Power Input 1 | WARNING | 3817 | Battery voltage below 10 V; least severe. | Battery Potential/Power Output 1 Test page 64 | battery low warn
Engine Position Sensor | ALARM | 4101 | Crankshaft sensor below normal range; high severe. | Crank Position Sensor Test page 66 | crank position sensor low
Secondary Sync | ALARM | 4201 | Timing sensor below normal range; high severe. | Engine Timing Sensor Test page 71 | engine timing sensor low
O2 Sensor | ALARM | 4300 | O2 sensor data above normal range; high severe. | Oxygen Sensor Test page 85 | oxygen sensor high
O2 Sensor | ALARM | 4301 | O2 sensor data below normal range; high severe. | Oxygen Sensor Test page 85 | oxygen sensor low
O2 Sensor | ALARM | 4303 | O2 sensor voltage above normal; may be shorted. | Oxygen Sensor Test page 85 | oxygen sensor short high
O2 Sensor | ALARM | 4304 | O2 sensor reading below normal range. | Oxygen Sensor Test page 85 | oxygen sensor low reading
O2 Sensor | ALARM | 4307 | ECU faulted; exhaust/O2 alarm. | Call Technical support. | o2 ecu fault
O2 Sensor | WARNING | 4315 | O2 sensor data above normal; least severe. | Oxygen Sensor Test page 85 | oxygen high warn
O2 Sensor | WARNING | 4317 | O2 sensor data below normal; least severe. | Oxygen Sensor Test page 85 | oxygen low warn
Engine Ignition Coil #1 | ALARM | 4503 | Ignition coil 1 voltage above normal range. | Ignition Coil Test page 77 | ignition coil 1 high
Engine Ignition Coil #1 | ALARM | 4504 | Ignition coil 1 voltage below normal range. | Ignition Coil Test page 77 | ignition coil 1 low
Engine Ignition Coil #1 | ALARM | 4507 | Ignition coil 1 mechanical system not responding. | Ignition Coil Test page 77 | ignition coil 1 mech
Engine Ignition Coil #2 | ALARM | 4603 | Ignition coil 2 voltage above normal range. | Ignition Coil Test page 77 | ignition coil 2 high
Engine Ignition Coil #2 | ALARM | 4604 | Ignition coil 2 voltage below normal range. | Ignition Coil Test page 77 | ignition coil 2 low
Engine Ignition Coil #2 | ALARM | 4607 | Ignition coil 2 mechanical system not responding. | Ignition Coil Test page 77 | ignition coil 2 mech
Engine Fuel Valve 1 Position | ALARM | 4900 | Mixer position above normal; high severe. | Fuel Mixer Valve Test page 72 | mixer position high
Engine Fuel Valve 1 Position | ALARM | 4901 | Mixer position below normal; high severe. | Fuel Mixer Valve Test page 72 | mixer position low
Engine Fuel Valve 1 Position | ALARM | 4903 | Mixer position signal above 4900 mV. | Fuel Mixer Valve Test page 72 | mixer signal high
Engine Fuel Valve 1 Position | ALARM | 4904 | Mixer position signal below 120 mV. | Fuel Mixer Valve Test page 72 | mixer signal low
Engine Fuel Valve 1 Position | ALARM | 4907 | Fuel mixer mechanical system not responding. | Mixer Valve Power Test page 82 | mixer power test
Engine Fuel Valve 1 Position | WARNING | 4915 | Mixer position above normal; least severe. | Fuel Mixer Valve Test page 72 | mixer high warn
Engine Fuel Valve 1 Position | WARNING | 4917 | Mixer position below normal; least severe. | Fuel Mixer Valve Test page 72 | mixer low warn
Engine Speed | ALARM | 5100 | Engine speed above normal; high severe. | Engine Speed Test page 70 | engine speed high
Engine Speed | ALARM | 5101 | Engine speed below normal; high severe. | Engine Speed Test page 70 | engine speed low
Engine Speed | WARNING | 5115 | Engine speed above normal; least severe. | Engine Speed Test page 70 | engine speed high warn
Engine Speed | WARNING | 5117 | Engine speed below normal; least severe. | Engine Speed Test page 70 | engine speed low warn
Cylinder Head Temperature 1 | ALARM | 5200 | CHT above normal; high severe. | Cylinder Head Temperature Sensor Test page 67 | cylinder head temp high
Cylinder Head Temperature 1 | ALARM | 5201 | CHT below normal; high severe. | Cylinder Head Temperature Sensor Test page 67 | cylinder head temp low
Cylinder Head Temperature 1 | ALARM | 5203 | CHT resistance above normal; >1.8 MΩ. | Cylinder Head Temperature Sensor Test page 67 | cht resistance high
Cylinder Head Temperature 1 | ALARM | 5204 | CHT resistance below normal; <15 Ω. | Cylinder Head Temperature Sensor Test page 67 | cht resistance low
Cylinder Head Temperature 1 | WARNING | 5215 | CHT above normal; least severe. | Cylinder Head Temperature Sensor Test page 67 | cht high warn
Cylinder Head Temperature 1 | WARNING | 5217 | CHT below normal; least severe. | Cylinder Head Temperature Sensor Test page 67 | cht low warn
Engine Fuel Shutoff 2 Control | ALARM | 5303 | Voltage for fuel shutoff signal above nominal. | Fuel Shutoff 2 (SOV2) Control Test page 75 | sov2 voltage high
Engine Fuel Shutoff 2 Control | ALARM | 5304 | Fuel shutoff signal below nominal or short detected. | Fuel Shutoff 2 (SOV2) Control Test page 75 | sov2 voltage low short
Engine Oil Level | WARNING | 5415 | Oil level sensor reading high. | Oil Level Sensor Test page 83 | oil level high
Engine Oil Level | WARNING | 5417 | Oil level sensor reading below nominal. | Oil Level Sensor Test page 83 | oil level low
Overload Cooldown | WARNING | 7000 | Unit running in cool down mode due to overload. | Allow unit to finish cooldown; verify load on unit (overload test). | overload cooldown
