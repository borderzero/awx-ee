# plugins/pre_hook.py
from ansible.plugins.callback import CallbackBase
import subprocess
import os

class CallbackModule(CallbackBase):
    CALLBACK_VERSION   = 2.0
    CALLBACK_TYPE      = 'notification'
    CALLBACK_NAME      = 'pre_hook'

    def v2_playbook_on_start(self, playbook):
        # this runs once before any plays/tasks
        self._display.banner("▶️  [pre_hook] Starting Border0 VPN…")
        
        # Set up environment with debug logging
        env = os.environ.copy()
        env['BORDER0_LOG_LEVEL'] = 'debug'
        env['BORDER0_VERY_VERBOSE'] = 'true'
        
        # Open log file for capturing border0 output
        log_file = open('/tmp/border0.log', 'w')
        
        subprocess.Popen(
            ['/bin/border0', 'node', 'start', '--start-vpn'],
            env=env,
            stdout=log_file,
            stderr=subprocess.STDOUT,
        )
        self._display.banner("✅  [pre_hook] VPN starting in background, logs at /tmp/border0.log")
