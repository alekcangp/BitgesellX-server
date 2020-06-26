.. image:: https://travis-ci.org/kyuupichan/bitgesellx.svg?branch=master
    :target: https://travis-ci.org/kyuupichan/bitgesellx
.. image:: https://coveralls.io/repos/github/kyuupichan/bitgesellx/badge.svg
    :target: https://coveralls.io/github/kyuupichan/bitgesellx

===============================================
BitgesellX - Reimplementation of electrumx server
===============================================

  :Licence: MIT
  :Language: Python (>= 3.7)
  :Original Author: Neil Booth

This project is a fork of `kyuupichan/electrumx <https://github.com/kyuupichan/electrumx>`_.
The original author dropped support for Bitcoin, which we intend to keep.

BitgesellX allows users to run their own Electrum server for bitgesell. It connects to your
full node and indexes the blockchain, allowing efficient querying of history of
arbitrary addresses. The server can be exposed publicly, and joined to the public network
of servers via peer discovery. As of May 2020, a significant chunk of the public
Electrum server network runs BitgesellX.

Documentation
=============

See `readthedocs <https://bitgesellx.readthedocs.io/>`_.

