
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "skjfhieuhrvkbjbkjfgojhdflgjtoihj"
    OPENAI_API_KEY = "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"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
