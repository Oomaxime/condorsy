import os

class Config:
    SECRET_KEY = 'your-secret-key'
<<<<<<< HEAD
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://root:pass@mongodb:27017/condorcy?authSource=admin')
=======
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://root:pass@mongodb:27017/condorsy?authSource=admin')
>>>>>>> b377c54 (merge Ãà 2 mainsÃ)

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False