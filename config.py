import logging

########################################################################
#
#   General options

### Logging
log_level = logging.INFO
log_format = '%(asctime)s %(levelname)s %(name)s: %(message)s'

### Server
listening_ip = "0.0.0.0"
listening_port = 8082

### Cost Estimate
kwh_rate        = 0.174  # Rate in currency_type to calculate cost to run job
currency_type   = "AUD"   # Currency Symbol to show when calculating cost to run job

########################################################################
#
#   GPIO Setup (BCM SoC Numbering Schema)
#
#   Check the RasPi docs to see where these GPIOs are
#   connected on the P1 header for your board type/rev.
#   These were tested on a Pi B Rev2 but of course you
#   can use whichever GPIO you prefer/have available.

### Outputs
gpio_heat = 23  # Switches zero-cross solid-state-relay
gpio_cool = 10  # Regulates PWM for 12V DC Blower
gpio_air  = 9   # Switches 0-phase det. solid-state-relay

heater_invert = 0 # switches the polarity of the heater control

### Inputs
gpio_door = 12

### Thermocouple Adapter selection (MAX31855 or MAX6675)
max31855 = 0
max6675 = 1

### Thermocouple I2C Connection
gpio_sensor_cs = 27
gpio_sensor_clock = 22
gpio_sensor_data = 17


########################################################################
#
#   PID parameters

pid_ki = 0.1  # Integration
pid_kd = 0.4  # Derivative
pid_kp = 0.5  # Proportional


########################################################################
#
#   Simulation parameters

sim_t_env      = 25.0   # deg C
sim_c_heat     = 100.0  # J/K  heat capacity of heat element
sim_c_kiln     = 2000.0 # J/K  heat capacity of kiln
sim_p_heat     = 3500.0 # W    heating power of kiln
sim_R_o_nocool = 1.0    # K/W  thermal resistance kiln -> environment
sim_R_o_cool   = 0.05   # K/W  " with cooling
sim_R_ho_noair = 0.1    # K/W  thermal resistance heat element -> kiln
sim_R_ho_air   = 0.05   # K/W  " with internal air circulation


########################################################################
#
#   Time and Temperature parameters

temp_scale          = "c" # c = Celsius | f = Fahrenheit - Unit to display
time_scale_slope    = "s" # s = Seconds | m = Minutes | h = Hours - Slope displayed in temp_scale per time_scale_slope
time_scale_profile  = "s" # s = Seconds | m = Minutes | h = Hours - Enter and view target time in time_scale_profile

########################################################################
#
#   Logging parameters
ubidots_url = 'https://things.ubidots.com/api/v1.6/devices/kiln-controller-v0.1'
ubidots_id = "58b3781b762542682ea93d8f"
ubidots_api_key = "644b7572d52b11b08150482c60a27cec4c58f666"
ubidots_token = "xDcEBxGgmmQR0owTeamfLSFSdhZXii"
