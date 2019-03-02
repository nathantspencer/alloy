import subprocess

print('Watching scss directory for changes...')
subprocess.check_output(['sass','--watch', 'alloy/static/scss/:alloy/static/css/'])
