# This file is part of wger Workout Manager.
# This file is also part of VPATEL's GRAD PROJECT 2021
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from wger.manager.views import workout_generator

from wger.core.tests.base_testcase import (
    WgerTestCase
)

from wger.exercises.models import (
    Exercise
)

class WorkoutGeneratorTest(WgerTestCase):
    results = []

    def generateList(self):
        self.results = workout_generator.generate("Yet another category", "Intermediate")

    def test_verify_level_conversion(self):

        # beginner = 1
        self.assertEqual(workout_generator.convertLevel("Beginner"), 1)

        # Intermediate = 2
        self.assertEqual(workout_generator.convertLevel("Intermediate"), 2)

        # Advanced = 3
        self.assertEqual(workout_generator.convertLevel("Advanced"), 3)

    def test_generated_list_size(self):
        # get exercise data from test-exercises.json
        exercises = Exercise.objects.filter(category__name="Yet another category")

        # generate list of workouts
        self.generateList()

        # intermediate level gives 6 exercises
        self.assertEqual(len(self.results), 6)

    def test_generated_list_reprange_low(self):
        self.generateList()

        # low range for intermediate = 10
        for workout in self.results:
            self.assertEqual(workout[2], '10')

    def test_generated_list_reprange_high(self):
        self.generateList()

        # high range for intermediate = 20
        for workout in self.results:
            self.assertEqual(workout[3], '20')


