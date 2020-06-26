#!/bin/sh
###############
# run_bitgesellx
###############

# configure bitgesellx
export COIN=Bitgesell
export DAEMON_URL=http://rpcuser:rpcpassword@127.0.0.1
export NET=mainnet
export CACHE_MB=400
export DB_DIRECTORY=/home/username/.bitgesellx/db
export SSL_CERTFILE=/home/username/.bitgesellx/certfile.crt
export SSL_KEYFILE=/home/username/.bitgesellx/keyfile.key
export BANNER_FILE=/home/username/.bitgesellx/banner
export DONATION_ADDRESS=bgl1q03382mlq43qyueh6fchxyuyk9z7k4uakrrf94w

# connectivity
export HOST=
export TCP_PORT=50001
export SSL_PORT=50002

# visibility
export REPORT_HOST=hostname.com
export RPC_PORT=8000

# run bitgesellx
ulimit -n 10000
/usr/local/bin/bitgesellx_server 2>> /home/username/.bitgesellx/bitgesellx.log >> /home/username/.bitgesellx/bitgesellx.log &

######################
# auto-start bitgesellx
######################

# add this line to crontab -e
# @reboot /path/to/run_bitgesellx.sh
