import os

class Config:
    SECRET_KEY = 'your-secret-key'
    MONGO_URI = 'mongodb://root:pass@mongodb:27017/condorsy?authSource=admin'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False