# plugins/pre_hook.py
from ansible.plugins.callback import CallbackBase
import subprocess

class CallbackModule(CallbackBase):
    CALLBACK_VERSION   = 2.0
    CALLBACK_TYPE      = 'notification'
    CALLBACK_NAME      = 'pre_hook'

    def v2_playbook_on_start(self, playbook):
        # this runs once before any plays/tasks
        self._display.banner("▶️  [pre_hook] Starting Border0 VPN…")
        subprocess.run(
            ['/bin/border0', 'node', 'start', '--start-vpn'],
            check=True,
        )
        self._display.banner("✅  [pre_hook] VPN up, continuing…")
