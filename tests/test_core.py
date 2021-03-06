#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
import os
import json
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
import user_deprovision  # NOQA

expected_filename = os.path.join(
    os.path.dirname(__file__),
    './expected/core.json'
)
input_filename = os.path.join(
    os.path.dirname(__file__),
    './input/core.json'
)
config_filname = os.path.join(os.path.dirname(__file__), './config.json')

with open(expected_filename) as expected_file:
    expected = json.load(expected_file)

with open(input_filename) as input_file:
    input = json.load(input_file)

with open(config_filname) as config_file:
    config = json.load(config_file)

core = user_deprovision.DeleteUser(config['access_token'])


class CoreLogicTests(unittest.TestCase):

    def check_schedule_for_user(self):
        expected_result = expected['check_schedule_for_user'][0]
        actual_result = core.check_schedule_for_user(
            input['check_schedule_for_user'][0]['user_id'],
            input['check_schedule_for_user'][0]['schedule']
        )
        self.assertEqual(expected_result, actual_result)
        expected_result = expected['check_schedule_for_user'][1]
        actual_result = core.check_schedule_for_user(
            input['check_schedule_for_user'][1]['user_id'],
            input['check_schedule_for_user'][1]['schedule']
        )
        self.assertEqual(expected_result, actual_result)

    def check_team_for_user(self):
        expected_result = expected['check_team_for_user'][0]
        actual_result = core.check_team_for_user(
            input['check_team_for_user'][0]['user_id'],
            input['check_team_for_user'][0]['team_users']
        )
        self.assertEqual(expected_result, actual_result)
        expected_result = expected['check_team_for_user'][1]
        actual_result = core.check_team_for_user(
            input['check_team_for_user'][1]['user_id'],
            input['check_team_for_user'][1]['team_users']
        )
        self.assertEqual(expected_result, actual_result)

    def get_user_layer_index(self):
        expected_result = expected['get_user_layer_index'][0]
        actual_result = core.get_user_layer_index(
            input['get_user_layer_index'][0]['user_id'],
            input['get_user_layer_index'][0]['schedule_layer']
        )
        self.assertEqual(expected_result, actual_result)
        expected_result = expected['get_user_layer_index'][1]
        actual_result = core.get_user_layer_index(
            input['get_user_layer_index'][1]['user_id'],
            input['get_user_layer_index'][1]['schedule_layer']
        )
        self.assertEqual(expected_result, actual_result)

    def get_target_indices(self):
        expected_result = expected['get_target_indices'][0]
        actual_result = core.get_target_indices(
            input['get_target_indices'][0]['id'],
            input['get_target_indices'][0]['escalation_rules']
        )
        self.assertEqual(expected_result, actual_result)
        expected_result = expected['get_target_indices'][1]
        actual_result = core.get_target_indices(
            input['get_target_indices'][1]['id'],
            input['get_target_indices'][1]['escalation_rules']
        )
        self.assertEqual(expected_result, actual_result)

    def remove_user_from_layer(self):
        expected_result = expected['remove_user_from_layer'][0]
        actual_result = core.remove_user_from_layer(
            input['remove_user_from_layer'][0]['index'],
            input['remove_user_from_layer'][0]['schedule_layer']
        )
        self.assertEqual(expected_result, actual_result)

    def remove_from_escalation_policy(self):
        expected_result = expected['remove_from_escalation_policy'][0]
        actual_result = core.remove_from_escalation_policy(
            input['remove_from_escalation_policy'][0]['indices'],
            input['remove_from_escalation_policy'][0]['escalation_rules']
        )
        self.assertEqual(expected_result, actual_result)

    def cache_schedule(self):
        expected_result = expected['cache_schedule'][0]
        actual_result = core.cache_schedule(
            input['cache_schedule'][0]['schedule'],
            input['cache_schedule'][0]['cache']
        )
        self.assertEqual(expected_result, actual_result)

    def cache_team(self):
        expected_result = expected['cache_team'][0]
        actual_result = core.cache_team(
            input['cache_team'][0]['team'],
            input['cache_team'][0]['cache']
        )
        self.assertEqual(expected_result, actual_result)

    def cache_escalation_policy(self):
        expected_result = expected['cache_escalation_policy'][0]
        actual_result = core.cache_escalation_policy(
            input['cache_escalation_policy'][0]['escalation_policy'],
            input['cache_escalation_policy'][0]['cache']
        )
        self.assertEqual(expected_result, actual_result)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(CoreLogicTests('check_schedule_for_user'))
    suite.addTest(CoreLogicTests('check_team_for_user'))
    suite.addTest(CoreLogicTests('get_user_layer_index'))
    suite.addTest(CoreLogicTests('get_target_indices'))
    suite.addTest(CoreLogicTests('remove_user_from_layer'))
    suite.addTest(CoreLogicTests('remove_from_escalation_policy'))
    suite.addTest(CoreLogicTests('cache_schedule'))
    suite.addTest(CoreLogicTests('cache_team'))
    suite.addTest(CoreLogicTests('cache_escalation_policy'))
    return suite
