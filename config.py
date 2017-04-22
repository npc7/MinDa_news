# !/usr/bin/python
# -*- coding: utf-8 -*-


import os

__author__ = 'AidChow'

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """default config"""
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = os.environ.get('DB_USER') or 'your mysql database user name'
    MYSQL_DATABASE_PASSWORD = os.environ.get('DB_PASSWORD') or 'your mysql database password'
    MYSQL_DATABASE_CHARSET = 'utf8mb4'


class DevelopmentConfig(Config):
    """development env"""
    DEBUG = True
    MYSQL_DATABASE_DB = 'minda__news_dev'


class TestingConfig(Config):
    """Test env"""
    TESTING = True
    MYSQL_DATABASE_DB = 'minda_news_test'


class ProductionConfig(Config):
    """product env"""
    MYSQL_DATABASE_DB = 'minda_news'


# app.config 配置
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': DevelopmentConfig,
    'default': ProductionConfig
}
