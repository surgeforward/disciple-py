import mongoengine
import config

def main():
    mongoengine.connect(config.MONGO_DATABASE, host=config.MONGO_HOST,
                        port=config.MONGO_PORT, username=config.MONGO_USERNAME,
                        password=config.MONGO_PASSWORD)
    print 'hello world'

if __name__ == '__main__':
    main()
