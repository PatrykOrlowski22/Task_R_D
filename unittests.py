# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:09:08 2023

@author: Patryk
"""
import unittest
import os.path
import Task_RD as TASK

class TestTASK(unittest.TestCase):
    def test_task(self):
        TASK.main()
        wideo = TASK.test_capture
        image = TASK.test_sample
        self.assertIsNotNone(wideo)
        self.assertIsNotNone(image)
        self.assertTrue(os.path.exists('processed/frame0_283_70.png'))
        self.assertTrue(os.path.exists('processed/frame3_253_100.png'))
        self.assertTrue(os.path.exists('processed/frame0_223_140.png'))
        #self.assertEqual(first, second)

if __name__ == '__main__':
    unittest.main()