#!/usr/bin/env python

"""Tests for `amazon_gift_reload` package."""

import pytest
from selenium import webdriver
from amazon_gift_reload import amazon_gift_reload


@pytest.fixture
def amazon_gift_reloader():
    return amazon_gift_reload.AmazonGiftReloader(0.5, 5, "test@email.com", "password")


def test_amazon_gift_reloader(amazon_gift_reloader):
    assert "amazon" in amazon_gift_reloader.RELOAD_URL


def test_amazon_gift_reloader_sign_in(amazon_gift_reloader):
    assert "amazon" in amazon_gift_reloader.sign_in()
