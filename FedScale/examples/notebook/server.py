import sys, os

from fedscale.core.execution.client import Client
from fedscale.core.aggregation.aggregator import Aggregator
from fedscale.core.logger.execution import args
Demo_Aggregator = Aggregator(args)
### On CPU
args.use_cuda = "False"
Demo_Aggregator.run()