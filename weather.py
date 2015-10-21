
import requests
import requests_mock
import os

secret_key = os.environ['WU_KEY']

zipcode = input("Enter you zipcode  ")


class Current:

    def __init__(self, zipcode):
        self.zipcode = zipcode

    def currentconditions():
        wu_url = 'http://api.wunderground.com/api/{}/geolookup/conditions/q/{}.json'.format(
            secret_key, zipcode)
        c = requests.get(wu_url)
        parsed_json = c.json()
        location = parsed_json['location']['city']
        state = parsed_json['location']['state']
        temp_f = parsed_json['current_observation']['temp_f']
        time = parsed_json['current_observation']['observation_time_rfc822']
        print("At {} temperature in {}, {} is: {}\u00b0F".format(
            time, location, state, temp_f))
        c.close()


class TenDay:
    pass


class Sunrise:

    def __init__(self, zipcode):
        self.zipcode = zipcode

    def suninfo():
        wu_url = 'http://api.wunderground.com/api/{}/astronomy/q/{}.json'.format(
            secret_key, zipcode)
        c = requests.get(wu_url)
        parsed_json = c.json()
        sunrise = "{}:{}".format(parsed_json['sun_phase']['sunrise'][
            'hour'], parsed_json['sun_phase']['sunrise']['minute'])
        sunset = "{}:{}".format(parsed_json['sun_phase']['sunset'][
                                'hour'], parsed_json['sun_phase']['sunset']['minute'])

        print("Sunrise is at {}, sunset is at {} today".format(sunrise, sunset))
        c.close()


class Alerts:
    pass


class Hurricanes:
    pass
