#!/usr/bin/env python3

import argparse
import xmlrpc.client

parser = argparse.ArgumentParser(description='a script to control aria2 XML-RPC server')
parser.add_argument('--rpc-method', nargs=None, default='addUri', help='Set RPC method.')
parser.add_argument('--rpc-server', nargs=None, default='http://127.0.0.1:6800/rpc', help='Set XML-RPC server address.')
parser.add_argument('--rpc-secret', nargs=None, default=None, help='Set RPC secret authorization token.')

args, other_options = parser.parse_known_args()

sep_index = other_options.index('--')
opt_args = dict((other_options[i].lstrip('--'), other_options[i+1]) for i in range(0, len(other_options[0:sep_index]), 2))
pos_args = other_options[sep_index+1:]

params = []

if args.rpc_secret is not None:
    params.append('token:{0}'.format(args.rpc_secret))

if args.rpc_method == 'addUri':
    params.append(pos_args)
elif len(pos_args) > 0:
    params.append(pos_args[0])

with xmlrpc.client.ServerProxy(args.rpc_server) as proxy:
    getattr(proxy.aria2, args.rpc_method)(*params)
