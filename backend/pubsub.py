import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-ae567020-b3d8-453c-9710-4dce8f17061a'
pnconfig.publish_key = 'pub-c-8e0d1e60-c344-4233-b223-2911760df6e3'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message object: {message_object}')
    
pubnub.add_listener(Listener())

def main():
    time.sleep(1)  # this allows subscribe to complete before publish
    
    pubnub.publish().channel(TEST_CHANNEL).message({ 'JMkey': 'JMvalue'}).sync()
    
if __name__ == '__main__':
    main()

