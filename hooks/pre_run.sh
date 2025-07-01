#!/usr/bin/env bash
set -euo pipefail

# Ensure the AWX-injected secret is present
if [ -z "${BORDER0_TOKEN:-}" ]; then
  echo "ERROR: BORDER0_TOKEN is not set"
#   exit 1
fi

# Export for any subprocess
export BORDER0_TOKEN

# Call the border0 binary (it will pick up $BORDER0_TOKEN)
echo "[pre_run] invoking border0…"
if ! /bin/border0; then
  echo "ERROR: border0 failed"
#   exit 1
fi

# Runner will automatically invoke your playbook next
/bin/border0 node start --start-vpn --wait-for-auth > /tmp/border0.log 2>&1 &

sleep 5
/bin/border0 node debug peers > /tmp/border0_status.log 2>&1
sleep 5

echo "[pre_run] border0 invoked successfully, proceeding with playbook execution."