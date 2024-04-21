#!/bin/bash
# Script to copy the master's public key into authorized_keys
cat /shared-keys/id_rsa.pub >> /root/.ssh/authorized_keys
# Start the SSH service
exec /usr/sbin/sshd -D -e
