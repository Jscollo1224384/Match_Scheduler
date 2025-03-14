import sys
import unittest
import Testing.unit_tests
from Testing import unit_tests
from Testing.unit_tests import LeagueTests

def run_unit_tests():

    tests = unit_tests.LeagueTests()

    tests.all_leagues_have_unique_teams()
    tests.all_leagues_have_unique_locations()
    tests.all_teams_have_a_location()
    tests.all_locations_have_at_least_one_team()
    tests.number_of_matches_is_number_of_teams_multiplied_by_number_of_teams_minus_one()

    print("Unit tests passed")

def main(debug):

    if debug:
        run_unit_tests()
    return 0

if __name__ == '__main__':
    sys.exit(main(True))
