# ee-entrypoint.sh
#!/usr/bin/env bash
set -euo pipefail

echo "🔔 running custom pre-hook…"
# /usr/local/bin/pre_ansible.sh

# Runner will automatically invoke your playbook next
/bin/border0 node start --start-vpn --wait-for-auth > /tmp/border0.log 2>&1 &

sleep 5
/bin/border0 node debug peers > /tmp/border0_status.log 2>&1
sleep 5

touch /tmp/worked.crumb

echo "[pre_run] border0 invoked successfully, proceeding with playbook execution."

echo "▶️ handing off to ansible-runner"
exec ansible-runner "$@"
