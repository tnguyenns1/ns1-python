#
# Copyright (c) 2014 NSONE, Inc.
#
# License under The MIT License (MIT). See LICENSE in project root.
#

###########
# TWISTED #
###########

from nsone import NSONE, Config
from twisted.internet import defer, reactor

config = Config()
# load default config
config.loadFromFile(Config.DEFAULT_CONFIG_FILE)
# to load directly from apikey instead, use
# config.createFromAPIKey('qACMD09OJXBxT7XOuRs8')

# override default synchronous transport. note, this would normally go
# in config file.
config['transport'] = 'twisted'
nsone = NSONE(config=config)


@defer.inlineCallbacks
def getQPS():
    # when twisted transport is in use, all of the NSONE methods return
    # Deferred. yield them to gather the results, or add callbacks/errbacks
    # to be run when results are available
    zone = yield nsone.loadZone('test.com')
    qps = yield zone.qps()
    defer.returnValue(qps)


def gotQPS(result):
    print("current QPS for test.com: %s" % result['qps'])
    reactor.stop()


def handleError(failure):
    print(failure)
    reactor.stop()

qps = getQPS()
qps.addCallback(gotQPS)
qps.addErrback(handleError)

reactor.run()