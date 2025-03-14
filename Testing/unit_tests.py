import unittest
import json
import argparse
from itertools import permutations

file = "/Users/jscollo/Match_Scheduler/Testing/test_league_8_teams.json"


try:
    with open(file, 'r') as file:
        config_data = json.load(file)
except Exception as e:
    print(f'Failed to read config data: {e}')



class LeagueTests(unittest.TestCase):
   teams = config_data.get('teams')
   locations = config_data.get('locations')
   locations_from_teams = config_data.get('locations_from_teams')
   teams_from_locations = config_data.get('teams_from_locations')

   def all_leagues_have_unique_teams(self):
       self.assertEquals(len(self.teams), len(set(self.teams)))

   def all_leagues_have_unique_locations(self):
       self.assertEquals(len(self.locations), len(set(self.locations)))

   def all_teams_have_a_location(self):
       for team in self.teams:
           self.assertIsNotNone(self.locations_from_teams[team])

   def all_locations_have_at_least_one_team(self):
       for location in self.locations:
           self.assertIsNotNone(self.teams_from_locations[location])

   def number_of_matches_is_number_of_teams_multiplied_by_number_of_teams_minus_one(self):
       matches = list(permutations(self.teams, 2))
       self.assertEquals(len(matches), len(self.teams) * (len(self.teams) - 1))


if __name__ == '__main__':
    unittest.main()