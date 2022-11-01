'''
Template file for USACO input, output files.

Steps:
1. Dowload test cases and put in your dowloads folder.
2. Complete read_input() function returns a tuple.
3. Complete solve() function which takes read_input().
    solve() returns a value that would be written in ./kur folder

submit() submits your function and creates results 
in ./kur against the ground truth
'''

import sys
import glob
import os, glob, filecmp
from os import listdir
from os.path import isfile, join
from typing import Callable

FOLDER_WITH_TESTS = '/home/ncuong/Downloads'

def _print_lines(lines, chars):
    for line in lines:
        if chars == float('inf'): print(line)
        else: print(line[:chars])

def print_mismatch(test_cases = [], chars = float('inf')):
    files = glob.glob(f'{FOLDER_WITH_TESTS}/*')
    latest = max(files, key=os.path.getctime)
    onlyfiles = [f for f in listdir(latest) if isfile(join(latest, f))]
    T = len(onlyfiles)//2
    errors = 0
    if not test_cases: test_cases = range(1,T+1)
    for i in test_cases:
        actual_path = os.path.join(latest,'kur',f'{i}.out')
        exp_path = os.path.join(latest,f'{i}.out')
        if not filecmp.cmp(actual_path, exp_path):
            file_exp = open(exp_path, 'r')
            lines_exp = file_exp.readlines()
            file_act = open(actual_path, 'r')
            lines_act = file_act.readlines()
            print(f'Test case {i}:')
            print('Expected: ', end = '')
            _print_lines(lines_exp, chars)
            print('Actual: ', end = '')
            _print_lines(lines_act, chars)
            errors += 1
    if not errors: print('SUCCESS')
    else: print('Errors:', errors)


def submit(solve: Callable, read_input: Callable, test_cases = [], new_line = False):
    files = glob.glob(f'{FOLDER_WITH_TESTS}/*')
    latest = max(files, key=os.path.getctime)
    res_path = os.path.join(latest,'kur')
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    onlyfiles = [f for f in listdir(latest) if isfile(join(latest, f))]
    T = len(onlyfiles)//2
    if not test_cases: test_cases = range(1,T+1)
    for i in test_cases:
        in_path = os.path.join(latest,f'{i}.in')
        out_path = os.path.join(latest,'kur',f'{i}.out')
        sys.stdin = open(in_path, "r")
        sys.stdout = open(out_path, "w")
        if not new_line:
            print(solve(read_input()))
        else:
            res = solve(read_input())
            for ans  in res:
                print(ans)
        sys.stdout.close()
    for i in test_cases:
        actual_path = os.path.join(latest,'kur',f'{i}.out')
        exp_path = os.path.join(latest,f'{i}.out')
        assert filecmp.cmp(actual_path, exp_path)