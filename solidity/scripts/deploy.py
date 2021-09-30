#!/usr/bin/python3
from brownie import MyToken, accounts


def main():
    MyToken.deploy({"from": accounts[0]})